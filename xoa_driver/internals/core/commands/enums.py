from enum import IntEnum
class ReservedStatus(IntEnum):
    RELEASED = 0
    RESERVED_BY_YOU = 1
    RESERVED_BY_OTHER = 2


class ReservedAction(IntEnum):
    RELEASE = 0
    RESERVE = 1
    RELINQUISH = 2


class ChassisShutdownAction(IntEnum):
    RESTART = 1
    POWEROFF = 2


class OnOff(IntEnum):
    OFF = 0
    ON = 1


class RESTControlAction(IntEnum):
    START = 0
    STOP = 1
    RESTART = 2


class ServiceStatus(IntEnum):
    SERVICE_OFF = 0
    SERVICE_ON = 1


class ChassisSessionType(IntEnum):
    MANAGER = 1
    SCRIPT = 2


class TimeSyncMode(IntEnum):
    CHASSIS = 0
    EXTERNAL = 1
    MODULE = 2


class CFPState(IntEnum):
    NOTCFP = 0
    NOTPRESENT = 1
    NOTFLEXIBLE = 2
    FLEXIBLE = 3


class CFPType(IntEnum):
    CFP_UNKNOWN = 0
    CFP_INVALID = 1
    CFP_1X40_SR4 = 2
    CFP_2X40_SR4 = 3
    CFP_1X40_LR4 = 4
    CFP_1X100_LR4 = 5
    CFP_1X100_SR10 = 6
    CFP_4X10_SFPP = 7
    QSFP_EMPTY = 8
    QSFP_UNKNOWN = 9
    QSFP_SR = 10
    QSFP_LR = 11
    QSFP_ER = 12
    CXP_UNKNOWN = 13
    CXP_SR10 = 14
    CXP_AOC = 15
    CFP4_UNKNOWN = 16
    CFP4_1X100_LR4 = 17
    CFP4_1X100_ER4 = 18
    CFP4_1X100_SR4 = 19
    QSFP28_CR4 = 20
    QSFP28_SR4 = 21
    QSFP28_LR4 = 22
    QSFP28_ER4 = 23
    QSFP28_AOC = 24
    QSFP28_ACC = 25
    QSFP28_UNKNOWN = 26
    QSFP28P_SR4 = 27
    QSFP28P_LR4 = 28
    QSFP28P_ER4 = 29
    QSFP28P_CR4 = 30
    QSFP28P_ISM4 = 31
    QSFP28P_UNKNOWN = 32
    TCVR_UNKNOWN = 33
    QSFP28_CWDM4 = 34
    QSFP28_CWDM4FEC = 35
    QSFP28_PSM4 = 36


class SMAInputFunction(IntEnum):
    NOTUSED = 0
    TX2MHZ = 1
    TX10MHZ = 2


class SMAOutputFunction(IntEnum):
    DISABLED = 0
    PASSTHROUGH = 1
    P0SOF = 2
    P1SOF = 3
    REF2MHZ = 4
    REF10MHZ = 5
    REF125MHZ = 6
    REF156MHZ = 7
    P0RXCLK = 8
    P1RXCLK = 9
    P0RXCLK2MHZ = 10
    P1RXCLK2MHZ = 11
    TS_PPS = 12


class SMAStatus(IntEnum):
    OK = 0
    NO_VALID_SIGNAL = 1


class HasDemo(IntEnum):
    NON_DEMO = 0
    DEMO = 1


class IsValid(IntEnum):
    INVALID = 0
    VALID = 1


class IsPermanent(IntEnum):
    NON_PERMANENT = 0
    PERMANENT = 1


class YesNo(IntEnum):
    NO = 0
    YES = 1


class UpdateState(IntEnum):
    NONE = 0
    UPDATING = 1
    UPDATE_SUCCESS = 2
    UPDATE_FAIL = 3


class IsOnline(IntEnum):
    OFFLINE = 0
    ONLINE = 1


