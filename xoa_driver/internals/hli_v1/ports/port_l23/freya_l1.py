from typing import (
    TYPE_CHECKING,
    Tuple,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    PP_PRECODING,
    PP_PRECODINGSTATUS,
    PP_GRAYCODING,
    PL1_AUTONEGINFO,
    PL1_LINKTRAININFO,
    PL1_LOG,
    PL1_CFG_TMP,
    PL1_LINKTRAIN_CMD,
    PL1_CTRL,
    PL1_GET_DATA,
    PL1_PHYTXEQ_LEVEL,
    PL1_PHYTXEQ_COEFF,
    PL1_AUTONEG_STATUS,
    PL1_AUTONEG_ABILITIES,
    PL1_PCS_VARIANT,
    PL1_AUTONEG_CONFIG,
    PL1_ANLT,
    PL1_PHYTXEQ,
    PL1_LINKTRAIN_CONFIG,
    PL1_LINKTRAIN_STATUS,
    PP_PHYRXEQ_EXT,
    PP_PHYRXEQSTATUS_EXT,
    PL1_CWE_CYCLE,
    PL1_CWE_ERR_SYM_INDICES,
    PL1_CWE_BIT_ERR_MASK,
    PL1_CWE_FEC_ENGINE,
    PL1_CWE_FEC_STATS,
    PL1_CWE_CONTROL,
    PL1_CWE_FEC_STATS_CLEAR,
)
from .pcs_pma_ghijkl import (
    Prbs,
)
from xoa_driver import enums

class FreyaPMA:
    """Freya PMA"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.precoding = PP_PRECODING(conn, module_id, port_id, serdes_xindex)
        """GET/SET Pre-Coding Configurations. (only for Freya)

        :type: PP_PRECODING
        """

        self.graycoding = PP_GRAYCODING(conn, module_id, port_id, serdes_xindex)
        """GET/SET Gray-Coding Configurations. (only for Freya)

        :type: PP_GRAYCODING
        """

class FreyaSIV:
    """Freya Signal Integrity View"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.control = PL1_CTRL(conn, module_id, port_id, serdes_xindex, enums.Layer1Control.SAMPLED_SIGNAL_INTEGRITY_SCAN)
        """Control SIV scan. (only for Freya)

        :type: PL1_CTRL
        """

        self.data = PL1_GET_DATA(conn, module_id, port_id, serdes_xindex, enums.Layer1Control.SAMPLED_SIGNAL_INTEGRITY_SCAN)
        """Get SIV scan data. (only for Freya)

        :type: PL1_GET_DATA
        """

