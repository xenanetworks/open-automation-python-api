from __future__ import annotations

from typing import Any, Dict, List
from xoa_driver.enums import (
    ReservedStatus,
    AutoNegFECOption,
    AutoNegMode,
    AutoNegTecAbility,
    PauseMode,
    NRZPreset,
    PAM4FrameSize,
    TimeoutMode,
    LinkTrainingInitCondition,
    LinkTrainingMode,
    LinkTrainCmd,
    LinkTrainCmdFlags,
    LinkTrainCmdResults,
    LinkTrainEncoding,
    LinkTrainCoeffs,
    LinkTrainFrameLock,
    LinkTrainPresets,
    Layer1ConfigType,
    Layer1LogType,
    LinkTrainingStatusMode,
    LinkTrainingStatus,
    AutoNegMode
)
from xoa_driver.misc import Token
from xoa_driver.utils import apply
from xoa_driver.internals.hli_v1.ports.port_l23.family_l import FamilyL
from xoa_driver.internals.hli_v1.ports.port_l23.family_l1 import FamilyL1
from xoa_driver.ports import GenericAnyPort
from xoa_driver.testers import L23Tester, L47Tester, GenericAnyTester
from xoa_driver.lli import commands
from xoa_driver.enums import SyncStatus
from .exceptions import NotConnectedError, NoSuchModuleError, NoSuchPortError

from decimal import *

PcsPmaSupported = (FamilyL, FamilyL1)
AutoNegSupported = (FamilyL, FamilyL1)
LinkTrainingSupported = FamilyL


async def autoneg_config(
    port: GenericAnyPort,
    enable: bool,
    loopback: bool
    ) -> None:
    """Configure auto-negotiation

    :param port: the port to configure AN
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param enable: enable or disable autonegotiation
    :type enable: bool
    :param loopback: allow or deny loopback
    :type loopback: bool
    :return:
    :rtype: None
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    autoneg_enabled = AutoNegMode(enable)

    c1 = commands.PL1_CFG_TMP(conn, mid, pid, 0, Layer1ConfigType.AN_ALLOW_LOOPBACK).set(values=[int(loopback)])

    c2 = commands.PP_AUTONEG(conn, mid, pid).set(
        autoneg_enabled,
        AutoNegTecAbility.DEFAULT_TECH_MODE,
        AutoNegFECOption.NO_FEC,
        AutoNegFECOption.NO_FEC,
        PauseMode.NO_PAUSE,
    )
    tokens = [c1, c2]
    await apply(*tokens)
    return None



async def autoneg_status(port: GenericAnyPort) -> Dict[str, Any]:
    """Get the auto-negotiation status

    :param port: the port to get auto-negotiation status
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :return:
    :rtype: typing.Dict[str, Any]
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    *_, loopback = await apply(commands.PL1_CFG_TMP(conn, mid, pid, 0, Layer1ConfigType.AN_ALLOW_LOOPBACK).get())
    *_, auto_neg_info = await apply(commands.PL1_AUTONEGINFO(conn, mid, pid, 0).get())
    return {
        "loopback": "allowed" if loopback.values[0] else "not allowed",
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
        "unformatted_pages": {
            "tx": auto_neg_info.tx_next_page_unformatted_count,
            "rx": auto_neg_info.rx_next_page_unformatted_count,
        },
    }


