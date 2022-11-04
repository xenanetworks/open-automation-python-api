from typing import Any, Dict, List, Literal, Union
from xoa_driver.enums import (
    ReservedStatus,
    AutoNegFECOption,
    AutoNegMode,
    AutoNegTecAbility,
    PauseMode,
    LinkTrainingInitCondition,
    LinkTrainingMode,
    NRZPreset,
    PAM4FrameSize,
    TimeoutMode,
)

from xoa_driver.internals.core import commands
from xoa_driver.misc import Token
from xoa_driver.utils import apply
from xoa_driver.internals.ports.port_l23.family_l import FamilyL
from xoa_driver.internals.ports.port_l23.family_l1 import FamilyL1
from xoa_driver.ports import GenericAnyPort
from xoa_driver.testers import L23Tester, L47Tester, GenericAnyTester
from xoa_driver.lli import commands

PcsPmaSupported = (FamilyL, FamilyL1)
AutoNegSupported = (FamilyL, FamilyL1)
LinkTrainingSupported = FamilyL


class ConfigError(Exception):
    def __init__(self) -> None:
        self.msg = ""

    def __repr__(self) -> str:
        return self.msg

    def __str__(self) -> str:
        return self.msg


class NotConnectedError(ConfigError):
    def __init__(self) -> None:
        self.msg = "No tester is connected!"


class NoSuchModuleError(ConfigError):
    def __init__(self, module_id: int) -> None:
        self.msg = f"No such module {module_id}!"


class NoSuchPortError(ConfigError):
    def __init__(self, port_id: int) -> None:
        self.msg = f"No such module {port_id}!"


class NotSupportPcsPmaError(ConfigError):
    def __init__(self, port: GenericAnyPort) -> None:
        module_id, port_id = port.kind.module_id, port.kind.port_id
        self.msg = f"This port {module_id}/{port_id} does not support pcs_pma!"


class NotSupportAutoNegError(ConfigError):
    def __init__(self, port: GenericAnyPort) -> None:
        module_id, port_id = port.kind.module_id, port.kind.port_id
        self.msg = f"This port {module_id}/{port_id} does not support auto negotiation!"


class NotSupportLinkTrainError(ConfigError):
    def __init__(self, port: GenericAnyPort) -> None:
        module_id, port_id = port.kind.module_id, port.kind.port_id
        self.msg = f"This port {module_id}/{port_id} does not support link training!"


class NotRightLaneLengthError(ConfigError):
    def __init__(self, lane: List[int]) -> None:

        self.msg = f"Lane {lane} should be length of 4!"


class NotRightLaneValueError(ConfigError):
    def __init__(self, lane: List[int]) -> None:
        self.msg = f"Lane {lane} should be a list of 4 integers ranges from 0 to 255!"


async def connect(
    tester_type: str,
    host: str,
    username: str,
    password: str = "xena",
    port: int = 22606,
) -> GenericAnyTester:
    """Connect to a Xena tester.

    :param tester_type: Tester type, either "l23" or "l47"
    :type tester_type: str
    :param host: IP address or hostname of the tester.
    :type host: str
    :param username: Username used to log on the tester
    :type username: str
    :param password: Password of the tester, defaults to "xena"
    :type password: str, optional
    :param port: the port number for establishing the TCP connection, defaults to 22606
    :type port: int, optional
    :return: tester object
    :rtype: :class:`~xoa_driver.testers.GenericAnyTester`
    """
    assert tester_type in ("l23", "l47"), "Para 'tester_type' not in ('l23', 'l47')!"
    class_ = {"l23": L23Tester, "l47": L47Tester}[tester_type]
    current_tester = await class_(host, username, password, port, debug=True)
    return current_tester


def get_port(
    tester: GenericAnyTester,
    module_id: int,
    port_id: int,
) -> GenericAnyPort:
    if tester is None:
        raise NotConnectedError()
    try:
        module = tester.modules.obtain(module_id)
    except KeyError:
        raise NoSuchModuleError(module_id)
    try:
        port = module.ports.obtain(port_id)
    except KeyError:
        raise NoSuchModuleError(port_id)
    return port