class FreyaTxTap:
    """Freya Tx Tap"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.native = PL1_PHYTXEQ(conn, module_id, port_id, serdes_xindex)
        """TX tap native value. (only for Freya)

        :type: PL1_PHYTXEQ
        """

        self.level = PL1_PHYTXEQ_LEVEL(conn, module_id, port_id, serdes_xindex)
        """TX tap mV/dB value. (only for Freya)

        :type: PL1_PHYTXEQ_LEVEL
        """

        self.ieee = PL1_PHYTXEQ_COEFF(conn, module_id, port_id, serdes_xindex)
        """TX tap IEEE coefficient value. (only for Freya)

        :type: PL1_PHYTXEQ_COEFF
        """

class FreyaRxTapConfig:
    """Freya Rx Tap Configuration"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.ctle_low = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.CTLE_LOW)
        """RX tap CTLE LOW. (only for Freya)
        """

        self.ctle_high = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.CTLE_HIGH)
        """RX tap CTLE HIGH. (only for Freya)
        """

        self.agc = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.AGC)
        """RX tap Automatic Gain Control. (only for Freya)
        """

        self.oc = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.OC)
        """RX tap Offset Cancellation. (only for Freya)
        """

        self.cdr = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.CDR)
        """RX tap Clock and Data Recovery. (only for Freya)
        """

        self.pre_ffe_1 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_1)
        """RX tap Pre Feed-Forward Equalizer #1. (only for Freya)
        """

        self.pre_ffe_2 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_2)
        """RX tap Pre Feed-Forward Equalizer #2. (only for Freya)
        """

        self.pre_ffe_3 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_3)
        """RX tap Pre Feed-Forward Equalizer #3. (only for Freya)
        """

        self.pre_ffe_4 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_4)
        """RX tap Pre Feed-Forward Equalizer #4. (only for Freya)
        """

        self.pre_ffe_5 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_5)
        """RX tap Pre Feed-Forward Equalizer #5. (only for Freya)
        """

        self.pre_ffe_6 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_6)
        """RX tap Pre Feed-Forward Equalizer #6. (only for Freya)
        """

        self.pre_ffe_7 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_7)
        """RX tap Pre Feed-Forward Equalizer #7. (only for Freya)
        """

        self.pre_ffe_8 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_8)
        """RX tap Pre Feed-Forward Equalizer #8. (only for Freya)
        """

        self.dfe = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.DFE)
        """RX tap Decision Feedback Equalization. (only for Freya)
        """

        self.post_ffe_1 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_1)
        """RX tap Post Feed-Forward Equalizer #1. (only for Freya)
        """

        self.post_ffe_2 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_2)
        """RX tap Post Feed-Forward Equalizer #2. (only for Freya)
        """

        self.post_ffe_3 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_3)
        """RX tap Post Feed-Forward Equalizer #3. (only for Freya)
        """

        self.post_ffe_4 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_4)
        """RX tap Post Feed-Forward Equalizer #4. (only for Freya)
        """

        self.post_ffe_5 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_5)
        """RX tap Post Feed-Forward Equalizer #5. (only for Freya)
        """

        self.post_ffe_6 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_6)
        """RX tap Post Feed-Forward Equalizer #6. (only for Freya)
        """

        self.post_ffe_7 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_7)
        """RX tap Post Feed-Forward Equalizer #7. (only for Freya)
        """

        self.post_ffe_8 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_8)
        """RX tap Post Feed-Forward Equalizer #8. (only for Freya)
        """

        self.post_ffe_9 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_9)
        """RX tap Post Feed-Forward Equalizer #9. (only for Freya)
        """

        self.post_ffe_10 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_10)
        """RX tap Post Feed-Forward Equalizer #10. (only for Freya)
        """

        self.post_ffe_11 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_11)
        """RX tap Post Feed-Forward Equalizer #11. (only for Freya)
        """

        self.post_ffe_12 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_12)
        """RX tap Post Feed-Forward Equalizer #12. (only for Freya)
        """

        self.post_ffe_13 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_13)
        """RX tap Post Feed-Forward Equalizer #13. (only for Freya)
        """

        self.post_ffe_14 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_14)
        """RX tap Post Feed-Forward Equalizer #14. (only for Freya)
        """

        self.post_ffe_15 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_15)
        """RX tap Post Feed-Forward Equalizer #15. (only for Freya)
        """

        self.post_ffe_16 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_16)
        """RX tap Post Feed-Forward Equalizer #16. (only for Freya)
        """

        self.post_ffe_17 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_17)
        """RX tap Post Feed-Forward Equalizer #17. (only for Freya)
        """

        self.post_ffe_18 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_18)
        """RX tap Post Feed-Forward Equalizer #18. (only for Freya)
        """

        self.post_ffe_19 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_19)
        """RX tap Post Feed-Forward Equalizer #19. (only for Freya)
        """

        self.post_ffe_20 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_20)
        """RX tap Post Feed-Forward Equalizer #20. (only for Freya)
        """

        self.post_ffe_21 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_21)
        """RX tap Post Feed-Forward Equalizer #21. (only for Freya)
        """

        self.post_ffe_22 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_22)
        """RX tap Post Feed-Forward Equalizer #22. (only for Freya)
        """

        self.post_ffe_23 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_13)
        """RX tap Post Feed-Forward Equalizer #23. (only for Freya)
        """

