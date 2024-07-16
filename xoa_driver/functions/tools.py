from __future__ import annotations
from typing import Any

from xoa_driver.ports import GenericAnyPort
from xoa_driver.internals.core import interfaces as itf
from xoa_driver.lli import commands
from xoa_driver import enums


def get_ctx(port: GenericAnyPort) -> tuple["itf.IConnection", int, int]:
    return (port._conn, *port.kind)


def dictionize_autoneg_status(
    loopback: commands.PL1_CFG_TMP.GetDataAttr,
    auto_neg_info: commands.PL1_AUTONEGINFO.GetDataAttr,
    status: commands.PL1_AUTONEG_STATUS.GetDataAttr,
) -> dict[str, Any]:
    _is_enabled = True if status.mode == enums.AutoNegMode.ANEG_ON else False
    _ta_hcd_status = status.tech_ability_hcd_status
    if _ta_hcd_status == enums.FreyaTechAbilityHCDStatus.FAILED:
        _ta_hcd_value = "N/A"
        _fec_result_value = "N/A"
    else:
        _ta_hcd_value = status.tech_ability_hcd_value.name
        _fec_result_value = status.fec_mode_result.name
    return {
        "is_enabled": _is_enabled,
        "loopback": "allowed" if loopback.values[0] else "not allowed",
        "state": status.autoneg_state.name,
        "hcd": _ta_hcd_value,
        "fec_result": _fec_result_value,
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


def _decode_ic(key: int) -> str:
    dic = {
        0: "INDV",
        1: "Preset 4",
        2: "Preset 1",
        3: "Preset 5",
        4: "Preset 2",
        6: "Preset 3",
    }
    return dic.get(key, "Reserved")


def _link_info_part(info: commands.PL1_LINKTRAININFO.GetDataAttr, index: str, part: str) -> dict[str, str]:
    tx_attr = f"{index}_tx_{part}"
    rx_attr = f"{index}_rx_{part}"
    return {
        "rx": getattr(info, rx_attr),
        "tx": getattr(info, tx_attr),
    }


def _link_info_all(info: commands.PL1_LINKTRAININFO.GetDataAttr, index: str) -> dict[str, Any]:
    return {
        "current_level": getattr(info, f"{index}_current_level"),
        "+req": _link_info_part(info, index, "increment_req_count"),
        "-req": _link_info_part(info, index, "decrement_req_count"),
        "coeff_and_eq_limit_reached": _link_info_part(
            info, index, "coeff_eq_limit_reached_count"
        ),
        "eq_limit_reached": _link_info_part(info, index, "eq_limit_reached_count"),
        "coeff_not_supported": _link_info_part(
            info, index, "coeff_not_supported_count"
        ),
        "coeff_at_limit": _link_info_part(info, index, "coeff_at_limit_count"),
    }


def dictionize_lt_status(
    status: commands.PL1_LINKTRAIN_STATUS.GetDataAttr,
    info: commands.PL1_LINKTRAININFO.GetDataAttr,
    ltconf: commands.PL1_LINKTRAIN_CONFIG.GetDataAttr,
    cfg: commands.PL1_CFG_TMP.GetDataAttr,
    ber: float,
    total_bit_count: float,
    total_error_bit_count: float,
) -> dict[str, Any]:
    _is_enabled = True if status.mode == enums.LinkTrainingStatusMode.ENABLED else False
    _is_traind = True if status.status == enums.LinkTrainingStatus.TRAINED else False
    _oos_preset = "Existing" if ltconf.oos_preset == enums.FreyaOutOfSyncPreset.CURRENT else "IEEE"
    ber_str = '{:.2e}'.format(ber)
    return {
        "is_enabled": _is_enabled,
        "is_trained": _is_traind,
        # "failure": enums.LinkTrainingFailureType(status.failure).name.lower(),
        "failure": status.failure.name.lower(),
        "oos_preset": _oos_preset,
        "init_modulation": enums.LinkTrainEncoding(cfg.values[0]).name.lower(),
        "total_bits": total_bit_count,
        "total_errored_bits": total_error_bit_count,
        "ber": ber_str,
        "duration": info.duration_us,
        "lock_lost": info.lock_lost_count,
        # "frame_lock": enums.LinkTrainFrameLock(info.frame_lock).name.lower(),
        "frame_lock": info.frame_lock.name.lower(),
        # "remote_frame_lock": enums.LinkTrainFrameLock(
        #     info.remote_frame_lock
        # ).name.lower(),
        "remote_frame_lock": info.remote_frame_lock.name.lower(),
        "frame_errors": info.num_frame_errors,
        "overrun_errors": info.num_overruns,
        "last_ic_received": _decode_ic(info.last_ic_received),
        "last_ic_sent": _decode_ic(info.last_ic_sent),
        "c(-3)": _link_info_all(info, "pre3"),
        "c(-2)": _link_info_all(info, "pre2"),
        "c(-1)": _link_info_all(info, "pre1"),
        "c(0)": _link_info_all(info, "main"),
        "c(1)": _link_info_all(info, "post1"),
    }


def dictionize_txtap_get(r: commands.PP_PHYTXEQ.GetDataAttr) -> dict[str, int]:
    return {
        "c(-3)": r.pre3_post2,
        "c(-2)": r.pre2,
        "c(-1)": r.pre,
        "c(0)": r.main,
        "c(1)": r.post,
    }


def dictionize_anlt_status(
    link_recovery: commands.PL1_CFG_TMP.GetDataAttr,
    anlt_op: commands.PL1_ANLT.GetDataAttr,
    linktrain_cfg: commands.PL1_LINKTRAIN_CONFIG.GetDataAttr,
    capabilities: commands.P_CAPABILITIES.GetDataAttr,
    allow_loopback: commands.PL1_CFG_TMP.GetDataAttr,
) -> dict[str, Any]:
    return {
        "autoneg_mode": anlt_op.an_mode.name.lower(),
        "link_training_mode": anlt_op.lt_mode.name.lower(),
        "link_training_timeout": "enable" if linktrain_cfg.timeout_mode == enums.TimeoutMode.DEFAULT else "disable",
        "restart_link_down": "on" if link_recovery.values[0] == 1 or link_recovery.values[0] == 3 else "off",
        "restart_lt_fail": "on" if link_recovery.values[0] == 2 or link_recovery.values[0] == 3 else "off",
        "serdes_count": capabilities.serdes_count,
        "autoneg_allow_loopback": allow_loopback.values,
        "link_training_preset0": enums.FreyaOutOfSyncPreset(linktrain_cfg.oos_preset).name.lower(),
    }


def dictionize_lt_im_status(
    capabilities: commands.P_CAPABILITIES.GetDataAttr,
    initial_mods: dict[str, str]
) -> dict[str, Any]:
    return {
        "serdes_count": capabilities.serdes_count,
        "initial_mods": initial_mods,
    }


def dictionize_lt_algorithm_status(
    capabilities: commands.P_CAPABILITIES.GetDataAttr,
    algorithms: dict[str, str]
) -> dict[str, Any]:
    return {
        "serdes_count": capabilities.serdes_count,
        "algorithms": algorithms
    }


MODULE_EOL_INFO: dict[str, str] = {
    "01": "2014-04-01",
    "02": "2024-09-01",
    "03": "2016-03-01",
    "09": "2022-01-01",
    "17": "2023-01-01",
    "18": "2023-01-01",
    "20": "2024-11-01",
    "22": "2018-11-01",
    "24": "2024-11-01",
    "26": "2023-06-01",
    "27": "2025-10-01",
    "30": "2024-01-01",
    "31": "2021-09-01",
    "32": "2024-04-01",
    "34": "2024-08-01",
    "36": "2024-04-01",
    "40": "2023-03-01",
    "50": "2022-02-01",
    "51": "2023-08-01",
    "54": "2023-01-01",
    "55": "2024-01-01",
    "60": "2025-10-01",
    "66": "2025-01-31",
    "90": "2025-10-01",
    "91": "2025-10-01",
    "93": "2025-10-01",
    "94": "2025-10-01",
    "97": "2025-10-01",
}

def dictionize_anlt_log_ctrl_status(
    logctrl_status: list[int]
) -> dict[str, bool]:
    _value = logctrl_status[0]
    _debug = bool(_value & enums.AnLtLogControl.LOG_TYPE_DEBUG)
    _an_trace = bool(_value & enums.AnLtLogControl.LOG_TYPE_AN_TRACE)
    _lt_trace = bool(_value & enums.AnLtLogControl.LOG_TYPE_LT_TRACE)
    _alg_trace = bool(_value & enums.AnLtLogControl.LOG_TYPE_ALG_TRACE)
    _fsm_port = bool(_value & enums.AnLtLogControl.LOG_TYPE_FSM_PORT)
    _fsm_an = bool(_value & enums.AnLtLogControl.LOG_TYPE_FSM_ANEG)
    _fsm_an_stimuli = bool(_value & enums.AnLtLogControl.LOG_TYPE_FSM_ANEG_STIMULI)
    _fsm_lt = bool(_value & enums.AnLtLogControl.LOG_TYPE_FSM_LT)
    _fsm_lt_coeff = bool(_value & enums.AnLtLogControl.LOG_TYPE_FSM_LT_COEFF)
    _fsm_lt_stimuli = bool(_value & enums.AnLtLogControl.LOG_TYPE_FSM_LT_STIMULI)
    _fsm_lt_alg0 = bool(_value & enums.AnLtLogControl.LOG_TYPE_FSM_LT_ALG0)
    _fsm_lt_algn1 = bool(_value & enums.AnLtLogControl.LOG_TYPE_FSM_LT_ALG1)
    return {
        "debug": _debug,
        "an_trace": _an_trace,
        "lt_trace": _lt_trace,
        "alg_trace": _alg_trace,
        "fsm_port": _fsm_port,
        "fsm_an": _fsm_an,
        "fsm_an_stimuli": _fsm_an_stimuli,
        "fsm_an_stimuli": _fsm_an_stimuli,
        "fsm_lt": _fsm_lt,
        "fsm_lt_coeff": _fsm_lt_coeff,
        "fsm_lt_stimuli": _fsm_lt_stimuli,
        "fsm_lt_alg0": _fsm_lt_alg0,
        "fsm_lt_algn1": _fsm_lt_algn1,
    }