async def port_reserve(port: GenericAnyPort) -> List[Token]:
    """Reserve a port regardless whether it is owned by others or not. 

    :param port: The port to reserve
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :return: 
    :rtype: typing.List[Token]
    """
    tokens = []
    r = await port.reservation.get()
    if r.status == ReservedStatus.RESERVED_BY_OTHER:
        tokens.append(port.reservation.set_relinquish())
        tokens.append(port.reservation.set_reserve())
    elif r.status == ReservedStatus.RELEASED:
        tokens.append(port.reservation.set_reserve())
    return tokens


async def port_reset(port: GenericAnyPort) -> List[Token]:
    """Reset a port

    :param port: The port to reset
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :return: 
    :rtype: typing.List[Token]
    """
    return [(port.reset.set())]


async def anlt_status(
    port: GenericAnyPort,
) -> Dict[str, Any]:
    """Get ANLT status

    :param port: the port to get ANLT status from
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :return: ANLT status
    :rtype: typing.Dict[str, Any]
    """

    # if not isinstance(port, LinkTrainingSupported):
    #     raise NotSupportLinkTrainError(port)
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    r0 = commands.PL1_CFG_TMP(
        _connection=conn, _module=mid, _port=pid, _serdes_xindex=0, _type=0
    ).get()
    r1 = commands.PP_AUTONEGSTATUS(_connection=conn, _module=mid, _port=pid).get()
    r2 = commands.PP_LINKTRAIN(_connection=port._conn, _module=mid, _port=pid).get()

    tokens = [
        # PL1_CFG_TMP[0,0] ?,
        r0,
        # port.pcs_pma.auto_neg.status.get(),
        r1,
        # port.pcs_pma.link_training.settings.get(),
        r2,
    ]
    *_, link_recovery, autoneg, linktrain = await apply(*tokens)
    return {
        "auto_neg_enabled": (autoneg.mode),
        "link_train_mode": (linktrain.mode),
        "link_train_timeout": (linktrain.timeout_mode),
        "link_recovery": (link_recovery.on_off),
    }


async def an_config(
    port: GenericAnyPort,
    allow_loopback: bool,
    enable: bool,
) -> List[Token]:
    """Configure auto-negotiation

    :param port: the port to configure AN
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param allow_loopback: whether allowing the port in loopback mode
    :type allow_loopback: bool
    :param enable: enable or disable autonegotiation
    :type enable: bool
    :return: 
    :rtype: typing.List[Token]
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    page_xindex = 8765
    register_xindex = 3
    loopback_hexstring = f"0x0000000{int(allow_loopback)}"
    autoneg_enabled = AutoNegMode(enable)
    r1 = commands.PX_RW(conn, mid, pid, page_xindex, register_xindex).set(
        loopback_hexstring
    )
    r2 = commands.PP_AUTONEG(conn, mid, pid).set(
        autoneg_enabled,
        AutoNegTecAbility.DEFAULT_TECH_MODE,
        AutoNegFECOption.NO_FEC,
        AutoNegFECOption.NO_FEC,
        PauseMode.NO_PAUSE,
    )

    tokens = [r1, r2]
    return tokens


async def an_status(port: GenericAnyPort) -> Dict[str, Any]:
    """Get the auto-negotiation status

    :param port: the port to get auto-negotiation status
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :return: 
    :rtype: typing.Dict[str, Any]
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    *_, auto_neg_info = await apply(commands.PL1_AUTONEGINFO(conn, mid, pid, 0).get())
    return {
        "duration": auto_neg_info.duration_us,
        "successes": auto_neg_info.negotiation_success_count,
        "timeouts": auto_neg_info.negotiation_timeout_count,
        "loss_of_sync": auto_neg_info.negotiation_loss_of_sync_count,
        "fec_negotiation_fails": auto_neg_info.negotiation_fec_fail_count,
        "hcd_negotiation_fails": auto_neg_info.negotiation_hcd_fail_count,
        "link_codewords": {
            "tx": auto_neg_info.tx_link_codeword_count,
            "rx": auto_neg_info.rx_link_codeword_count,
        },
        "next_page_messages": {
            "tx": auto_neg_info.tx_next_page_message_count,
            "rx": auto_neg_info.rx_next_page_message_count,
        },
        "unformatted pages": {
            "tx": auto_neg_info.tx_next_page_unformatted_count,
            "rx": auto_neg_info.rx_next_page_unformatted_count,
        },
    }