class FreyaRxTapStatus:
    """Freya Rx Tap Status"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.ctle_low = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.CTLE_LOW)
        """RX tap CTLE LOW. (only for Freya)
        """

        self.ctle_high = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.CTLE_HIGH)
        """RX tap CTLE HIGH. (only for Freya)
        """

        self.agc = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.AGC)
        """RX tap Automatic Gain Control. (only for Freya)
        """

        self.oc = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.OC)
        """RX tap Offset Cancellation. (only for Freya)
        """

        self.cdr = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.CDR)
        """RX tap Clock and Data Recovery. (only for Freya)
        """

        self.pre_ffe_1 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_1)
        """RX tap Pre Feed-Forward Equalizer #1. (only for Freya)
        """

        self.pre_ffe_2 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_2)
        """RX tap Pre Feed-Forward Equalizer #2. (only for Freya)
        """

        self.pre_ffe_3 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_3)
        """RX tap Pre Feed-Forward Equalizer #3. (only for Freya)
        """

        self.pre_ffe_4 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_4)
        """RX tap Pre Feed-Forward Equalizer #4. (only for Freya)
        """

        self.pre_ffe_5 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_5)
        """RX tap Pre Feed-Forward Equalizer #5. (only for Freya)
        """

        self.pre_ffe_6 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_6)
        """RX tap Pre Feed-Forward Equalizer #6. (only for Freya)
        """

        self.pre_ffe_7 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_7)
        """RX tap Pre Feed-Forward Equalizer #7. (only for Freya)
        """

        self.pre_ffe_8 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_8)
        """RX tap Pre Feed-Forward Equalizer #8. (only for Freya)
        """

        self.dfe = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.DFE)
        """RX tap Decision Feedback Equalization. (only for Freya)
        """

        self.post_ffe_1 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_1)
        """RX tap Post Feed-Forward Equalizer #1. (only for Freya)
        """

        self.post_ffe_2 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_2)
        """RX tap Post Feed-Forward Equalizer #2. (only for Freya)
        """

        self.post_ffe_3 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_3)
        """RX tap Post Feed-Forward Equalizer #3. (only for Freya)
        """

        self.post_ffe_4 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_4)
        """RX tap Post Feed-Forward Equalizer #4. (only for Freya)
        """

        self.post_ffe_5 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_5)
        """RX tap Post Feed-Forward Equalizer #5. (only for Freya)
        """

        self.post_ffe_6 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_6)
        """RX tap Post Feed-Forward Equalizer #6. (only for Freya)
        """

        self.post_ffe_7 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_7)
        """RX tap Post Feed-Forward Equalizer #7. (only for Freya)
        """

        self.post_ffe_8 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_8)
        """RX tap Post Feed-Forward Equalizer #8. (only for Freya)
        """

        self.post_ffe_9 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_9)
        """RX tap Post Feed-Forward Equalizer #9. (only for Freya)
        """

        self.post_ffe_10 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_10)
        """RX tap Post Feed-Forward Equalizer #10. (only for Freya)
        """

        self.post_ffe_11 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_11)
        """RX tap Post Feed-Forward Equalizer #11. (only for Freya)
        """

        self.post_ffe_12 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_12)
        """RX tap Post Feed-Forward Equalizer #12. (only for Freya)
        """

        self.post_ffe_13 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_13)
        """RX tap Post Feed-Forward Equalizer #13. (only for Freya)
        """

        self.post_ffe_14 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_14)
        """RX tap Post Feed-Forward Equalizer #14. (only for Freya)
        """

        self.post_ffe_15 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_15)
        """RX tap Post Feed-Forward Equalizer #15. (only for Freya)
        """

        self.post_ffe_16 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_16)
        """RX tap Post Feed-Forward Equalizer #16. (only for Freya)
        """

        self.post_ffe_17 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_17)
        """RX tap Post Feed-Forward Equalizer #17. (only for Freya)
        """

        self.post_ffe_18 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_18)
        """RX tap Post Feed-Forward Equalizer #18. (only for Freya)
        """

        self.post_ffe_19 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_19)
        """RX tap Post Feed-Forward Equalizer #19. (only for Freya)
        """

        self.post_ffe_20 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_20)
        """RX tap Post Feed-Forward Equalizer #20. (only for Freya)
        """

        self.post_ffe_21 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_21)
        """RX tap Post Feed-Forward Equalizer #21. (only for Freya)
        """

        self.post_ffe_22 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_22)
        """RX tap Post Feed-Forward Equalizer #22. (only for Freya)
        """

        self.post_ffe_23 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_13)
        """RX tap Post Feed-Forward Equalizer #23. (only for Freya)
        """

class FreyaRxTap:
    """Freya Rx tap
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.config = FreyaRxTapConfig(conn, module_id, port_id, serdes_xindex)
        """Freya Rx tap configuration
        """
        self.status = FreyaRxTapStatus(conn, module_id, port_id, serdes_xindex)
        """Freya Rx tap status
        """