class PortSpeedMode(IntEnum):
    AUTO = 0
    F10M = 1
    F100M = 2
    F1G = 3
    F10G = 4
    F40G = 5
    F100G = 6
    F10MHDX = 7
    F100MHDX = 8
    F10M100M = 9
    F100M1G = 10
    F100M1G10G = 11
    F2500M = 12
    F5G = 13
    F100M1G2500M = 14
    F25G = 15
    F50G = 16
    F200G = 17
    F400G = 18
    F800G = 19
    F1600G = 20

    UNKNOWN = 255


class SyncStatus(IntEnum):
    NO_SYNC = 0
    IN_SYNC = 1


class LoopMode(IntEnum):
    NONE = 0
    L1RX2TX = 1
    L2RX2TX = 2
    L3RX2TX = 3
    TXON2RX = 4
    TXOFF2RX = 5
    PORT2PORT = 6


class TrafficOnOff(IntEnum):
    OFF = 0
    ON = 1
    PREPARING = 2


class StartOrStop(IntEnum):
    STOP = 0
    START = 1


class LatencyMode(IntEnum):
    LAST2LAST = 0
    FIRST2LAST = 1
    LAST2FIRST = 2
    FIRST2FIRST = 3


class SourceType(IntEnum):
    TXIFG = 0
    TXLEN = 1
    RXIFG = 2
    RXLEN = 3
    RXLAT = 4
    RXJIT = 5


class PacketDetailSelection(IntEnum):
    ALL = 0
    TPLD = 1
    FILTER = 2


class OnOffWithSuppress(IntEnum):
    OFF = 0
    ON = 1
    SUPPRESS = 2


class ProtocolOption(IntEnum):
    ETHERNET = 1
    VLAN = 2
    ARP = 3
    IP = 4
    IPV6 = 5
    UDP = 6
    TCP = 7
    LLC = 8
    SNAP = 9
    GTP = 10
    ICMP = 11
    RTP = 12
    RTCP = 13
    STP = 14
    SCTP = 15
    MACCTRL = 16
    MPLS = 17
    PBBTAG = 18
    FCOE = 19
    FC = 20
    FCOETAIL = 21
    IGMPV3L0 = 22
    IGMPV3L1 = 23
    UDPCHECK = 24
    IGMPV2 = 25
    MPLS_TP_OAM = 26
    GRE_NOCHECK = 27
    GRE_CHECK = 28
    TCPCHECK = 29
    GTPV1L0 = 30
    GTPV1L1 = 31
    GTPV2L0 = 32
    GTPV2L1 = 33
    IGMPV1 = 34
    PWETHCTRL = 35
    VXLAN = 36
    ETHERNET_8023 = 37
    NVGRE = 38
    DHCPV4 = 39
    GENEVE = 40
    XENA_TPLD = 41
    XENA_TPLD_PI = 42
    XENA_MICROTPLD = 43
    ETHERNET_FCS = 44
    MACCTRLPFC = 45
    ECPRI = 46
    ROE = 47
    ETHERTYPE = 48
    
    # Generat RAW form 1...64 bytes
    _ignore_ = 'ProtocolOption i'
    ProtocolOption = vars()
    for i in range(1, 65):
        ProtocolOption['RAW_%d' % i] = 256 - i # type: ignore

class ModifierAction(IntEnum):
    INC = 0
    DEC = 1
    RANDOM = 2


class LengthType(IntEnum):
    FIXED = 0
    INCREMENTING = 1
    BUTTERFLY = 2
    RANDOM = 3
    MIX = 4


class PayloadType(IntEnum):
    PATTERN = 0
    INCREMENTING = 1
    PRBS = 2
    RANDOM = 3


class MDIXMode(IntEnum):
    AUTO = 0
    MDI = 1
    MDIX = 2


class LengthCheckType(IntEnum):
    AT_MOST = 0
    AT_LEAST = 1


class StartTrigger(IntEnum):
    ON = 0
    FCSERR = 1
    FILTER = 2
    PLDERR = 3


class StopTrigger(IntEnum):
    FULL = 0
    FCSERR = 1
    FILTER = 2
    PLDERR = 3
    USERSTOP = 4


class PacketType(IntEnum):
    ALL = 0
    FCSERR = 1
    NOTPLD = 2
    TPLD = 3
    FILTER = 4
    PLDERR = 5