async def an_log(port: GenericAnyPort) -> str:
    """Show the auto-negotiation logs

    :param port: the port to get auto-negotiation logs
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :return: auto-negotiation log
    :rtype: str
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    serdes_xindex = 0
    _type = 0
    *_, log = await apply(commands.PL1_LOG(conn, mid, pid, serdes_xindex, _type).get())
    return log.log_string


async def lt_config(
    port: GenericAnyPort, enable: bool, timeout_enable: bool, mode: str
) -> List[Token]:
    """Configure link training on a port

    :param port: the port to configure LT on
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param enable: whether LT should be enabled on the port
    :type enable: bool
    :param timeout_enable: whether LT timeout should be enabled on the port
    :type timeout_enable: bool
    :param mode: LT mode, auto or interactive
    :type mode: str
    :return: 
    :rtype: typing.List[Token]
    """
    assert mode in (
        "auto",
        "interactive",
    ), "Para 'mode' not in ('auto', 'interactive')!"
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    t = (enable, timeout_enable, mode)
    tokens = []
    if t == (True, False, "interactive"):
        tokens += await lt_clear(port, 0)
        tokens += await lt_nop(port, 0)
        lm, tm = (LinkTrainingMode.FORCE_ENABLE, TimeoutMode.TIMEOUT_DISABLED)
    elif t == (True, True, "interactive"):
        lm, tm = (LinkTrainingMode.FORCE_ENABLE, TimeoutMode.DEFAULT_TIMEOUT)
    elif t == (True, False, "auto"):
        lm, tm = (LinkTrainingMode.AUTO, TimeoutMode.TIMEOUT_DISABLED)
    elif t == (True, True, "auto"):
        lm, tm = (LinkTrainingMode.AUTO, TimeoutMode.DEFAULT_TIMEOUT)
    elif t == (False, False, "auto"):
        lm, tm = (LinkTrainingMode.FORCE_DISABLE, TimeoutMode.TIMEOUT_DISABLED)
    else:  # if t == (False, True, "auto"):
        lm, tm = (LinkTrainingMode.FORCE_DISABLE, TimeoutMode.DEFAULT_TIMEOUT)

    tokens += [
        commands.PP_LINKTRAIN(conn, mid, pid).set(
            mode=lm,
            pam4_frame_size=PAM4FrameSize.P16K_FRAME,
            nrz_pam4_init_cond=LinkTrainingInitCondition.NO_INIT,
            nrz_preset=NRZPreset.NRZ_NO_PRESET,
            timeout_mode=tm,
        ),
    ]
    return tokens


async def lt_clear(port: GenericAnyPort, lane: int) -> List[Token]:
    """Clear the LT command sequence for the lane.

    :param port: the port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :return: 
    :rtype: typing.List[Token]
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    page_xindex = 8766
    register_xindex = ((0xFFFF & lane) << 16) + 0x0002
    return [
        commands.PX_RW(conn, mid, pid, page_xindex, register_xindex).set("0x00000000")
    ]