async def autoneg_log(port: GenericAnyPort) -> str:
    """Get the auto-negotiation log messages

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
    port: GenericAnyPort,
    mode: str,
    preset0: bool,
    timeout: bool
    ) -> None:
    """Configure link training on a port.

    :param port: the port to configure LT on
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param mode: the mode of link training. 
    "autocomplete"=to set the port to start link training without performing auto-negotiation. "autostart"=to set the port to start link training automatically after auto-negotiation. Requires auto-negotiation is enabled.
    "interactive"=to set the port to manually perform link training procedure.
    "disable"=to set the port to stop link training.
    :type mode: str
    :param preset0: should the preset0 (out-of-sync) use existing tap values (true) or standard values (false)
    :type preset0: bool
    :param timeout: should LT run with or without timeout
    :type timeout: bool
    :return:
    :rtype: None
    """
    assert mode in (
        "autocomplete",
        "disable",
        "autostart",
        "interactive",
    ), "Para 'mode' not in ('autocomplete', 'disable', 'autostart', 'interactive')!"
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    t = (mode, preset0, timeout)
    tokens = []
    if t == ('autocomplete', True, True):
        md, ps, tm = (LinkTrainingMode.STANDALONE, NRZPreset.NRZ_WITH_PRESET, TimeoutMode.DEFAULT)
    elif t == ('autocomplete', True, False):
        md, ps, tm = (LinkTrainingMode.STANDALONE, NRZPreset.NRZ_WITH_PRESET, TimeoutMode.DISABLED)
    elif t == ('autocomplete', False, True):
        md, ps, tm = (LinkTrainingMode.STANDALONE, NRZPreset.NRZ_NO_PRESET, TimeoutMode.DEFAULT)
    elif t == ('autocomplete', False, False):
        md, ps, tm = (LinkTrainingMode.STANDALONE, NRZPreset.NRZ_NO_PRESET, TimeoutMode.DISABLED)

    elif t == ('disable', True, True):
        md, ps, tm = (LinkTrainingMode.DISABLE, NRZPreset.NRZ_WITH_PRESET, TimeoutMode.DEFAULT)
    elif t == ('disable', True, False):
        md, ps, tm = (LinkTrainingMode.DISABLE, NRZPreset.NRZ_WITH_PRESET, TimeoutMode.DISABLED)
    elif t == ('disable', False, True):
        md, ps, tm = (LinkTrainingMode.DISABLE, NRZPreset.NRZ_NO_PRESET, TimeoutMode.DEFAULT)
    elif t == ('disable', False, False):
        md, ps, tm = (LinkTrainingMode.DISABLE, NRZPreset.NRZ_NO_PRESET, TimeoutMode.DISABLED)

    elif t == ('interactive', True, True):
        md, ps, tm = (LinkTrainingMode.INTERACTIVE, NRZPreset.NRZ_WITH_PRESET, TimeoutMode.DEFAULT)
    elif t == ('interactive', True, False):
        md, ps, tm = (LinkTrainingMode.INTERACTIVE, NRZPreset.NRZ_WITH_PRESET, TimeoutMode.DISABLED)
    elif t == ('interactive', False, True):
        md, ps, tm = (LinkTrainingMode.INTERACTIVE, NRZPreset.NRZ_NO_PRESET, TimeoutMode.DEFAULT)
    elif t == ('interactive', False, False):
        md, ps, tm = (LinkTrainingMode.INTERACTIVE, NRZPreset.NRZ_NO_PRESET, TimeoutMode.DISABLED)

    elif t == ('autostart', True, True):
        md, ps, tm = (LinkTrainingMode.START_AFTER_AUTONEG, NRZPreset.NRZ_WITH_PRESET, TimeoutMode.DEFAULT)
    elif t == ('autostart', True, False):
        md, ps, tm = (LinkTrainingMode.START_AFTER_AUTONEG, NRZPreset.NRZ_WITH_PRESET, TimeoutMode.DISABLED)
    elif t == ('autostart', False, True):
        md, ps, tm = (LinkTrainingMode.START_AFTER_AUTONEG, NRZPreset.NRZ_NO_PRESET, TimeoutMode.DEFAULT)
    else:
        md, ps, tm = (LinkTrainingMode.START_AFTER_AUTONEG, NRZPreset.NRZ_NO_PRESET, TimeoutMode.DISABLED)

    tokens += [
        commands.PP_LINKTRAIN(conn, mid, pid).set(
            mode=LinkTrainingMode.DISABLE,
            pam4_frame_size=PAM4FrameSize.P16K_FRAME,
            nrz_pam4_init_cond=LinkTrainingInitCondition.NO_INIT,
            nrz_preset=ps,
            timeout_mode=tm,
        ),
        commands.PP_LINKTRAIN(conn, mid, pid).set(
            mode=md,
            pam4_frame_size=PAM4FrameSize.P16K_FRAME,
            nrz_pam4_init_cond=LinkTrainingInitCondition.NO_INIT,
            nrz_preset=ps,
            timeout_mode=tm,
        ),
    ]
    await apply(*tokens)
    return None


async def lt_coeff_inc(port: GenericAnyPort, lane: int, emphasis: str) -> None:
    """Ask the remote port to increase coeff of the specified lane.

    :param port: the port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :param emphasis: coefficient index (-3, -2, -1, 0, 1)
    :type emphasis: str
    :return:
    :rtype: None
    """
    assert emphasis.lower() in ("pre3", "pre2", "pre", "main", "post"), "Para 'emphasis' not in (pre3, pre2, pre, main, post, PRE3, PRE2, PRE, MAIN, POST)!"
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    
    await apply(
        commands.PL1_LINKTRAIN_CMD(conn, mid, pid, lane).set(cmd=LinkTrainCmd.CMD_INC, arg=LinkTrainCoeffs.from_str(emphasis))
        )
    return None


async def lt_coeff_dec(port: GenericAnyPort, lane: int, emphasis: str) -> None:
    """Ask the remote port to decrease coeff of the specified lane.

    :param port: the port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :param coeff: coefficient index (-3, -2, -1, 0, 1)
    :type coeff: int
    :param value: the decrease value
    :type count: int
    :return:
    :rtype: None
    """
    assert emphasis.lower() in ("pre3", "pre2", "pre", "main", "post"), "Para 'emphasis' not in (pre3, pre2, pre, main, post, PRE3, PRE2, PRE, MAIN, POST)!"
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    
    await apply(
        commands.PL1_LINKTRAIN_CMD(conn, mid, pid, lane).set(cmd=LinkTrainCmd.CMD_INC, arg=LinkTrainCoeffs.from_str(emphasis))
        )
    return None


async def lt_preset(port: GenericAnyPort, lane: int, preset: int) -> None:
    """Ask the remote port to use the preset of the specified lane.

    :param port: port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :param preset: preset index to select for the lane, 1,2,3,4,5
    :type preset: int
    :return:
    :rtype: None
    """
    assert preset in range(1, 5), "Para 'preset' not in (1, 2, 3, 4, 5)!"
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    await apply(
        commands.PL1_LINKTRAIN_CMD(conn, mid, pid, lane).set(cmd=LinkTrainCmd.CMD_PRESET, arg=LinkTrainPresets.from_str(str(preset)))
        )
    return None



async def lt_encoding(port: GenericAnyPort, lane: int, encoding: str) -> None:
    """Ask the remote port to use the encoding of the specified lane.

    :param port: port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :param encoding: link training encoding (nrz/pam2, pam4, pam4pre)
    :type encoding: str
    :return:
    :rtype: None
    """
    assert encoding in ("nrz", "pam2", "pam4", "pam4pre"), "Para 'encoding' not in (nrz, pam2, pam4, pam4pre)!"
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    await apply(
        commands.PL1_LINKTRAIN_CMD(conn, mid, pid, lane).set(cmd=LinkTrainCmd.CMD_ENCODING, arg=LinkTrainEncoding.from_str(str(encoding)))
        )
    return None


async def lt_im(port: GenericAnyPort, lane: int, encoding: str) -> None:
    """To set the initial modulation for the lane.

    :param port: port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :param encoding: link training encoding (nrz/pam2, pam4, pam4pre)
    :type encoding: str
    :return:
    :rtype: None
    """
    assert encoding in ("nrz", "pam2", "pam4", "pam4pre"), "Para 'encoding' not in (nrz, pam2, pam4, pam4pre)!"
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    await apply(
        commands.PL1_CFG_TMP(conn, mid, pid, lane, Layer1ConfigType.LT_INITIAL_MODULATION).set(values=[LinkTrainEncoding.from_str(str(encoding))])
        )
    return None


async def lt_trained(port: GenericAnyPort, lane: int) -> None:
    """Tell the remote port that the current lane is trained.

    :param port: port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :return:
    :rtype: None
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    await apply(
        commands.PL1_LINKTRAIN_CMD(conn, mid, pid, lane).set(cmd=LinkTrainCmd.CMD_LOCAL_TRAINED, arg=0)
        )
    return None