class FreyaMedium:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.tx = FreyaTxTap(conn, module_id, port_id, serdes_xindex)
        """Freya Tx tap
        """
        self.rx = FreyaRxTap(conn, module_id, port_id, serdes_xindex)
        """Freya Rx tap
        """
        self.siv = FreyaSIV(conn, module_id, port_id, serdes_xindex)
        """Freya Signal Integrity
        """

class SerDesFreya:
    """L23 high-speed port SerDes configuration and status."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:

        self.prbs = Prbs(conn, module_id, port_id, serdes_xindex)
        """PRBS
        :type: Prbs
        """
        
        self.pma = FreyaPMA(conn, module_id, port_id, serdes_xindex)
        """Freya PMA

        :type: FreyaPMA
        """

        self.medium = FreyaMedium(conn, module_id, port_id, serdes_xindex)
        """Freya medium

        :type: FreyaMedium
        """

        self.lt_cmd = PL1_LINKTRAIN_CMD(conn, module_id, port_id, serdes_xindex)
        """Link training command.
        
        :type: PP_LINKTRAIN
        """

        self.lt_info = PL1_LINKTRAININFO(conn, module_id, port_id, serdes_xindex, 0)
        """Link training info.
        
        :type: PL1_LINKTRAININFO
        """

        self.lt_status = PL1_LINKTRAIN_STATUS(conn, module_id, port_id, serdes_xindex)
        """Link training status.
        
        :type: PL1_LINKTRAIN_STATUS
        """

class FreyaAutoNeg:
    """Freya Autoneg"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.info = PL1_AUTONEGINFO(conn, module_id, port_id, 0)
        """Autoneg info

        :type: PL1_AUTONEGINFO
        """

        self.status = PL1_AUTONEG_STATUS(conn, module_id, port_id)
        """Autoneg status

        :type: PL1_AUTONEG_STATUS
        """

        self.abilities = PL1_AUTONEG_ABILITIES(conn, module_id, port_id)
        """Autoneg abilities

        :type: PL1_AUTONEG_ABILITIES
        """

        self.config = PL1_AUTONEG_CONFIG(conn, module_id, port_id)
        """Autoneg configuration

        :type: PL1_AUTONEG_CONFIG
        """

class FreyaANLT:
    """Freya port-level anlt. For per-serdes configuration and status, use serdes[x]
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.an = FreyaAutoNeg(conn, module_id, port_id)
        """Autoneg config and status
        """
        self.ctrl = PL1_ANLT(conn, module_id, port_id)
        """ANLT control
        """
        self.lt_config = PL1_LINKTRAIN_CONFIG(conn, module_id, port_id)
        """Port-level Link Training config
        """
        self.log = PL1_LOG(conn, module_id, port_id)
        """ANLT log
        """

class FreyaFecCodewordErrorInject:
    """Freya FEC Codeword Error Injection
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.cycle = PL1_CWE_CYCLE(conn, module_id, port_id)
        """FEC codeword error injection cycle.
        """
        self.err_symbols = PL1_CWE_ERR_SYM_INDICES(conn, module_id, port_id)
        """The positions of the errored symbols in errored codewords.
        """
        self.bit_err_mask = PL1_CWE_BIT_ERR_MASK(conn, module_id, port_id)
        """The bit error mask for the errored symbols.
        """
        self.engine = PL1_CWE_FEC_ENGINE(conn, module_id, port_id)
        """The FEC engines to use.
        """
        self.statistics = PL1_CWE_FEC_STATS(conn, module_id, port_id)
        """FEC error injection statistics
        """
        self.clear_stats = PL1_CWE_FEC_STATS_CLEAR(conn, module_id, port_id)
        """Clear FEC codeword injection stats
        """
        self.control = PL1_CWE_CONTROL(conn, module_id, port_id)
        """Control the FEC codeword error injection
        """

class Layer1:
    def __init__(self, conn: "itf.IConnection", port) -> None:
        self.serdes: Tuple[SerDesFreya, ...] = tuple(
                SerDesFreya(conn, *port.kind, serdes_xindex=idx)
                for idx in range(port.info.capabilities.serdes_count)
                )
        self.anlt = FreyaANLT(conn, *port.kind)
        """Freya port-level anlt. For per-serdes configuration and status, use serdes[x]
        """
        self.pcs_variant = PL1_PCS_VARIANT(conn, *port.kind)
        """PCS variant configuration
        """
        self.fec_error_inject = FreyaFecCodewordErrorInject(conn, *port.kind)
        """FEC codeword error injection
        """
        