async def lt_nop(port: GenericAnyPort, lane: int) -> List[Token]:
    """No operation for the lane, used to indicate interactive use

    :param port: the port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :return: 
    :rtype: typing.List[Token]
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    page_xindex = 8766
    register_xindex = ((0xFFFF & lane) << 16) + 0x0000
    return [
        commands.PX_RW(conn, mid, pid, page_xindex, register_xindex).set("0x00010000")
    ]


async def lt_coeff_inc(
    port: GenericAnyPort, lane: int, coeff: int, value: int
) -> List[Token]:
    """Increase coeff for a lane on a port

    :param port: the port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :param coeff: coefficient index (-3, -2, -1, 0, 1)
    :type coeff: int
    :param value: the increase value
    :type count: int
    :return: 
    :rtype: typing.List[Token]
    """
    assert coeff in range(-3, 1), "Para 'coeff' not in (-3, -2, -1, 0, 1)!"
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    page_xindex = 8766
    register_xindex = ((0xFFFF & lane) << 16) + 0x0000
    aaaa = hex(value & 0xFFFF).replace("0x", "").zfill(4)
    if coeff == -3:
        coeff = 4
    if coeff == -2:
        coeff = 3
    if coeff == -1:
        coeff = 0
    if coeff == 0:
        coeff = 1
    if coeff == 1:
        coeff = 2
    cc = hex(coeff & 0xFF).replace("0x", "").zfill(2)
    return [
        commands.PX_RW(conn, mid, pid, page_xindex, register_xindex).set(
            f"0x{aaaa}01{cc}"
        )
    ]


async def lt_coeff_dec(
    port: GenericAnyPort, lane: int, coeff: int, count: int
) -> List[Token]:
    """Decrease coeff for a lane on a port

    :param port: the port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :param coeff: coefficient index (-3, -2, -1, 0, 1)
    :type coeff: int
    :param value: the decrease value
    :type count: int
    :return: 
    :rtype: typing.List[Token]
    """
    assert coeff in range(-3, 1), "Para 'coeff' not in (-3, -2, -1, 0, 1)!"
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    page_xindex = 8766
    register_xindex = ((0xFFFF & lane) << 16) + 0x0000
    aaaa = hex(count & 0xFFFF).replace("0x", "").zfill(4)
    if coeff == -3:
        coeff = 4
    if coeff == -2:
        coeff = 3
    if coeff == -1:
        coeff = 0
    if coeff == 0:
        coeff = 1
    if coeff == 1:
        coeff = 2
    cc = hex(coeff & 0xFF).replace("0x", "").zfill(2)
    return [
        commands.PX_RW(conn, mid, pid, page_xindex, register_xindex).set(
            f"0x{aaaa}02{cc}"
        )
    ]


async def lt_preset(port: GenericAnyPort, lane: int, preset: int) -> List[Token]:
    """Select a preset for the lane.

    :param port: port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :param preset: preset index to select for the lane, 1,2,3,4,5
    :type preset: int
    :return: 
    :rtype: typing.List[Token]
    """
    assert preset in range(1, 6), "Para 'preset' not in (1, 2, 3, 4, 5)!"
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    page_xindex = 8766
    register_xindex = ((0xFFFF & lane) << 16) + 0x0000
    bb = {1: "0B", 2: "0C", 3: "0D", 4: "0E", 5: "0F"}[preset]
    return [
        commands.PX_RW(conn, mid, pid, page_xindex, register_xindex).set(
            f"0x0001{bb}00"
        )
    ]


async def lt_preset0(port: GenericAnyPort, lane: int, use: str) -> List[Token]:
    """Should the preset0 (out-of-sync preset) use existing tap values or standard values.

    :param port: port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :param use: preset0 (out-of-sync preset) use existing tap values ("existing") or standard values ("standard")
    :type use: str
    :return: 
    :rtype: typing.List[Token]
    """
    assert use in (
        "existing",
        "standard",
    ), "Para 'coeff' not in ('standard', 'existing')!"
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    page_xindex = 8766
    register_xindex = ((0xFFFF & lane) << 16) + 0x0000
    preset = 0 if use == "existing" else 1
    return [
        commands.PX_RW(conn, mid, pid, page_xindex, register_xindex).set(
            f"0x0000000{preset}"
        )
    ]


async def lt_trained(port: GenericAnyPort, lane: int) -> List[Token]:
    """Announce the current lane is trained.

    :param port: port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :return: 
    :rtype: typing.List[Token]
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    page_xindex = 8766
    register_xindex = ((0xFFFF & lane) << 16) + 0x0000
    return [
        commands.PX_RW(conn, mid, pid, page_xindex, register_xindex).set(f"0x0001FF00")
    ]


