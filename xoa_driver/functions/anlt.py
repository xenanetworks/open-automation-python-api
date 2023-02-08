from __future__ import annotations

from typing import Any, Dict
from xoa_driver.enums import (
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
    LinkTrainEncoding,
    LinkTrainCoeffs,
    LinkTrainPresets,
    Layer1ConfigType,
    Layer1LogType,
    LinkTrainingStatusMode,
    LinkTrainingStatus,
    AutoNegMode,
    LinkTrainingFailureType,
    LinkTrainFrameLock,
)
from xoa_driver.utils import apply
from xoa_driver.internals.hli_v1.ports.port_l23.family_l import FamilyL
from xoa_driver.internals.hli_v1.ports.port_l23.family_l1 import FamilyL1
from xoa_driver.ports import GenericAnyPort
from xoa_driver.lli import commands
from xoa_driver.internals.core import interfaces as itf
from xoa_driver.misc import Token

PcsPmaSupported = (FamilyL, FamilyL1)
AutoNegSupported = (FamilyL, FamilyL1)
LinkTrainingSupported = FamilyL


def _pp_autoneg(group: tuple["itf.IConnection", int, int], on: bool) -> list[Token]:
    conn, mid, pid = group
    state = AutoNegMode.ANEG_ON if on else AutoNegMode.ANEG_OFF
    return [
        commands.PP_AUTONEG(conn, mid, pid).set(
            state,
            AutoNegTecAbility.DEFAULT_TECH_MODE,
            AutoNegFECOption.NO_FEC,
            AutoNegFECOption.NO_FEC,
            PauseMode.NO_PAUSE,
        ),
    ]


def _pp_link_train(
    group, mode: LinkTrainingMode, nrz_preset: NRZPreset, timeout_mode: TimeoutMode
) -> list[Token]:
    conn, mid, pid = group
    return [
        commands.PP_LINKTRAIN(conn, mid, pid).set(
            mode=mode,
            pam4_frame_size=PAM4FrameSize.P16K_FRAME,
            nrz_pam4_init_cond=LinkTrainingInitCondition.NO_INIT,
            nrz_preset=nrz_preset,
            timeout_mode=timeout_mode,
        )
    ]


def _pl1_cfg_tmp(
    group, lane: int, config_type: Layer1ConfigType, values: int
) -> list[Token]:
    conn, mid, pid = group
    return [
        commands.PL1_CFG_TMP(conn, mid, pid, lane, config_type).set(
            values=[int(values)]
        )
    ]


async def do_anlt(
    port: GenericAnyPort,
    should_do_an: bool,
    should_do_lt: bool,
    an_allow_loopback: bool,
    lt_preset0_std: bool,
    lt_initial_modulations: Dict[str, LinkTrainEncoding],
    should_lt_interactive: bool,
) -> None:
    """_summary_

    :param port: port to select
    :type port: GenericAnyPort
    :param should_do_an: should the port do autoneg?
    :type should_do_an: bool
    :param should_do_lt: should the port do link training?
    :type should_do_lt: bool
    :param an_allow_loopback: should the autoneg allow loopback?
    :type an_allow_loopback: bool
    :param lt_preset0_std: should lt preset0 uses the standard values or the existing tap values?
    :type lt_preset0_std: bool
    :param lt_initial_modulations: the initial modulations of each lane (serdes)
    :type lt_initial_modulations: Dict[str, LinkTrainEncoding]
    :param should_lt_interactive: should perform link training manually?
    :type should_lt_interactive: bool
    """

    group = port._conn, port.kind.module_id, port.kind.port_id
    nrz_preset = (
        NRZPreset.NRZ_WITH_PRESET if lt_preset0_std else NRZPreset.NRZ_NO_PRESET
    )
    # # Set autoneg timeout
    tokens = _pp_link_train(
        group, LinkTrainingMode.DISABLED, NRZPreset.NRZ_NO_PRESET, TimeoutMode.DEFAULT
    )

    # # Set autoneg allow-loopback
    tokens += _pl1_cfg_tmp(
        group, 0, Layer1ConfigType.AN_LOOPBACK, int(an_allow_loopback)
    )

    dis_an = (not should_do_an) or should_do_lt
    if dis_an:
        # Disable autoneg
        tokens += _pp_autoneg(group, False)

    if should_do_lt:
        for lane_str, im in lt_initial_modulations.items():
            tokens += _pl1_cfg_tmp(
                group,
                int(lane_str),
                Layer1ConfigType.LT_INITIAL_MODULATION,
                int(im),
            )

        if should_do_an:
            timeout_mode = TimeoutMode.DEFAULT
            lt_mode = LinkTrainingMode.START_AFTER_AUTONEG
        elif should_lt_interactive:
            lt_mode = LinkTrainingMode.INTERACTIVE
            timeout_mode = TimeoutMode.DEFAULT
        else:
            lt_mode = LinkTrainingMode.STANDALONE
            timeout_mode = TimeoutMode.DISABLED
        tokens += _pp_link_train(group, LinkTrainingMode.DISABLED, nrz_preset, timeout_mode)
        tokens += _pp_link_train(group, lt_mode, nrz_preset, timeout_mode)

    if should_do_an:
        tokens += _pp_autoneg(group, True)

    await apply(*tokens)