class InjectErrorType(IntEnum):
    HEADERERROR = 1
    ALIGNERROR = 2
    BIP8ERROR = 3


class HeaderLockStatus(IntEnum):
    HEADEROFF = 0
    HEADERON = 1
    HEADEROFFUNSTABLE = 2
    HEADERONUNSTABLE = 3


class AlignLockStatus(IntEnum):
    ALIGNOFF = 0
    ALIGNON = 1
    ALIGNUNSTABLE = 3


class PRBSLockStatus(IntEnum):
    PRBSOFF = 0
    PRBSON = 1
    PRBSOFFUNSTABLE = 2
    PRBSONUNSTABLE = 3


class MulticastOperation(IntEnum):
    OFF = 0
    ON = 1
    JOIN = 2
    LEAVE = 3


class MulticastExtOperation(IntEnum):
    OFF = 0
    ON = 1
    JOIN = 2
    LEAVE = 3
    INCLUDE = 4
    EXCLUDE = 5
    LEAVE_TO_ALL = 6
    GENERAL_QUERY = 7
    GROUP_QUERY = 8


class IGMPVersion(IntEnum):
    IGMPV2 = 0
    IGMPV3 = 1


class LoopbackMode(IntEnum):
    NORMAL = 0
    STRICTUNIFORM = 1
    SEQUENTIAL = 2
    BURST = 3


class PayloadMode(IntEnum):
    NORMAL = 0
    EXTPL = 1
    CDF = 2


class BRRMode(IntEnum):
    SLAVE = 0
    MASTER = 1


class TXClock(IntEnum):
    MODULELOCALCLOCK = 0
    SMAINPUT = 1
    P0RXCLK = 2
    P1RXCLK = 3
    P2RXCLK = 4
    P3RXCLK = 5
    P4RXCLK = 6
    P5RXCLK = 7
    P6RXCLK = 8
    P7RXCLK = 9


class TXClockStatus(IntEnum):
    OK = 0
    NOVALIDTXCLK = 1


class FilterBandwidth(IntEnum):
    BW103HZ = 1
    BW207HZ = 2
    BW416HZ = 3
    BW1683HZ = 4
    BW7019HZ = 5


class MediaType(IntEnum):
    CFP4 = 0
    QSFP28 = 1
    CXP = 2
    SFP28 = 3
    QSFP56 = 4
    QSFP_DD = 5
    SFP56 = 6
    SFP_DD = 7
    QSFP_DD_NRZ = 9
    QSFP28_PAM4 = 10
    CFP = 99
    BASE_T1 = 100
    BASE_T1S = 101


class TXHState(IntEnum):
    TXH_NA = 0
    TXH_X = 1


class RXHState(IntEnum):
    RXH_NA = 0
    RXH_X = 1


class TXCState(IntEnum):
    TXC_ACTIVE = 0
    TXC_LPI = 1


class RXCState(IntEnum):
    RXC_ACTIVE = 0
    RXC_LPI = 1


class LinkState(IntEnum):
    LINK_DOWN = 0
    LINK_UP = 1


class FaultSignaling(IntEnum):
    NORMAL = 0
    FORCE_LOCAL = 1
    FORCE_REMOTE = 2
    DISABLED = 3


class LocalFaultStatus(IntEnum):
    OK = 0
    LOCAL_FAULT = 1


class RemoteFaultStatus(IntEnum):
    OK = 0
    REMOTE_FAULT = 1


class TPLDMode(IntEnum):
    NORMAL = 0
    MICRO = 1


class SerdesStatus(IntEnum):
    STOPPED = 0
    STARTED = 1
    INITIALIZING = 2
    PLOTTING = 3


class FECMode(IntEnum):
    OFF = 0
    ON = 1
    RS_FEC = 2
    FC_FEC = 3
    RS_FEC_KR = 4
    RS_FEC_KP = 5


class PRBSInsertedType(IntEnum):
    CAUI_VIRTUAL = 0
    PHY_LINE = 1
    PHY_HOST = 2
    TCVR = 3