async def lt_log(port: GenericAnyPort, lane: int) -> str:
    """Show the link training trace log.

    :param port: port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :return: 
    :rtype: str
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    *_, log = await apply(commands.PL1_LOG(conn, mid, pid, lane, 1).get())
    return log.log_string


async def lt_status(port: GenericAnyPort, lane: int) -> Dict[str, Any]:
    """ Show the link training status.

    :param port: port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :return: 
    :rtype: str
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    page_xindex = 8765
    page_xindex2 = 8766
    serdes_xindex = 3
    *_, status, info, rw, rw1 = await apply(
        commands.PP_LINKTRAINSTATUS(conn, mid, pid, lane).get(),
        commands.PL1_LINKTRAININFO(conn, mid, pid, lane, 0).get(),
        commands.PX_RW(conn, mid, pid, page_xindex, serdes_xindex).get(),
        commands.PX_RW(conn, mid, pid, page_xindex2, serdes_xindex).get(),
    )
    total_bit_count = (info.prbs_total_bits_high << 32) + info.prbs_total_error_bits_low
    total_error_bit_count = (
        (info.prbs_total_error_bits_high & 0x0000FFFF) << 32
    ) + info.prbs_total_error_bits_low
    prbs = total_error_bit_count / total_bit_count if total_bit_count != 0 else 0

    return {
        "preset0": rw1.value,
        "failure": status.failure,
        "loopback": rw.value[3],
        "pbrs": prbs,
        "duration": info.duration_us,
        "lock_lost": info.lock_lost_count,
        "frame_lock": info.frame_lock,
        "remote_frame_lock": info.remote_frame_lock,
        "c(-3)": {
            "current_level": info.pre3_current_level,
            "+reg": {
                "rx": info.pre3_rx_increment_req_count,
                "tx": info.pre3_tx_increment_req_count,
            },
            "-reg": {
                "rx": info.pre3_rx_decrement_req_count,
                "tx": info.pre3_tx_decrement_req_count,
            },
            "coeff_and_eq_limit_reached": {
                "rx": info.pre3_rx_coeff_eq_limit_reached_count,
                "tx": info.pre3_tx_coeff_eq_limit_reached_count,
            },
            "eq_limit_reached": {
                "rx": info.pre3_rx_eq_limit_reached_count,
                "tx": info.pre3_tx_eq_limit_reached_count,
            },
            "coeff_not_supported": {
                "rx": info.pre3_rx_coeff_not_supported_count,
                "tx": info.pre3_tx_coeff_not_supported_count,
            },
            "coeff_at_limit": {
                "rx": info.pre3_rx_coeff_at_limit_count,
                "tx": info.pre3_tx_coeff_at_limit_count,
            },
        },
        "c(-2)": {
            "current_level": info.pre2_current_level,
            "+reg": {
                "rx": info.pre2_rx_increment_req_count,
                "tx": info.pre2_tx_increment_req_count,
            },
            "-reg": {
                "rx": info.pre2_rx_decrement_req_count,
                "tx": info.pre2_tx_decrement_req_count,
            },
            "coeff_and_eq_limit_reached": {
                "rx": info.pre2_rx_coeff_eq_limit_reached_count,
                "tx": info.pre2_tx_coeff_eq_limit_reached_count,
            },
            "eq_limit_reached": {
                "rx": info.pre2_rx_eq_limit_reached_count,
                "tx": info.pre2_tx_eq_limit_reached_count,
            },
            "coeff_not_supported": {
                "rx": info.pre2_rx_coeff_not_supported_count,
                "tx": info.pre2_tx_coeff_not_supported_count,
            },
            "coeff_at_limit": {
                "rx": info.pre2_rx_coeff_at_limit_count,
                "tx": info.pre2_tx_coeff_at_limit_count,
            },
        },
        "c(-1)": {
            "current_level": info.pre1_current_level,
            "+reg": {
                "rx": info.pre1_rx_increment_req_count,
                "tx": info.pre1_tx_increment_req_count,
            },
            "-reg": {
                "rx": info.pre1_rx_decrement_req_count,
                "tx": info.pre1_tx_decrement_req_count,
            },
            "coeff_and_eq_limit_reached": {
                "rx": info.pre1_rx_coeff_eq_limit_reached_count,
                "tx": info.pre1_tx_coeff_eq_limit_reached_count,
            },
            "eq_limit_reached": {
                "rx": info.pre1_rx_eq_limit_reached_count,
                "tx": info.pre1_tx_eq_limit_reached_count,
            },
            "coeff_not_supported": {
                "rx": info.pre1_rx_coeff_not_supported_count,
                "tx": info.pre1_tx_coeff_not_supported_count,
            },
            "coeff_at_limit": {
                "rx": info.pre1_rx_coeff_at_limit_count,
                "tx": info.pre1_tx_coeff_at_limit_count,
            },
        },
        "c(0)": {
            "current_level": info.main_current_level,
            "+reg": {
                "rx": info.main_rx_increment_req_count,
                "tx": info.main_tx_increment_req_count,
            },
            "-reg": {
                "rx": info.main_rx_decrement_req_count,
                "tx": info.main_tx_decrement_req_count,
            },
            "coeff_and_eq_limit_reached": {
                "rx": info.main_rx_coeff_eq_limit_reached_count,
                "tx": info.main_tx_coeff_eq_limit_reached_count,
            },
            "eq_limit_reached": {
                "rx": info.main_rx_eq_limit_reached_count,
                "tx": info.main_tx_eq_limit_reached_count,
            },
            "coeff_not_supported": {
                "rx": info.main_rx_coeff_not_supported_count,
                "tx": info.main_tx_coeff_not_supported_count,
            },
            "coeff_at_limit": {
                "rx": info.main_rx_coeff_at_limit_count,
                "tx": info.main_tx_coeff_at_limit_count,
            },
        },
        "c(1)": {
            "current_level": info.post1_current_level,
            "+reg": {
                "rx": info.post1_rx_increment_req_count,
                "tx": info.post1_tx_increment_req_count,
            },
            "-reg": {
                "rx": info.post1_rx_decrement_req_count,
                "tx": info.post1_tx_decrement_req_count,
            },
            "coeff_and_eq_limit_reached": {
                "rx": info.post1_rx_coeff_eq_limit_reached_count,
                "tx": info.post1_tx_coeff_eq_limit_reached_count,
            },
            "eq_limit_reached": {
                "rx": info.post1_rx_eq_limit_reached_count,
                "tx": info.post1_tx_eq_limit_reached_count,
            },
            "coeff_not_supported": {
                "rx": info.post1_rx_coeff_not_supported_count,
                "tx": info.post1_tx_coeff_not_supported_count,
            },
            "coeff_at_limit": {
                "rx": info.post1_rx_coeff_at_limit_count,
                "tx": info.post1_tx_coeff_at_limit_count,
            },
        },
    }