async def autoneg_status(port: GenericAnyPort) -> Dict[str, Any]:
    """Get the auto-negotiation status

    :param port: the port to get auto-negotiation status
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :return:
    :rtype: typing.Dict[str, Any]
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    *_, loopback, auto_neg_info = await apply(
        commands.PL1_CFG_TMP(conn, mid, pid, 0, Layer1ConfigType.AN_LOOPBACK).get(),
        commands.PL1_AUTONEGINFO(conn, mid, pid, 0).get(),
    )
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


async def lt_coeff_inc(port: GenericAnyPort, lane: int, emphasis: LinkTrainCoeffs) -> None:
    """Ask the remote port to increase coeff of the specified lane.

    :param port: the port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :param emphasis: coefficient index (pre1, pre2, pre3, main, post)
    :type emphasis: str
    :return:
    :rtype: None
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    await commands.PL1_LINKTRAIN_CMD(conn, mid, pid, lane).set(
        cmd=LinkTrainCmd.CMD_INC, arg=emphasis.value
    )
    return None


async def lt_coeff_dec(port: GenericAnyPort, lane: int, emphasis: LinkTrainCoeffs) -> None:
    """Ask the remote port to decrease coeff of the specified lane.

    :param port: the port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :param emphasis: coefficient index (pre1, pre2, pre3, main, post)
    :type emphasis: str
    :return:
    :rtype: None
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    await commands.PL1_LINKTRAIN_CMD(conn, mid, pid, lane).set(
        cmd=LinkTrainCmd.CMD_INC, arg=emphasis.value
    )
    return None


async def lt_preset(port: GenericAnyPort, lane: int, preset: LinkTrainPresets) -> None:
    """Ask the remote port to use the preset of the specified lane.

    :param port: port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :param preset: preset index to select for the lane, 0,1,2,3,4,
    :type preset: int
    :return:
    :rtype: None
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    await commands.PL1_LINKTRAIN_CMD(conn, mid, pid, lane).set(
        cmd=LinkTrainCmd.CMD_PRESET, arg=preset.value
    )
    return None