class PRBSPolynomial(IntEnum):
    PRBS7 = 0
    PRBS9 = 1
    PRBS11 = 2
    PRBS15 = 3
    PRBS23 = 4
    PRBS31 = 5
    PRBS58 = 6
    PRBS49 = 7
    PRBS10 = 8
    PRBS20 = 9
    PRBS13 = 10


class PRBSInvertState(IntEnum):
    NON_INVERTED = 0
    INVERTED = 1


class PRBSStatisticsMode(IntEnum):
    ACCUMULATIVE = 0
    PERSECOND = 1


class AutoNegMode(IntEnum):
    ANEG_OFF = 0
    ANEG_ON = 1


class AutoNegTecAbility(IntEnum):
    DEFAULT_TECH_MODE = 0
    IEEE_10G_KR = 4
    IEEE_40G_CR4 = 16
    IEEE_100G_KR4 = 128
    IEEE_100G_CR4 = 256
    IEEE_25GBASE_CRS_KRS = 512
    IEEE_25GBASE_CR_KR = 1024
    IEEE_50GBASE_CR_KR = 8192
    IEEE_100GBASE_CR2_KR2 = 16384
    IEEE_200GBASE_CR4_KR4 = 32768
    EC_25GBASE_KR1 = 16777216
    EC_25GBASE_CR1 = 33554432
    EC_50GBASE_KR2 = 67108864
    EC_50GBASE_CR2 = 134217728
    EC_400GGBASE_KR8 = 268435456
    EC_50G_CR1_KR1 = 503
    BAM_50G_CR1_KR1 = 504
    BAM_50G_CR2_KR2 = 505
    BAM_100G_CR2_KR2 = 1002
    BAM_100G_CR4_KR4 = 1003
    BAM_200G_CR2_KR2 = 2002
    BAM_400G_CR8_KR8 = 4001


class AutoNegFecOption(IntEnum):
    DEFAULT_FEC = 0
    NO_FEC = 1
    FCFEC = 2
    RSFEC_CL91 = 4
    RS528 = 256
    RS544 = 512
    RS272 = 1024


class PauseMode(IntEnum):
    NO_PAUSE = 0
    SYM_PAUSE = 1
    ASYM_PAUSE = 2


class AutoNegFECType(IntEnum):
    PENDING = 0
    NOFEC = 1
    RS_FEC = 513
    FC_FEC = 257


class AutoNegStatus(IntEnum):
    UNKNOWN = 0
    ENABLE = 1
    TRANSMIT_DISABLE = 2
    ABILITY_DETECT = 3
    ACKNOWLEDGE_DETECT = 4
    COMPLETE_ACKNOWLEDGE = 5
    NEXT_PAGE_WAIT = 6
    AN_GOOD_CHECK = 7
    AN_GOOD = 8


class AutoNegStatusFEC(IntEnum):
    DEFAULT_FEC = 0
    NO_FEC = 1
    FC_FEC = 2
    RSFEC_CL91 = 4
    RS528 = 256
    RS544 = 512
    RS272 = 1024


class LinkTrainMode(IntEnum):
    AUTO = 0
    FORCE_ENABLE = 1


class PAM4FrameSize(IntEnum):
    N16K_FRAME = 0
    N4K_FRAME = 1


class LinkTrainingInitCondition(IntEnum):
    NO_INIT = 0
    INIT_ENABLED = 1


class NRZPreset(IntEnum):
    NRZ_NO_PRESET = 0
    NRZ_WITH_PRESET = 1


class TimeoutMode(IntEnum):
    DEFAULT_TIMEOUT = 0
    TIMEOUT_DISABLED = 255


class LinkTrainingMode(IntEnum):
    DISABLED = 0
    ENABLED = 1


class LinkTrainStatus(IntEnum):
    NOT_TRAINED = 0
    TRAINED = 1


class LinkTrainFailureType(IntEnum):
    NO_FAILURE = 0
    FRAME_LOCK_ERROR = 1
    SNR_BELOW_THRESHOLD = 2
    TIME_OUT_FAILURE = 3


class Role(IntEnum):
    CLIENT = 0
    SERVER = 1


class Timescale(IntEnum):
    MSECS = 0
    SECONDS = 1
    MINUTES = 2
    HOURS = 3