async def txtap_get(port: GenericAnyPort, lane: int) -> Dict[str, Any]:
    """Get the tap value of the local TX tap.

    :param port: port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :return: 
    :rtype: typing.Dict[str, Any]
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    *_, r = await apply(commands.PP_PHYTXEQ(conn, mid, pid, lane).get())
    return {
        "c(-3)": r.post2,
        "c(-2)": r.pre2,
        "c(-1)": r.pre1,
        "c(0)": r.main,
        "c(1)": r.post1,
    }


async def txtap_set(
    port: GenericAnyPort,
    lane: int,
    pre3: int,
    pre2: int,
    pre1: int,
    main: int,
    post1: int,
) -> List[Token]:
    """Set the tap value of the local TX tap.

    :param port: port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :param pre3: pre3 value 
    :type pre3: int
    :param pre2: pre2 value
    :type pre2: int
    :param pre1: pre1 value
    :type pre1: int
    :param main: main value
    :type main: int
    :param post1: post1 value
    :type post1: int
    :return: 
    :rtype: typing.List[Token]
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    return [
        commands.PP_PHYTXEQ(conn, mid, pid, lane).set(
            pre1=pre1,
            main=main,
            post1=post1,
            pre2=pre2,
            post2=pre3,
            post3=0,
        )
    ]


async def link_recovery(port: GenericAnyPort, enable: bool) -> List[Token]:
    """Should xenaserver automatically do link recovery when detecting down signal.

    :param port: port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param enable: Should xenaserver automatically do link recovery when detecting down signal.
    :type enable: bool
    :return: 
    :rtype: typing.List[Token]
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    page_xindex = 0
    serdes_xindex = 0
    return [
        commands.PL1_CFG_TMP(conn, mid, pid, page_xindex, serdes_xindex).set(enable)
    ]
