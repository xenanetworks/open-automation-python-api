import asyncio
import platform
from typing import Any, Dict, List, Literal, Optional, Union
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
    tokens = []
    r = await port.reservation.get()
    if r == ReservedStatus.RESERVED_BY_OTHER:
        tokens.append(port.reservation.set_relinquish())
    elif r == ReservedStatus.RELEASED:
        tokens.append(port.reservation.set_reserve())
    return tokens


def port_reset(port: GenericAnyPort) -> List[Token]:
    return [(port.reset.set())]


async def anlt_status(
    port: GenericAnyPort,
) -> Dict[str, Any]:

    # if not isinstance(port, LinkTrainingSupported):
    #     raise NotSupportLinkTrainError(port)
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    r1 = commands.PP_AUTONEG(_connection=conn, _module=mid, _port=pid).get()
    r2 = commands.PP_LINKTRAIN(_connection=port._conn, _module=mid, _port=pid).get()

    tokens = [
        # port.pcs_pma.auto_neg.settings.get(),
        r1,
        # port.pcs_pma.link_training.settings.get(),
        r2,
    ]
    *_, autoneg, linktrain = await apply(*tokens)
    return {
        "auto_neg_enabled": (autoneg.mode),
        "link_train_mode": (linktrain.mode),
        "link_train_timeout": (linktrain.timeout_mode),
    }


def an(
    port: GenericAnyPort,
    loopback: bool,
    enable: bool,
) -> List[Token]:
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    page_xindex = 8765
    register_xindex = 3
    loopback_hexstring = f"0x0000000{int(loopback)}"
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
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    *_, log = await apply(commands.PL1_LOG(conn, mid, pid, 0, 0).get())
    return log.log_string


def lt(
    port: GenericAnyPort,
    enable: bool,
    timeout_enable: bool,
    mode: Literal["auto", "interactive"],
) -> List[Token]:
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    t = (enable, timeout_enable, mode)
    tokens = [
        # lt_nop
    ]
    if t == (True, False, "interactive"):
        tokens += [
            lt_clear(port, 0),
        ]
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


def lt_clear(port: GenericAnyPort, lane: int) -> List[Token]:
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    page_xindex = 8766
    register_xindex = ((0xFFFF & lane) << 16) + 0x0002
    return [
        commands.PX_RW(conn, mid, pid, page_xindex, register_xindex).set("0x00000000")
    ]


def lt_nop(port: GenericAnyPort, lane: int) -> List[Token]:
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    page_xindex = 8766
    register_xindex = ((0xFFFF & lane) << 16) + 0x0000
    return [
        commands.PX_RW(conn, mid, pid, page_xindex, register_xindex).set("0x00010000")
    ]


def lt_coeff_inc(
    port: GenericAnyPort, lane: int, coeff: int, value: int
) -> List[Token]:
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    page_xindex = 8766
    register_xindex = ((0xFFFF & lane) << 16) + 0x0000
    aaaa = hex(value & 0xFFFF).replace("0x", "").zfill(4)
    cc = hex(coeff & 0xFF).replace("0x", "").zfill(2)

    return [
        commands.PX_RW(conn, mid, pid, page_xindex, register_xindex).set(
            f"0x{aaaa}01{cc}"
        )
    ]


def lt_coeff_dec(
    port: GenericAnyPort, lane: int, coeff: int, value: int
) -> List[Token]:
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    page_xindex = 8766
    register_xindex = ((0xFFFF & lane) << 16) + 0x0000
    aaaa = hex(value & 0xFFFF).replace("0x", "").zfill(4)
    cc = hex(coeff & 0xFF).replace("0x", "").zfill(2)

    return [
        commands.PX_RW(conn, mid, pid, page_xindex, register_xindex).set(
            f"0x{aaaa}02{cc}"
        )
    ]


def lt_preset(port: GenericAnyPort, lane: int, preset: int) -> List[Token]:
    assert preset in range(1, 6), "Preset should be an integer between 1 and 5!"
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    page_xindex = 8766
    register_xindex = ((0xFFFF & lane) << 16) + 0x0000
    bb = {1: "0B", 2: "0C", 3: "0D", 4: "0E", 5: "0F"}[preset]
    return [
        commands.PX_RW(conn, mid, pid, page_xindex, register_xindex).set(
            f"0x0001{bb}00"
        )
    ]


def lt_trained(port: GenericAnyPort, lane: int) -> List[Token]:
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    page_xindex = 8766
    register_xindex = ((0xFFFF & lane) << 16) + 0x0000
    return [
        commands.PX_RW(conn, mid, pid, page_xindex, register_xindex).set(f"0x0001FF00")
    ]


async def lt_log(port: GenericAnyPort, lane: int) -> str:
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    *_, log = await apply(commands.PL1_LOG(conn, mid, pid, lane, 1).get())
    return log.log_string


async def lt_status(port: GenericAnyPort, lane: int) -> Dict[str, Any]:
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    page_xindex = 8765
    serdes_xindex = 3
    *_, status, info, rw = await apply(
        commands.PP_LINKTRAINSTATUS(conn, mid, pid, lane).get(),
        commands.PL1_LINKTRAININFO(conn, mid, pid, lane, 0).get(),
        commands.PX_RW(conn, mid, pid, page_xindex, serdes_xindex).get(),
    )
    total_bit_count = (info.prbs_total_bits_high << 32) + info.prbs_total_error_bits_low
    total_error_bit_count = (
        (info.prbs_total_error_bits_high & 0x0000FFFF) << 32
    ) + info.prbs_total_error_bits_low
    prbs = total_error_bit_count / total_bit_count if total_bit_count != 0 else 0

    return {
        "mode": status.mode,
        "status": status.status,
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
                "tx": info.pre3_tx_coeff_at_limit_countt,
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
                "tx": info.pre2_tx_coeff_at_limit_countt,
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
                "tx": info.pre1_tx_coeff_at_limit_countt,
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
                "tx": info.main_tx_coeff_at_limit_countt,
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
                "tx": info.post1_tx_coeff_at_limit_countt,
            },
        },
    }


async def txtap_get(port: GenericAnyPort, lane: int) -> Dict[str, Any]:
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    *_, r = await apply(commands.PP_PHYTXEQ(conn, mid, pid, lane).get())
    return {
        "c(-3)": r.post2,
        "c(-2)": r.pre2,
        "c(-1)": r.pre1,
        "c(0)": r.main,
        "c(1)": r.post1,
    }


def txtap_set(
    port: GenericAnyPort, lane: int, c__3, c__2, c__1, c_0, c_1
) -> List[Token]:
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    return [
        commands.PP_PHYTXEQ(conn, mid, pid, lane).set(
            pre1=c__1, main=c_0, post1=c_1, pre2=c__2, post2=c__3, post3=0, mode=4
        )
    ]