class MssType(IntEnum):
    FIXED = 0
    INCREMENT = 1
    RANDOM = 2


class RtoType(IntEnum):
    STATIC = 0
    DYNAMIC = 1


class CongestionType(IntEnum):
    NONE = 0
    RENO = 1
    NEW_RENO = 2


class IsEnabled(IntEnum):
    DISABLE = 0
    ENABLE = 1


class AlgorithmMethod(IntEnum):
    RFC5681 = 0
    RFC2581 = 1
    FIXED_FACTOR = 2


class AutoOrManual(IntEnum):
    AUTOMATIC = 0
    MANUAL = 1


class EmbedIP(IntEnum):
    DONT_EMBED_IP = 0
    EMBED_IP = 1


class ApplicationLayerBehavior(IntEnum):
    NONE = 0
    RAW = 1
    REPLAY = 2


class TrafficScenario(IntEnum):
    DOWNLOAD = 0
    UPLOAD = 1
    BOTH = 2
    ECHO = 3


class PayloadGenerationMethod(IntEnum):
    FIXED = 0
    INCREMENT = 1
    RANDOM = 2
    LONGRANDOM = 3


class InfiniteOrFinite(IntEnum):
    INFINITE = 0
    FINITE = 1


class WhoClose(IntEnum):
    NONE = 0
    CLIENT = 1
    SERVER = 2


class LifecycleMode(IntEnum):
    ONCE = 0
    IMMORTAL = 1
    REINCARNATE = 2


class IPVersion(IntEnum):
    IPV4 = 4
    IPV6 = 6


class ProtocolType(IntEnum):
    TCP = 0
    UDP = 1


class TrafficState(IntEnum):
    OFF = 0
    ON = 1
    STOP = 2
    PREPARE = 3
    PRERUN = 4


class PortState(IntEnum):
    OFF = 0
    PREPARE = 1
    PREPARE_RDY = 2
    PREPARE_FAIL = 3
    PRERUN = 4
    PRERUN_RDY = 5
    RUNNING = 6
    STOPPING = 7
    STOPPED = 8


class PortSpeed(IntEnum):
    AUTO = 0
    F100M = 1
    F1G = 2
    F2_5G = 3
    F5G = 4
    F10G = 5
    F25G = 6
    F40G = 7
    F50G = 8
    F100G = 9


class CaptureSize(IntEnum):
    FULL = 0
    SMALL = 1


class ReplayParserState(IntEnum):
    OFF = 0
    PARSING = 1


class IsPresent(IntEnum):
    NOT_PRESENT = 0
    PRESENT = 1


class LicenseSpeed(IntEnum):
    UNDEFINED = 0
    F1G = 1
    F2_5G = 2
    F5G = 3
    F10G = 4
    F25G = 5
    F40G = 6
    F50G = 7
    F100G = 8


class TLSVersion(IntEnum):
    SSLV3 = 0
    TLS10 = 1
    TLS11 = 2
    TLS12 = 3


class HeaderFormat(IntEnum):
    NOHDR = 0
    VLAN = 1


# class Infinite(IntEnum):
#     INFINITE = 0


class CorruptionType(IntEnum):
    OFF = 0
    ETH = 1
    IP = 2
    UDP = 3
    TCP = 4
    BER = 5


class PolicerMode(IntEnum):
    L1 = 0
    L2 = 1


class EthernetInfo(IntEnum):
    OFF = 0
    AND = 1


class Clude(IntEnum):
    EXCLUDE = 0
    INCLUDE = 1


class L2PlusPresent(IntEnum):
    NA = 0
    VLAN1 = 1
    VLAN2 = 2
    MPLS = 3


class L3PlusPresent(IntEnum):
    NA = 0
    IP4 = 1
    IP6 = 2


class Flow(IntEnum):
    BASIC = 0
    EXTENDED = 1


class TimeKeeperLicenseFileState(IntEnum):
    NA = 0
    INV = 1
    VALID = 2


class TimeKeeperLicenseType(IntEnum):
    UNDEF = 0
    CLIENT = 1
    SERVER = 2