async def lt_log(port: GenericAnyPort, lane: int, live: bool) -> str:
    """Show the link training trace log.

    :param port: port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :param live: should show the live LT log
    :type lane: bool
    :return:
    :rtype: str
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    if not live:
        *_, log = await apply(commands.PL1_LOG(conn, mid, pid, lane, Layer1LogType.LT).get())
        return log.log_string
    else:
        return "TBD"


async def lt_status(port: GenericAnyPort, lane: int) -> Dict[str, Any]:
    """Show the link training status.

    :param port: port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :return:
    :rtype: str
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    
    def decode_ic(value: int) -> str:
        dict = {
            "INDV": 0,
            "Preset 4": 1,
            "Preset 1": 2,
            "Preset 5": 3,
            "Preset 2": 4,
            "Preset 3": 5,
            }
        if value in dict.values():
            position = list(dict.values()).index(value)
            return list(dict.keys())[position]
        else:
            return "Reserved"
    
    *_, status, info, ltconf, cfg= await apply(
        commands.PP_LINKTRAINSTATUS(conn, mid, pid, lane).get(),
        commands.PL1_LINKTRAININFO(conn, mid, pid, lane, 0).get(),
        commands.PP_LINKTRAIN(conn, mid, pid).get(),
        commands.PL1_CFG_TMP(conn, mid, pid, lane, Layer1ConfigType.LT_INITIAL_MODULATION).get()
    )
    getcontext().prec = 8
    total_bit_count = Decimal(info.prbs_total_bits_high << 32) + Decimal(info.prbs_total_error_bits_low)
    total_error_bit_count = Decimal(info.prbs_total_error_bits_high << 32) + Decimal(info.prbs_total_error_bits_low)
    prbs = total_error_bit_count / total_bit_count if total_bit_count > 0 else Decimal('NaN')

    return {
        "is_enabled": True if status.mode==LinkTrainingStatusMode.ENABLED else False,
        "is_trained": True if status.status==LinkTrainingStatus.TRAINED else False,
        "failure": status.failure.name.lower(),
        "preset0": "standard" if ltconf.nrz_preset==NRZPreset.NRZ_NO_PRESET else "existing tap value", 
        "init_modulation": cfg.value[0],
        "prbs_ber": str(prbs),
        "duration": f"{info.duration_us} us",
        "lock_lost": info.lock_lost_count,
        "frame_lock": info.frame_lock.name.lower(),
        "remote_frame_lock": info.remote_frame_lock.name.lower(),
        "frame_errors": info.num_frame_errors,
        "overrun_errors": info.num_overruns,
        "last_ic_received": decode_ic(info.last_ic_received),
        "last_ic_sent": decode_ic(info.last_ic_sent),
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
) -> None:
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
    :rtype: None
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    await commands.PP_PHYTXEQ(conn, mid, pid, lane).set(
        pre1=pre1,
        main=main,
        post1=post1,
        pre2=pre2,
        post2=pre3,
        post3=0,
    )
    return None


