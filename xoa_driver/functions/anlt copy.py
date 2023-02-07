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
)
from xoa_driver.utils import apply
from xoa_driver.internals.hli_v1.ports.port_l23.family_l import FamilyL
from xoa_driver.internals.hli_v1.ports.port_l23.family_l1 import FamilyL1
from xoa_driver.ports import GenericAnyPort
from xoa_driver.lli import commands


PcsPmaSupported = (FamilyL, FamilyL1)
AutoNegSupported = (FamilyL, FamilyL1)
LinkTrainingSupported = FamilyL


def _pp_autoneg(group, on: bool):
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
):
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


def _pl1_cfg_tmp(group, lane: int, config_type: Layer1ConfigType, values: int):
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
    if should_do_lt:
        # Disable autoneg
        tokens += _pp_autoneg(group, False)
        for lane_str, im in lt_initial_modulations.items():
            tokens += _pl1_cfg_tmp(
                group,
                int(lane_str),
                Layer1ConfigType.LT_INITIAL_MODULATION,
                int(im),
            )
        tokens += _pp_link_train(
            group, LinkTrainingMode.DISABLED, nrz_preset, TimeoutMode.DEFAULT
        )
        if should_do_an:
            timeout_mode = TimeoutMode.DEFAULT
            lt_mode = LinkTrainingMode.START_AFTER_AUTONEG
        else:
            timeout_mode = TimeoutMode.DISABLED
            if should_lt_interactive:
                lt_mode = LinkTrainingMode.INTERACTIVE
            else:
                lt_mode = LinkTrainingMode.STANDALONE
        tokens += _pp_link_train(group, lt_mode, nrz_preset, timeout_mode)

    if should_do_an:
        tokens += _pl1_cfg_tmp(
            group,
            0,
            Layer1ConfigType.AN_LOOPBACK,
            int(an_allow_loopback),
        )
        tokens += _pp_autoneg(group, True)

    await apply(*tokens)