class TimeKeeperLicenseError(IntEnum):
    NO_LICENSE_ERROR = 0
    INVALID_SERIALNO = 1
    INVALID_CHASSISTYPE = 2


class SystemUpdateStatus(IntEnum):
    OK = 0
    FAILED_SCRIPT = 1
    FAILED_PREP = 10
    FAILED_FILENAME = 11
    FAILED_DECRYPT = 12
    FAILED_UNPACK = 13
    FAILED_VERIFY = 14
    FAILED_MOVE = 15


class TimeKeeperServiceStatus(IntEnum):
    STOPPED = 0
    STARTED = 1
    NA = 2


class TimeKeeperServiceAction(IntEnum):
    STOP = 0
    START = 1
    RESTART = 2


class CustomeDefaultCommand(IntEnum):
    SET = 0
    CLEAR = 1


class CustomeDefaultScope(IntEnum):
    ALL = 0
    INSTANCE = 1


class NORMAL_EXTENDED(IntEnum):
    NORMAL = 0
    EXTENDED = 1


class ResourceAllocationMode(IntEnum):
    SIMPLE = 0
    ADVANCED = 1


class BANDWIDTH_TIME(IntEnum):
    BANDWIDTH = 0
    TIME = 1


class PER_CONN_PER_USER(IntEnum):
    PER_CONN = 0
    PER_USER = 1


class TrafficError(IntEnum):
    NOT_PREPARED = 0
    RATE_LENGTH_ERROR = 1
    PREPARED_OK = 2


class PRBSOnOff(IntEnum):
    PRBSOFF = 0
    PRBSON = 1


class ErrorOnOff(IntEnum):
    ERRORSOFF = 0
    ERRORSON = 1


class PRBSPattern(IntEnum):
    PRBS7 = 0
    PRBS9 = 1
    PRBS11 = 2
    PRBS15 = 3
    PRBS23 = 4
    PRBS31 = 5


class PHYSignalStatus(IntEnum):
    NO_SIGNAL = 0
    NO_CDRLOCK = 2
    LOCKED = 3


class ShadowWorkingSelection(IntEnum):
    SHADOW = 0
    WORKING = 1


class TSNConfigProfile(IntEnum):
    AUTOMOTIVE = 0
    IEEE1588V2 = 1


class TSNPortRole(IntEnum):
    GRANDMASTER = 0
    SLAVE = 1


class TSNDeviationMode(IntEnum):
    FIXED = 0


class TSNTimeSource(IntEnum):
    ATOMIC = 0x10
    GPS = 0x20
    TERRESTRIAL = 0x30
    PTP = 0x40
    NTP = 0x50
    HAND_SET = 0x60
    OTHER = 0x90
    INTERNAL_OSC = 0xA0


class TSNSource(IntEnum):
    DRIFT = 0
    DRIFTPRE = 1
    PDELAY = 2
    NRR = 3


class TSNClearStatistics(IntEnum):
    ALL = 0
    PACKETCOUNT = 1
    OFFSET = 2
    PDELAY = 3
    SYNCRATE = 4


class PFCMode(IntEnum):
    VLAN_PCP = 128


class OnOffDefault(IntEnum):
    OFF = 0
    ON = 1
    DEFAULT = 2


class ImpairmentTypeIndex(IntEnum):
    DROP = 0
    MISORDER = 1
    DELAYJITTER = 2
    DUPLICATION = 3
    CORRUPTION = 4
    POLICER = 5
    SHAPER = 6


class FilterType(IntEnum):
    SHADOWN = 0  # “shadow-copy”
    WORKING = 1  # “working-copy”


class VlanType(IntEnum):
    INNER = 0  # VLAN1 (0) (INNER VLAN Tag is specified for the filter – used also when only 1 VLAN), indicates single/inner VLAN-TPID=0x8100
    OUTER = 1  # VLAN2 (1) (OUTER VLAN Tag is specified for the filter), indicates outer VLAN-TPID=0x88A8


class LatencyType(IntEnum):
    INTERPACKET_DISTRIBUTION = 0
    LATENCY_DISTRIBUTION = 1