async def link_recovery(port: GenericAnyPort, enable: bool) -> None:
    """Should xenaserver automatically do link recovery when detecting down signal.

    :param port: port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param enable: Should xenaserver automatically do link recovery when detecting down signal.
    :type enable: bool
    :return:
    :rtype:  None
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    await commands.PL1_CFG_TMP(conn, mid, pid, 0, Layer1ConfigType.ANLT_INTERACTIVE_MODE).set(values=[int(enable)])
    return None


async def status(
    port: GenericAnyPort,
    ) -> Dict[str, Any]:
    """Get the overview of ANLT status

    :param port: the port to get ANLT status from
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :return: ANLT overview status
    :rtype: typing.Dict[str, Any]
    """

    # if not isinstance(port, LinkTrainingSupported):
    #     raise NotSupportLinkTrainError(port)
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    r0 = commands.PL1_CFG_TMP(conn, mid, pid, 0, Layer1ConfigType.ANLT_INTERACTIVE_MODE).get()
    r1 = commands.PP_AUTONEGSTATUS(conn, mid, pid).get()
    r2 = commands.PP_LINKTRAIN(conn, mid, pid).get()

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
        "autoneg_enabled": autoneg.mode.name.lower(),
        "link_training_mode": linktrain.mode.name.lower(),
        "link_training_timeout": linktrain.timeout_mode.name.lower(),
        "link_recovery": "on" if link_recovery.values[0]==1 else "off"
    }