async def lt_encoding(port: GenericAnyPort, lane: int, encoding: LinkTrainEncoding) -> None:
    """Ask the remote port to use the encoding of the specified lane.

    :param port: port to configure
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param lane: lane index, starting from 0
    :type lane: int
    :param encoding: link training encoding (nrz, pam4, pam4pre)
    :type encoding: str
    :return:
    :rtype: None
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    await commands.PL1_LINKTRAIN_CMD(conn, mid, pid, lane).set(
        cmd=LinkTrainCmd.CMD_ENCODING, arg=encoding.value
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
        commands.PL1_LINKTRAIN_CMD(conn, mid, pid, lane).set(
            cmd=LinkTrainCmd.CMD_LOCAL_TRAINED, arg=0
        )
    )
    return None


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

    def decode_ic(key: int) -> str:
        dic = {
            0: "INDV",
            1: "Preset 4",
            2: "Preset 1",
            3: "Preset 5",
            4: "Preset 2",
            6: "Preset 3",
        }
        return dic.get(key, "Reserved")

    *_, status, info, ltconf, cfg = await apply(
        commands.PP_LINKTRAINSTATUS(conn, mid, pid, lane).get(),
        commands.PL1_LINKTRAININFO(conn, mid, pid, lane, 0).get(),
        commands.PP_LINKTRAIN(conn, mid, pid).get(),
        commands.PL1_CFG_TMP(
            conn, mid, pid, lane, Layer1ConfigType.LT_INITIAL_MODULATION
        ).get(),
    )
    total_bit_count = (info.prbs_total_bits_high << 32) + (
        info.prbs_total_error_bits_low
    )
    total_error_bit_count = (info.prbs_total_error_bits_high << 32) + (
        info.prbs_total_error_bits_low
    )
    prbs = (
        total_error_bit_count / total_bit_count if total_bit_count > 0 else float("nan")
    )

    return {
        "is_enabled": True if status.mode == LinkTrainingStatusMode.ENABLED else False,
        "is_trained": True if status.status == LinkTrainingStatus.TRAINED else False,
        "failure": LinkTrainingFailureType(status.failure).name.lower(),
        "preset0": "standard value"
        if ltconf.nrz_preset == NRZPreset.NRZ_NO_PRESET
        else "existing tap value",
        "init_modulation": cfg.value[0],
        "ber": str(prbs),
        "duration": f"{info.duration_us} us",
        "lock_lost": info.lock_lost_count,
        "frame_lock": LinkTrainFrameLock(info.frame_lock).name.lower(),
        "remote_frame_lock": LinkTrainFrameLock(info.remote_frame_lock).name.lower(),
        "frame_errors": info.num_frame_errors,
        "overrun_errors": info.num_overruns,
        "last_ic_received": decode_ic(info.last_ic_received),
        "last_ic_sent": decode_ic(info.last_ic_sent),
        "c(-3)": {
            "current_level": info.pre3_current_level,
            "+req": {
                "rx": info.pre3_rx_increment_req_count,
                "tx": info.pre3_tx_increment_req_count,
            },
            "-req": {
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
            "+req": {
                "rx": info.pre2_rx_increment_req_count,
                "tx": info.pre2_tx_increment_req_count,
            },
            "-req": {
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
    await commands.PL1_CFG_TMP(
        conn, mid, pid, 0, Layer1ConfigType.ANLT_INTERACTIVE
    ).set(values=[int(enable)])
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
    tokens = [
        commands.PL1_CFG_TMP(
            conn, mid, pid, 0, Layer1ConfigType.ANLT_INTERACTIVE
        ).get(),
        commands.PP_AUTONEGSTATUS(conn, mid, pid).get(),
        commands.PP_LINKTRAIN(conn, mid, pid).get(),
        commands.P_CAPABILITIES(conn, mid, pid).get(),
    ]
    *_, link_recovery, autoneg, linktrain, capabilities = await apply(*tokens)
    return {
        "autoneg_enabled": AutoNegMode(autoneg.mode).name.lower().lstrip("aneg_"),
        "link_training_mode": LinkTrainingMode(linktrain.mode).name.lower(),
        "link_training_timeout": TimeoutMode(linktrain.timeout_mode).name.lower(),
        "link_recovery": "on" if link_recovery.values[0] == 1 else "off",
        "serdes_count": capabilities.serdes_count,
    }


# WIP
async def anlt_log(port: GenericAnyPort) -> str:
    """Get the anlt log messages

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :return: anlt log
    :rtype: str
    """
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    *_, log = await apply(commands.PL1_LOG(conn, mid, pid).get())
    return log.log_string