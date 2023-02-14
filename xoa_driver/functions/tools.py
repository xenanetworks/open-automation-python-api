from __future__ import annotations

from xoa_driver.ports import GenericAnyPort
from xoa_driver.internals.core import interfaces as itf
from xoa_driver.lli import commands
from xoa_driver import enums


def get_ctx(port: GenericAnyPort) -> tuple["itf.IConnection", int, int]:
    return port._conn, port.kind.module_id, port.kind.port_id


def dictionize_autoneg_status(
    loopback: commands.PL1_CFG_TMP.GetDataAttr,
    auto_neg_info: commands.PL1_AUTONEGINFO.GetDataAttr,
) -> dict:
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


def _link_info_part(
    info: commands.PL1_LINKTRAININFO.GetDataAttr, index: str, part: str
) -> dict:
    tx_attr = f"{index}_tx_{part}"
    rx_attr = f"{index}_rx_{part}"
    return {
        "rx": getattr(info, rx_attr),
        "tx": getattr(info, tx_attr),
    }


def _link_info_all(info: commands.PL1_LINKTRAININFO.GetDataAttr, index: str) -> dict:
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
    status: commands.PP_LINKTRAINSTATUS.GetDataAttr,
    info: commands.PL1_LINKTRAININFO.GetDataAttr,
    ltconf: commands.PP_LINKTRAIN.GetDataAttr,
    cfg: commands.PL1_CFG_TMP.GetDataAttr,
    prbs: float,
    total_bit_count: float,
    total_error_bit_count: float,
) -> dict:
    is_enabled = True if status.mode == enums.LinkTrainingStatusMode.ENABLED else False
    is_traind = True if status.status == enums.LinkTrainingStatus.TRAINED else False
    preset0 = (
        "standard value"
        if ltconf.nrz_preset == enums.NRZPreset.NRZ_NO_PRESET
        else "existing tap value"
    )
    return {
        "is_enabled": is_enabled,
        "is_trained": is_traind,
        "failure": enums.LinkTrainingFailureType(status.failure).name.lower(),
        "preset0": preset0,
        "init_modulation": cfg.values[0],
        "total_bits": total_bit_count,
        "total_errored_bits": total_error_bit_count,
        "ber": prbs,
        "duration": info.duration_us,
        "lock_lost": info.lock_lost_count,
        "frame_lock": enums.LinkTrainFrameLock(info.frame_lock).name.lower(),
        "remote_frame_lock": enums.LinkTrainFrameLock(
            info.remote_frame_lock
        ).name.lower(),
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


def dictionize_txtap_get(r: commands.PP_PHYTXEQ.GetDataAttr) -> dict:
    return {
        "c(-3)": r.post2,
        "c(-2)": r.pre2,
        "c(-1)": r.pre1,
        "c(0)": r.main,
        "c(1)": r.post1,
    }


def dictionize_anlt_status(
    link_recovery: commands.PL1_CFG_TMP.GetDataAttr,
    autoneg: commands.PP_AUTONEGSTATUS.GetDataAttr,
    linktrain: commands.PP_LINKTRAIN.GetDataAttr,
    capabilities: commands.P_CAPABILITIES.GetDataAttr,
) -> dict:
    return {
        "autoneg_enabled": enums.AutoNegMode(autoneg.mode).name.lower().lstrip("aneg_"),
        "link_training_mode": enums.LinkTrainingMode(linktrain.mode).name.lower(),
        "link_training_timeout": enums.TimeoutMode(linktrain.timeout_mode).name.lower(),
        "link_recovery": "on" if link_recovery.values[0] == 1 else "off",
        "serdes_count": capabilities.serdes_count,
    }
