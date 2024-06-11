
from enum import IntEnum, IntFlag


# region L23 enums
class ReservedStatus(IntEnum):
    """Test resource reservation status"""

    RELEASED = 0
    """Test resource is released."""
    RESERVED_BY_YOU = 1
    """Test resource is reserved by you."""
    RESERVED_BY_OTHER = 2
    """Test resource is reserved by another user."""


class ReservedAction(IntEnum):
    """Reservation actions."""

    RELEASE = 0
    """Release the test resource."""
    RESERVE = 1
    """Reserve the test resource."""
    RELINQUISH = 2
    """Force release other's ownership of the test resource."""


class ChassisShutdownAction(IntEnum):
    """Chassis shutdown actions."""

    RESTART = 1
    """Restart after shutdown."""
    POWER_OFF = 2
    """Keep power-off after shutdown."""


class OnOff(IntEnum):
    """On or Off."""

    OFF = 0
    """Off"""
    ON = 1
    """On"""


class RESTControlAction(IntEnum):
    """Controls of Valkyrie REST server."""

    START = 0
    """Start the REST server on the chassis."""
    STOP = 1
    """Stop the REST server on the chassis."""
    RESTART = 2
    """Restart the REST server on the chassis."""


class ServiceStatus(IntEnum):
    """Service status."""

    SERVICE_OFF = 0
    """Service is off."""
    SERVICE_ON = 1
    """Service is on."""


class ChassisSessionType(IntEnum):
    """The type of the session between the client and the chassis."""

    MANAGER = 1
    """Connection on port 22606 running binary command (used by ValkyrieManager & VulcanManager)."""
    SCRIPT = 2
    """Connection on port 22611, running CLI command."""


class TimingSource(IntEnum):
    """Module's time sync mode."""

    CHASSIS = 0
    """Module syncs to chassis's clock."""
    EXTERNAL = 1
    """Module syncs to an external clock."""
    MODULE = 2
    """Module syncs to its own clock."""


class MediaCFPState(IntEnum):
    """Modules' CFP state"""

    NOT_CFP = 0
    """This is not a CFP-based test module."""
    NOT_PRESENT = 1
    """No transceiver, the CFP cage is empty"""
    NOT_FLEXIBLE = 2
    """Transceiver present, supporting a fixed speed and port-count"""
    FLEXIBLE = 3
    """Transceiver present, supporting flexible speed and port-count"""


class MediaCFPType(IntEnum):
    """Module's Media CFP Type. What kind of transceiver, may have multiple ports"""

    CFP_UNKNOWN = 0
    """CFP unknown"""
    CFP_INVALID = 1
    """CFP 100G not supported"""
    CFP_1X40_SR4 = 2
    """CFP 40G SR4 850 nm"""
    CFP_2X40_SR4 = 3
    """CFP 40G SR4 850 nm"""
    CFP_1X40_LR4 = 4
    """CFP 40G LR4 1310 nm"""
    CFP_1X100_LR4 = 5
    """CFP 100G LR4 1310 nm"""
    CFP_1X100_SR10 = 6
    """CFP 100G SR10 850 nm / CFP 40G SR4 850 nm"""
    CFP_4X10_SFPP = 7
    """"""
    QSFP_EMPTY = 8
    """QSFP empty"""
    QSFP_UNKNOWN = 9
    """QSFP unknown"""
    QSFP_SR = 10
    """QSFP SR 850 nm"""
    QSFP_LR = 11
    """QSFP LR 1550 nm"""
    QSFP_ER = 12
    """QSFP ER 1550 nm"""
    CXP_UNKNOWN = 13
    """CXP unknown SR10"""
    CXP_SR10 = 14
    """CXP 100G SR10 850 nm / CXP 40G SR4 850 nm"""
    CXP_AOC = 15
    """CXP 100G SR10 AOC / CXP 40G SR4 AOC"""
    CFP4_UNKNOWN = 16
    """CFP4 unknown"""
    CFP4_1X100_LR4 = 17
    """CFP4 100G LR4"""
    CFP4_1X100_ER4 = 18
    """CFP4 100G ER4"""
    CFP4_1X100_SR4 = 19
    """CFP4 100G SR4"""
    QSFP28_CR4 = 20
    """QSFP28 CR4"""
    QSFP28_SR4 = 21
    """QSFP28 SR4"""
    QSFP28_LR4 = 22
    """QSFP28 LR4"""
    QSFP28_ER4 = 23
    """QSFP28 ER4"""
    QSFP28_AOC = 24
    """QSFP28 AOC"""
    QSFP28_ACC = 25
    """QSFP28 ACC"""
    QSFP28_UNKNOWN = 26
    """QSFP28 unknown"""
    QSFP28P_SR4 = 27
    """QSFP+ SR4 850 nm"""
    QSFP28P_LR4 = 28
    """QSFP+ LR4 1310 nm"""
    QSFP28P_ER4 = 29
    """QSFP+ ER4 1500 nm"""
    QSFP28P_CR4 = 30
    """QSFP+ CR4 Copper"""
    QSFP28P_ISM4 = 31
    """QSFP+ iSM4 1310 nm"""
    QSFP28P_UNKNOWN = 32
    """QSFP+ unknown"""
    TCVR_UNKNOWN = 33
    """Transceiver unknown"""
    QSFP28_CWDM4 = 34
    """QSFP28 CWDM4"""
    QSFP28_CWDM4_FEC = 35
    """QSFP28 CWDM4 FEC"""
    QSFP28_PSM4 = 36
    """QSFP28 PSM4"""


class SMAInputFunction(IntEnum):
    """SMA input function"""

    NOT_USED = 0
    """SMA input not used"""
    TX2MHZ = 1
    """TX Clock Ref. 2.048 MHz"""
    TX10MHZ = 2
    """TX Clock Ref. 10.0 MHz"""


class SMAOutputFunction(IntEnum):
    """SMA output function"""

    DISABLED = 0
    """Disabled"""
    PASSTHROUGH = 1
    """Pass-through"""
    P0SOF = 2
    """Port 0 Start-of-Frame Pulse"""
    P1SOF = 3
    """Port 1 Start-of-Frame Pulse"""
    REF2MHZ = 4
    """TX Clock (nom. 2.048 MHz)"""
    REF10MHZ = 5
    """TX Clock (nom. 10.0 MHz)"""
    REF125MHZ = 6
    """TX Clock (nom. 125 MHz)"""
    REF156MHZ = 7
    """TX Clock (nom. 156.25 MHz)"""
    P0RXCLK = 8
    """Port 0 RX Clock (nom. 10.0 MHz)"""
    P1RXCLK = 9
    """Port 1 RX Clock (nom. 10.0 MHz)"""
    P0RXCLK2MHZ = 10
    """Port 0 RX Clock (nom. 2.048 MHz)"""
    P1RXCLK2MHZ = 11
    """Port 1 RX Clock (nom. 2.048 MHz)"""
    TS_PPS = 12
    """Timing Source (Pulse-Per-Second)"""


class SMAStatus(IntEnum):
    """SMA status"""

    OK = 0
    """Status OK"""
    NO_VALID_SIGNAL = 1
    """No valid signal"""


class HasDemo(IntEnum):
    """Demo or not"""

    NON_DEMO = 0
    """Not a demo unit"""
    DEMO = 1
    """Demo unit"""


class IsValid(IntEnum):
    """Whether it is valid"""

    INVALID = 0
    """Invalid"""
    VALID = 1
    """Valid"""


class IsPermanent(IntEnum):
    """Whether it is permanent"""

    NON_PERMANENT = 0
    """Not permanent"""
    PERMANENT = 1
    """Permanent"""


class YesNo(IntEnum):
    NO = 0
    """No"""
    YES = 1
    """Yes"""


class UpdateState(IntEnum):
    """License update state"""

    NONE = 0
    """None"""
    UPDATING = 1
    """Updating"""
    UPDATE_SUCCESS = 2
    """Update successful"""
    UPDATE_FAIL = 3
    """Update failed"""


class IsOnline(IntEnum):
    """Chassis online or not"""

    OFFLINE = 0
    """Chassis offline"""
    ONLINE = 1
    """Chassis online"""


class PortSpeedMode(IntEnum):
    """Port speed mode"""

    AUTO = 0
    """Auto negotiate with peer"""
    F10M = 1
    """Forced to 10 Mbit/s"""
    F100M = 2
    """Forced to 100 Mbit/s"""
    F1G = 3
    """Forced to 1 Gbit/s"""
    F10G = 4
    """Forced to 10 Gbit/s"""
    F40G = 5
    """Forced to 40 Gbit/s"""
    F100G = 6
    """Forced to 100 Gbit/s"""
    F10MHDX = 7
    """Forced to 10 Mbit/s half-duplex"""
    F100MHDX = 8
    """Forced to 100 Mbit/s half-duplex"""
    F10M100M = 9
    """Auto negotiate to 10/100 Mbit/s"""
    F100M1G = 10
    """Auto negotiate to 100 Mbit/s or 1 Gbit/s"""
    F100M1G10G = 11
    """Auto negotiate to 100 Mbit/s or 1 Gbit/s or 10 Gbit/s"""
    F2500M = 12
    """Forced to 2500 Mbit/s"""
    F5G = 13
    """Forced to 5 Gbit/s"""
    F100M1G2500M = 14
    """Auto negotiate to 100 Mbit/s or 1 Gbit/s or 2500 Mbit/s"""
    F25G = 15
    """Forced to 25 Gbit/s"""
    F50G = 16
    """Forced to 50 Gbit/s"""
    F200G = 17
    """Forced to 200 Gbit/s"""
    F400G = 18
    """Forced to 400 Gbit/s"""
    F800G = 19
    """Forced to 800 Gbit/s"""
    F1600G = 20
    """Forced to 1600 Gbit/s"""
    UNKNOWN = 255
    """Speed mode unknown"""


class SyncStatus(IntEnum):
    """Port sync status"""

    NO_SYNC = 0
    """Not sync"""
    IN_SYNC = 1
    """In sync with peer"""


class LoopbackMode(IntEnum):
    """Port loopback mode"""

    NONE = 0
    """Off"""
    L1RX2TX = 1
    """L1 RX-to-TX"""
    L2RX2TX = 2
    """L2 RX-to-TX"""
    L3RX2TX = 3
    """L3 RX-to-TX"""
    TXON2RX = 4
    """TX(on)-to-RX"""
    TXOFF2RX = 5
    """TX(off)-to-RX"""
    PORT2PORT = 6
    """Port-to-Port"""


class TrafficOnOff(IntEnum):
    """Traffic status"""

    OFF = 0
    """Traffic off"""
    ON = 1
    """Traffic on"""
    PREPARING = 2
    """Traffic preparing"""


class StartOrStop(IntEnum):
    STOP = 0
    """Stop the action"""
    START = 1
    """Start the action"""


class LatencyMode(IntEnum):
    """Latency measurement mode"""

    LAST2LAST = 0
    """Last-to-Last"""
    FIRST2LAST = 1
    """First-to-Last"""
    LAST2FIRST = 2
    """Last-to-First"""
    FIRST2FIRST = 3
    """First-to-First"""


class SourceType(IntEnum):
    TX_IFG = 0
    """TX IFG"""
    TX_LEN = 1
    """TX Length"""
    RX_IFG = 2
    """RX IFG"""
    RX_LEN = 3
    """RX Length"""
    RX_LATENCY = 4
    """RX Latency"""
    RX_JITTER = 5
    """RX Jitter"""


class PacketDetailSelection(IntEnum):
    ALL = 0
    """All"""
    TPLD = 1
    """Based on Test Payload ID"""
    FILTER = 2
    """Based on filter"""


class OnOffWithSuppress(IntEnum):
    """Stream status"""

    OFF = 0
    """Off"""
    ON = 1
    """On"""
    SUPPRESS = 2
    """Suppressed"""


class ProtocolOption(IntEnum):
    """Protocol header options"""

    ETHERNET = 1
    """Ethernet II"""
    VLAN = 2
    """VLAN"""
    ARP = 3
    """Address Resolution Protocol"""
    IP = 4
    """IPv4"""
    IPV6 = 5
    """IPv6"""
    UDP = 6
    """User Datagram Protocol (w/o checksum)"""
    TCP = 7
    """Transmission Control Protocol (w/o checksum)"""
    LLC = 8
    """Logic Link Control"""
    SNAP = 9
    """Subnetwork Access Protocol"""
    GTP = 10
    """GPRS Tunnelling Protocol"""
    ICMP = 11
    """Internet Control Message Protocol"""
    RTP = 12
    """Real-time Transport Protocol"""
    RTCP = 13
    """RTP Control Protocol"""
    STP = 14
    """Spanning Tree Protocol"""
    SCTP = 15
    """Stream Control Transmission Protocol"""
    MACCTRL = 16
    """MAC Control"""
    MPLS = 17
    """Multiprotocol Label Switching"""
    PBBTAG = 18
    """Provider Backbone Bridge tag"""
    FCOE = 19
    """Fibre Channel over Ethernet"""
    FC = 20
    """Fibre Channel"""
    FCOETAIL = 21
    """Fibre Channel over Ethernet (tail)"""
    IGMPV3L0 = 22
    """IGMPv3 Membership Query L=0"""
    IGMPV3L1 = 23
    """IGMPv3 Membership Query L=1"""
    UDPCHECK = 24
    """User Datagram Protocol (w/ checksum)"""
    IGMPV2 = 25
    """Internet Group Management Protocol v2"""
    MPLS_TP_OAM = 26
    """MPLS-TP, OAM Header"""
    GRE_NOCHECK = 27
    """Generic Routing Encapsulation (w/o checksum)"""
    GRE_CHECK = 28
    """Generic Routing Encapsulation (w/ checksum)"""
    TCPCHECK = 29
    """Transmission Control Protocol (w/ checksum)"""
    GTPV1L0 = 30
    """GTPv1 (no options), GPRS Tunneling Protocol v1"""
    GTPV1L1 = 31
    """GTPv1 (w/ options), GPRS Tunneling Protocol v1"""
    GTPV2L0 = 32
    """GTPv2 (no options), GPRS Tunneling Protocol v2"""
    GTPV2L1 = 33
    """GTPv2 (w/ options), GPRS Tunneling Protocol v2"""
    IGMPV1 = 34
    """Internet Group Management Protocol v1"""
    PWETHCTRL = 35
    """PW Ethernet Control Word"""
    VXLAN = 36
    """Virtual eXtensible LAN"""
    ETHERNET_8023 = 37
    """Ethernet 802.3"""
    NVGRE = 38
    """Generic Routing Encapsulation (Network Virtualization)"""
    DHCPV4 = 39
    """Dynamic Host Configuration Protocol (IPv4)"""
    GENEVE = 40
    """Generic Network Virtualization Encapsulation"""
    XENA_TPLD = 41
    XENA_TPLD_PI = 42
    XENA_MICROTPLD = 43
    ETHERNET_FCS = 44
    MACCTRLPFC = 45
    """MAC Control for PFC"""
    ECPRI = 46
    """Enhanced Common Public Radio Interface"""
    ROE = 47
    """Radio over Ethernet"""
    ETHERTYPE = 48
    """EtherType"""

    # Generate RAW form 1...64 bytes
    # _ignore_ = "ProtocolOption i"
    # ProtocolOption = vars()
    # for i in range(1, 65):
    #     ProtocolOption["RAW_%d" % i] = 256 - i  # type: ignore
    RAW_1 = 255
    RAW_2 = 254
    RAW_3 = 253
    RAW_4 = 252
    RAW_5 = 251
    RAW_6 = 250
    RAW_7 = 249
    RAW_8 = 248
    RAW_9 = 247
    RAW_10 = 246
    RAW_11 = 245
    RAW_12 = 244
    RAW_13 = 243
    RAW_14 = 242
    RAW_15 = 241
    RAW_16 = 240
    RAW_17 = 239
    RAW_18 = 238
    RAW_19 = 237
    RAW_20 = 236
    RAW_21 = 235
    RAW_22 = 234
    RAW_23 = 233
    RAW_24 = 232
    RAW_25 = 231
    RAW_26 = 230
    RAW_27 = 229
    RAW_28 = 228
    RAW_29 = 227
    RAW_30 = 226
    RAW_31 = 225
    RAW_32 = 224
    RAW_33 = 223
    RAW_34 = 222
    RAW_35 = 221
    RAW_36 = 220
    RAW_37 = 219
    RAW_38 = 218
    RAW_39 = 217
    RAW_40 = 216
    RAW_41 = 215
    RAW_42 = 214
    RAW_43 = 213
    RAW_44 = 212
    RAW_45 = 211
    RAW_46 = 210
    RAW_47 = 209
    RAW_48 = 208
    RAW_49 = 207
    RAW_50 = 206
    RAW_51 = 205
    RAW_52 = 204
    RAW_53 = 203
    RAW_54 = 202
    RAW_55 = 201
    RAW_56 = 200
    RAW_57 = 199
    RAW_58 = 198
    RAW_59 = 197
    RAW_60 = 196
    RAW_61 = 195
    RAW_62 = 194
    RAW_63 = 193
    RAW_64 = 192
    RAW_65 = 191
    RAW_66 = 190
    RAW_67 = 189
    RAW_68 = 188
    RAW_69 = 187
    RAW_70 = 186
    RAW_71 = 185
    RAW_72 = 184
    RAW_73 = 183
    RAW_74 = 182
    RAW_75 = 181
    RAW_76 = 180
    RAW_77 = 179
    RAW_78 = 178
    RAW_79 = 177
    RAW_80 = 176
    RAW_81 = 175
    RAW_82 = 174
    RAW_83 = 173
    RAW_84 = 172
    RAW_85 = 171
    RAW_86 = 170
    RAW_87 = 169
    RAW_88 = 168
    RAW_89 = 167
    RAW_90 = 166
    RAW_91 = 165
    RAW_92 = 164
    RAW_93 = 163
    RAW_94 = 162
    RAW_95 = 161
    RAW_96 = 160
    RAW_97 = 159
    RAW_98 = 158
    RAW_99 = 157
    RAW_100	= 156
    RAW_101	= 155
    RAW_102	= 154
    RAW_103	= 153
    RAW_104	= 152
    RAW_105	= 151
    RAW_106	= 150
    RAW_107	= 149
    RAW_108	= 148
    RAW_109	= 147
    RAW_110	= 146
    RAW_111	= 145
    RAW_112	= 144
    RAW_113	= 143
    RAW_114	= 142
    RAW_115	= 141
    RAW_116	= 140
    RAW_117	= 139
    RAW_118	= 138
    RAW_119	= 137
    RAW_120	= 136
    RAW_121	= 135
    RAW_122	= 134
    RAW_123	= 133
    RAW_124	= 132
    RAW_125	= 131
    RAW_126	= 130
    RAW_127	= 129
    RAW_128	= 128
    RAW_129	= 127
    RAW_130	= 126
    RAW_131	= 125
    RAW_132	= 124
    RAW_133	= 123
    RAW_134	= 122
    RAW_135	= 121
    RAW_136	= 120
    RAW_137	= 119
    RAW_138	= 118
    RAW_139	= 117
    RAW_140	= 116
    RAW_141	= 115
    RAW_142	= 114
    RAW_143	= 113
    RAW_144	= 112
    RAW_145	= 111
    RAW_146	= 110
    RAW_147	= 109
    RAW_148	= 108
    RAW_149	= 107
    RAW_150	= 106


class ModifierAction(IntEnum):
    """Modifier action mode"""

    INC = 0
    """Incrementing"""
    DEC = 1
    """Decrementing"""
    RANDOM = 2
    """Random"""


class LengthType(IntEnum):
    """Packet length type"""

    FIXED = 0
    """Fixed"""
    INCREMENTING = 1
    """Incrementing"""
    BUTTERFLY = 2
    """Butterfly"""
    RANDOM = 3
    """Random"""
    MIX = 4
    """Mix"""


class PayloadType(IntEnum):
    """Packet payload type"""

    PATTERN = 0
    """Pattern"""

    INC8 = INCREMENTING = 1
    """
    .. versionchanged:: 1.1

    Incrementing with 0xFF (8-bit mode)

    """

    PRBS = 2
    """PRBS"""

    RANDOM = 3
    """Random"""

    DEC8 = DECREMENTING = 4
    """
    .. versionchanged:: 1.1

    Decrementing with 0xFF (8-bit mode)
    """

    INC16 = 5
    """
    .. versionadded:: 1.1

    Incrementing with 0xFFFF (16-bit mode)
    """

    DEC16 = 6
    """
    .. versionadded:: 1.1

    Decrementing with 0xFFFF (16-bit mode)
    """


class MDIXMode(IntEnum):
    """MDIX mode"""

    AUTO = 0
    """Auto"""
    MDI = 1
    """MDI"""
    MDIX = 2
    """MDIX"""


class LengthCheckType(IntEnum):
    AT_MOST = 0
    """At Most"""
    AT_LEAST = 1
    """At Least"""


class StartTrigger(IntEnum):
    """Capture start trigger"""

    ON = 0
    """From Traffic On"""
    FCSERR = 1
    """From FCS Error"""
    FILTER = 2
    """From Filter"""
    PLDERR = 3
    """From Payload Error"""


class StopTrigger(IntEnum):
    """Capture stop trigger"""

    FULL = 0
    """Until Capture Buffer Full"""
    FCSERR = 1
    """Until Receiving FCS Error"""
    FILTER = 2
    """Until Filter Matched"""
    PLDERR = 3
    """Until Receiving Payload Error"""
    USERSTOP = 4
    """Until User Stops"""


class PacketType(IntEnum):
    """Type of Packet to Keep in Capture Buffer"""

    ALL = 0
    """All Packets"""
    FCSERR = 1
    """With FCS Errors"""
    NOTPLD = 2
    """Without Test Payload"""
    TPLD = 3
    """With Test Payload"""
    FILTER = 4
    """Filtered Packets"""
    PLDERR = 5
    """With Payload Errors"""


class InjectErrorType(IntEnum):
    """Lane Injection Error Type"""

    HEADERERROR = 1
    """Header Error"""
    ALIGNERROR = 2
    """Alignment Error"""
    BIP8ERROR = 3
    """BIP8 Error"""


class HeaderLockStatus(IntEnum):
    """Physical Lane Header Lock Status"""

    HEADEROFF = 0
    """Header Lock Off"""
    HEADERON = 1
    """Header Lock On"""
    HEADEROFFUNSTABLE = 2
    """Header Lock Off and Unstable"""
    HEADERONUNSTABLE = 3
    """Header Lock On but Unstable"""


class AlignLockStatus(IntEnum):
    """Physical Lane Alignment Lock Status"""

    ALIGNOFF = 0
    """Alignment Lock Off"""
    ALIGNON = 1
    """Alignment Lock On"""
    ALIGNOFFUNSTABLE = 2
    """Alignment Lock Off and Unstable"""
    ALIGNONUNSTABLE = 3
    """Alignment Lock On but Unstable"""


class PRBSLockStatus(IntEnum):
    """Physical Lane PRBS Lock Status"""

    PRBSOFF = 0
    """PRBS Lock Off"""
    PRBSON = 1
    """PRBS Lock On"""
    PRBSOFFUNSTABLE = 2
    """PRBS Lock Off and Unstable"""
    PRBSONUNSTABLE = 3
    """PRBS Lock On but Unstable"""


class MulticastOperation(IntEnum):
    """IGMPv2 Request Type"""

    OFF = 0
    """Off"""
    ON = 1
    """On"""
    JOIN = 2
    """Join"""
    LEAVE = 3
    """Leave"""


class MulticastExtOperation(IntEnum):
    """IGMPv2/v3Request Type"""

    OFF = 0
    """Off"""
    ON = 1
    """On"""
    JOIN = 2
    """Join"""
    LEAVE = 3
    """Leave"""
    INCLUDE = 4
    """Include"""
    EXCLUDE = 5
    """EXclude"""
    LEAVE_TO_ALL = 6
    """Leave To All"""
    GENERAL_QUERY = 7
    """General Query"""
    GROUP_QUERY = 8
    """Group Query"""


class IGMPVersion(IntEnum):
    """IGMP Version"""

    IGMPV2 = 0
    """IGMP Version 2"""
    IGMPV3 = 1
    """IGMP Version 3"""


class TXMode(IntEnum):
    """Port TX Mode"""

    NORMAL = 0
    """Normal"""
    STRICTUNIFORM = 1
    """Strict Uniform"""
    SEQUENTIAL = 2
    """Sequential"""
    BURST = 3
    """Burst"""


class PayloadMode(IntEnum):
    """Payload Mode"""

    NORMAL = 0
    """Normal"""
    EXTPL = 1
    """Extend Payload"""
    CDF = 2
    """Custom Data Field"""


class BRRMode(IntEnum):
    """BRR Mode"""

    SLAVE = 0
    """Slave Mode"""
    MASTER = 1
    """Master Mode"""


class TXClockSource(IntEnum):
    """TX Clock Source"""

    MODULELOCALCLOCK = 0
    """Module Local Clock"""
    SMAINPUT = 1
    """SMA Input"""
    P0RXCLK = 2
    """Port 0 RX Clock"""
    P1RXCLK = 3
    """Port 1 RX Clock"""
    P2RXCLK = 4
    """Port 2 RX Clock"""
    P3RXCLK = 5
    """Port 3 RX Clock"""
    P4RXCLK = 6
    """Port 4 RX Clock"""
    P5RXCLK = 7
    """Port 5 RX Clock"""
    P6RXCLK = 8
    """Port 6 RX Clock"""
    P7RXCLK = 9
    """Port 7 RX Clock"""


class TXClockStatus(IntEnum):
    """TX Clock Status"""

    OK = 0
    """Clock OK"""
    NOVALIDTXCLK = 1
    """No Valid TX Clock"""


class LoopBandwidth(IntEnum):
    """Loop Bandwidth"""

    BW103HZ = 1
    """Loop Bandwidth = 103 Hz"""
    BW207HZ = 2
    """Loop Bandwidth = 207 Hz"""
    BW416HZ = 3
    """Loop Bandwidth = 416 Hz"""
    BW1683HZ = 4
    """Loop Bandwidth = 1683 Hz"""
    BW7019HZ = 5
    """Loop Bandwidth = 7019 Hz"""


class MediaConfigurationType(IntEnum):
    """Module Media Configuration Type"""

    CFP4 = 0
    """CFP4"""

    QSFP28 = QSFP28_NRZ = 1
    """QSFP28, 25G serdes"""

    CXP = 2
    """CXP"""

    SFP28 = 3
    """SFP28, 25G serdes"""

    QSFP56 = QSFP56_PAM4 = 4
    """QSFP56, 56G serdes"""

    QSFPDD = QSFPDD_PAM4 = 5
    """QSFP-DD, 56G serdes"""

    SFP56 = 6
    """SFP56"""

    SFP_DD = SFPDD = 7
    """SFP-DD"""

    SFP112 = 8
    """SFP112"""

    QSFP_DD_NRZ = QSFPDD_NRZ = 9
    """QSFP-DD, 25G serdes"""

    QSFP28_PAM4 = 10
    """QSFP28 4x26G KP -> 2x53G KP PAM4"""

    CFP = 99
    """CFP"""

    BASE_T1 = 100
    """BASE-T1"""

    BASE_T1S = 101
    """BASE-T1S"""

    QSFPDD800 = 110
    """QSFP-DD800, 112G serdes"""

    QSFP112 = 111
    """QSFP112, 112G serdes"""

    OSFP800 = 112
    """OSFP800, 112G serdes"""

    QSFPDD800_ANLT = 113
    """QSFPDD800, 112G serdes, L1/ANLT"""

    QSFP112_ANLT = 114
    """QSFP112, 112G serdes, L1/ANLT"""

    OSFP800_ANLT = 115
    """OSFP800, 112G serdes, L1/ANLT"""

    OSFP = 116
    """OSFP, 56G serdes"""

    QSFPDD_ANLT = 117
    """QSFP-DD, 56G serdes, L1/ANLT"""

    QSFP56_ANLT = 118
    """QSFP56, 56G serdes, L1/ANLT"""

    OSFP_ANLT = 119
    """OSFP, 56G serdes, L1/ANLT"""

    UNKNOWN = 255


class TXHState(IntEnum):
    """Recent Change in EEE State on TX"""

    TXH_NA = 0
    """Leaving or Going Into"""
    TXH_X = 1
    """No Activity"""


class RXHState(IntEnum):
    """Recent Change in EEE State on RX"""

    RXH_NA = 0
    """Leaving or Going Into"""
    RXH_X = 1
    """No Activity"""


class TXCState(IntEnum):
    """TX EEE State"""

    TXC_ACTIVE = 0
    """Active"""
    TXC_LPI = 1
    """Low Power"""


class RXCState(IntEnum):
    """RX EEE State"""

    RXC_ACTIVE = 0
    """Active"""
    RXC_LPI = 1
    """Low Power"""


class LinkState(IntEnum):
    """Low Power Mode Link State"""

    LINK_DOWN = 0
    """Link Down"""
    LINK_UP = 1
    """Link Up"""


class FaultSignaling(IntEnum):
    """Fault Signaling Behavior"""

    NORMAL = 0
    """Normal"""
    FORCE_LOCAL = 1
    """Forced to Local"""
    FORCE_REMOTE = 2
    """Forced to Remote"""
    DISABLED = 3
    """Disabled"""


class LocalFaultStatus(IntEnum):
    """Local Fault Status"""

    OK = 0
    """OK"""
    LOCAL_FAULT = 1
    """Local Fault"""


class RemoteFaultStatus(IntEnum):
    """Remote Fault Status"""

    OK = 0
    """OK"""
    REMOTE_FAULT = 1
    """Remote Fault"""


class TPLDMode(IntEnum):
    """Test Payload Mode"""

    NORMAL = 0
    """Normal"""
    MICRO = 1
    """Micro"""


class SerdesStatus(IntEnum):
    """Serdes Status"""

    STOPPED = 0
    """Stopped"""
    STARTED = 1
    """Started"""
    INITIALIZING = 2
    """Initializing"""
    PLOTTING = 3
    """Plotting"""


class FECMode(IntEnum):
    """FEX Mode"""

    OFF = 0
    """Off"""
    ON = 1
    """On"""
    RS_FEC = 2
    """RS FEC"""
    FC_FEC = 3
    """Firecode FEC"""
    RS_FEC_KR = 4
    """RS FEC KR"""
    RS_FEC_KP = 5
    """RS FEC KP"""
    RS_FEC_INT = 6
    """RS FEC Int"""


class PRBSInsertedType(IntEnum):
    """PRBS Type"""

    CAUI_VIRTUAL = 0
    """CAUI Virtual"""
    PHY_LINE = 1
    """PHY Line"""
    PHY_HOST = 2
    """PHY Host"""
    TCVR = 3
    """Transceiver"""


class PRBSPolynomial(IntEnum):
    """PRBS Polynomial"""

    PRBS7 = 0
    """PRBS-7"""
    PRBS9 = 1
    """PRBS-9"""
    PRBS11 = 2
    """PRBS-11"""
    PRBS15 = 3
    """PRBS-15"""
    PRBS23 = 4
    """PRBS-23"""
    PRBS31 = 5
    """PRBS-31"""
    PRBS58 = 6
    """PRBS-58"""
    PRBS49 = 7
    """PRBS-49"""
    PRBS10 = 8
    """PRBS-10"""
    PRBS20 = 9
    """PRBS-20"""
    PRBS13 = 10
    """PRBS-13"""
    SSPRQ = 24
    """SSPRQ"""
    SQUARE_WAVE = 25
    """Square Wave"""


class PRBSInvertState(IntEnum):
    """PRBS Invert State"""

    NON_INVERTED = 0
    """Non-inverted"""
    INVERTED = 1
    """Inverted"""


class PRBSStatisticsMode(IntEnum):
    """PRBS Statistics Mode"""

    ACCUMULATIVE = 0
    """Accumulative"""
    PERSECOND = 1
    """Per Second"""


class PauseMode(IntEnum):
    """Pause Mode"""

    NO_PAUSE = 0
    """No Pause"""
    SYM_PAUSE = 1
    """Symmetric Pause"""
    ASYM_PAUSE = 2
    """Asymmetric Pause"""


class MulticastHeaderFormat(IntEnum):
    """Additional Header to IGMPv2/v3 Packets"""

    NOHDR = 0
    """No Header"""
    VLAN = 1
    """VLAN"""


class PFCMode(IntEnum):
    """The PFC CoS value of the stream"""
    ZERO = 0
    """the PFC CoS value = 0"""
    ONE = 1
    """the PFC CoS value = 1"""
    TWO = 2
    """the PFC CoS value = 2"""
    THREE = 3
    """the PFC CoS value = 3"""
    FOUR = 4
    """the PFC CoS value = 4"""
    FIVE = 5
    """the PFC CoS value = 5"""
    SIX = 6
    """the PFC CoS value = 6"""
    SEVEN = 7
    """the PFC CoS value = 7"""
    VLAN_PCP = 128
    """PFC CoS value is automatically using the outer VLAN PCP value of the stream. If the VLAN field is missing, the stream won't have a PFC CoS."""
    OFF = 129
    """Remove PFC CoS value of the stream."""


class PRBSOnOff(IntEnum):
    """PRBS Status"""

    PRBSOFF = 0
    """PRBS Off"""
    PRBSON = 1
    """PRBS On"""


class ErrorOnOff(IntEnum):
    """PRBS Error Injection Status"""

    ERRORSOFF = 0
    """PRBS Error Injection Off"""
    ERRORSON = 1
    """PRBS Error Injection On"""


class PRBSPattern(IntEnum):
    """PRBS Pattern"""

    PRBS7 = 0
    """PRBS-7"""
    PRBS9 = 1
    """PRBS-9"""
    PRBS11 = 2
    """PRBS-11"""
    PRBS15 = 3
    """PRBS-15"""
    PRBS23 = 4
    """PRBS-23"""
    PRBS31 = 5
    """PRBS-31"""
    PRBS58 = 6
    """PRBS-58"""
    PRBS49 = 7
    """PRBS-49"""
    PRBS10 = 8
    """PRBS-10"""
    PRBS20 = 9
    """PRBS-20"""
    PRBS13 = 10
    """PRBS-13"""


class PHYSignalStatus(IntEnum):
    """PHY Signal Status"""

    NO_SIGNAL = 0
    """No Signal"""
    NO_CDRLOCK = 2
    """No CDR Lock"""
    LOCKED = 3
    """Locked"""


class OnOffDefault(IntEnum):
    """On Off Default Status"""

    OFF = 0
    """Off"""
    ON = 1
    """On"""
    DEFAULT = 2
    """Default"""


class TimeKeeperLicenseFileState(IntEnum):
    """TimeKeeper License File State"""

    NA = 0
    """Not Available"""
    INV = 1
    """Invalid"""
    VALID = 2
    """Valid"""


class TimeKeeperLicenseType(IntEnum):
    """TimeKeeper License Type"""

    UNDEF = 0
    """Undefined"""
    CLIENT = 1
    """TimeKeeper Client"""
    SERVER = 2
    """TimeKeeper Server"""


class TimeKeeperLicenseError(IntEnum):
    """TimeKeeper License Error"""

    NO_LICENSE_ERROR = 0
    """No License Error"""
    INVALID_SERIALNO = 1
    """Invalid Serial Number"""
    INVALID_CHASSISTYPE = 2
    """Invalid Chassis Type"""


class SystemUpdateStatus(IntEnum):
    """System Update Status"""

    OK = 0
    """Update OK"""
    FAILED_SCRIPT = 1
    """Script Failed"""
    FAILED_PREP = 10
    """Preparation Failed"""
    FAILED_FILENAME = 11
    """Filename Failed"""
    FAILED_DECRYPT = 12
    """Decryption Failed"""
    FAILED_UNPACK = 13
    """Unpacking Failed"""
    FAILED_VERIFY = 14
    """Verification Failed"""
    FAILED_MOVE = 15
    """Moving Failed"""


class TimeKeeperServiceStatus(IntEnum):
    """TimeKeeper Service Status"""

    STOPPED = 0
    """Service Stopped"""
    STARTED = 1
    """Service Started"""
    NA = 2
    """Not Available"""


class TimeKeeperServiceAction(IntEnum):
    """TimeKeeper Service Action"""

    STOP = 0
    """Stop"""
    START = 1
    """Start"""
    RESTART = 2
    """Restart"""


class CustomDefaultCommand(IntEnum):
    """Custom Default Command"""

    SET = 0
    """Set Custom Default"""
    CLEAR = 1
    """Clear Custom Default"""


class CustomDefaultScope(IntEnum):
    """Custom Default Scope"""

    ALL = 0
    """All"""
    INSTANCE = 1
    """Instance"""


class TrafficError(IntEnum):
    """Traffic Error"""

    NOT_PREPARED = 0
    """Not Prepared"""
    RATE_LENGTH_ERROR = 1
    """Rate Length Error"""
    PREPARED_OK = 2
    """Prepared OK"""


class TrafficEngine(IntEnum):
    """Traffic Engine"""

    TGA = 1
    """Normal TGA"""
    MICRO_TGA = 2
    """Micro TGA"""


class LinkTrainFrameLock(IntEnum):
    """L1 Link Training Frame Lock Status"""

    LOST = 0
    """No Frame Lock detected"""

    LOCKED = 1
    """Frame Lock detected"""


class PPMSweepMode(IntEnum):
    """Module clock PPM Sweep Modes"""

    NONE = 0
    """Off"""
    TRIANGLE = 1
    """Triangle sweeping"""


class PPMSweepStatus(IntEnum):
    """Module clock PPM Sweep Status"""

    OFF = 0
    """Off"""
    SWEEPING = 1
    """The module is sweeping"""


class ReconciliationSublayerSupport(IntEnum):
    """Reconciliation Sublayer Support"""

    NO_SUPPORT = 0
    """Not Supported"""
    FAULT_SIGNALING = 1
    """Supported, which means P_FAULTSTATUS and P_FAULTSIGNALLING are supported by the port."""

class StreamOption(IntEnum):
    """Stream Options"""

    INCPLDFROM0 = 0
    """This flag affects the INC8/DEC8/INC16/DEC16 payload types (refer to the PS_PAYLOAD command): With the flag set, the first payload byte/word after the header will be 0 (INC8/INC16) or -1 (DEC8/DEC16). With the flag unset, the default is used: The first payload byte/word of the payload will be equal to <length of header> (INC8/INC16), or -<length of header> - 1 (DEC8/DEC16)."""

# endregion

# region L47 enums
class Role(IntEnum):
    """L47 port role"""

    CLIENT = 0
    """Client"""
    SERVER = 1
    """Server"""


class Timescale(IntEnum):
    """Time scale"""

    MSECS = 0
    """Milliseconds"""
    SECONDS = 1
    """Seconds"""
    MINUTES = 2
    """Minutes"""
    HOURS = 3
    """Hours"""


class MSSType(IntEnum):
    """TCP Maximum Segment Type"""

    FIXED = 0
    """Fixed"""
    INCREMENT = 1
    """Incrementing"""
    RANDOM = 2
    """Pseudorandom"""


class RTOType(IntEnum):
    """TCP RTO Type"""

    STATIC = 0
    """Static RTO"""
    DYNAMIC = 1
    """Dynamic RTO"""


class CongestionType(IntEnum):
    """TCP Congestion Control Algorithm"""

    NONE = 0
    """No TCP Congestion Control"""
    RENO = 1
    """RENO"""
    NEW_RENO = 2
    """New RENO"""


class IsEnabled(IntEnum):
    DISABLE = 0
    ENABLE = 1


class AlgorithmMethod(IntEnum):
    """Algorithm to calculate the TCP initial congestion window (ICWND)"""

    RFC5681 = 0
    """RFC 5681"""
    RFC2581 = 1
    """RFC 2581"""
    FIXED_FACTOR = 2
    """Fixed"""


class AutoOrManual(IntEnum):
    AUTOMATIC = 0
    MANUAL = 1


class EmbedIP(IntEnum):
    """Should Embed IP in MAC"""

    DONT_EMBED_IP = 0
    """Do not embed"""
    EMBED_IP = 1
    """Embed IP in MAC"""


class ApplicationLayerBehavior(IntEnum):
    """L47 Test Application Type"""

    NONE = 0
    """TCP connections are created according to the client and server ranges, and ramped up/down as specified in the load profile. But no payload is transmitted."""
    RAW = 1
    """Differs from ``NONE`` in that it transmits payload when the TCP connection is established."""
    REPLAY = 2
    """PCAP replay."""


class TrafficScenario(IntEnum):
    """Traffic direction scenario"""

    DOWNLOAD = 0
    """Server transmits payload to client."""
    UPLOAD = 1
    """Client transmits payload to server."""
    BOTH = 2
    """Payload is transmitted in both directions."""
    ECHO = 3
    """Client transmits payload to server, server echoes the payload back"""


class PayloadGenerationMethod(IntEnum):
    """Payload generation method."""

    FIXED = 0
    """Payload has a fixed value."""
    INCREMENT = 1
    """Payload consist of incrementing bytes."""
    RANDOM = 2
    """Payload consists of pseudo random bytes with a repeat cycle of 1 MB."""
    LONGRANDOM = 3
    """Payload consists of pseudo random bytes with a repeat cycle of 4 GB."""


class InfiniteOrFinite(IntEnum):
    INFINITE = 0
    FINITE = 1


class WhoClose(IntEnum):
    """How to close TCP connection when all payload has been transmitted."""

    NONE = 0
    """Keep the connection open after last byte is transmitted"""
    CLIENT = 1
    """Client closes the connection after last byte is receiver/transmitted"""
    SERVER = 2
    """Server closes the connection after last byte is transmitted"""


class LifecycleMode(IntEnum):
    """Connection lifecycle mode"""

    ONCE = 0
    """Connections are established during the ramp-up phase and not closed until the ramp-down phase of the load profile. That is, each configured connection only exists once."""
    IMMORTAL = 1
    """Connections are established during the ramp-up phase of the load profile, and are closed after the configured lifetime (configured by  P4G_RAW_CONN_LIFETIME).
    As connections close, new connections are established, attempting to keep the concurrent number of established connections constant.
    A new connection will have the same IP address as the connection it replaces, but will have a new TCP port number.
    This will simulate that the user (defined by the client IP address) is living on, and creates new connections as old connections close.
    """
    REINCARNATE = 2
    """Connections are established during the ramp-up phase of the load profile, and are closed after the configured lifetime (configured by  P4G_RAW_CONN_LIFETIME).
    As connections close, new connections are established, attempting to keep the concurrent number of established connections constant.
    A new connection will have the same TCP port number as the connection it replaces, but will have a new IP address.
    This will simulate that the user (defined by the client IP address) ceases to exist, and new users appear as old users die.
    """


class L47IPVersion(IntEnum):
    """IP version of the Connection Group"""

    IPV4 = 4
    """IPv4"""
    IPV6 = 6
    """IPv6"""


class L47ProtocolType(IntEnum):
    """L4 protocol of the Connection Group"""

    TCP = 0
    """TCP"""
    UDP = 1
    """UDP"""


class L47TrafficState(IntEnum):
    """L47 traffic state"""

    OFF = 0
    """Off"""
    ON = 1
    """On"""
    STOP = 2
    """Stop"""
    PREPARE = 3
    """Prepare"""
    PRERUN = 4
    """Prerun"""


class L47PortState(IntEnum):
    """L47 port state"""

    OFF = 0
    """Off"""
    PREPARE = 1
    """Prepare"""
    PREPARE_RDY = 2
    """Prepare Ready"""
    PREPARE_FAIL = 3
    """Prepare Failed"""
    PRERUN = 4
    """Prerun"""
    PRERUN_RDY = 5
    """Prepare Ready"""
    RUNNING = 6
    """Running"""
    STOPPING = 7
    """Stopping"""
    STOPPED = 8
    """Stopped"""
    DHCP = 9
    """DHCP Running"""


class L47PortSpeed(IntEnum):
    """L47 port speed mode"""

    AUTO = 0
    """Auto"""
    F100M = 1
    """100 Mbit/s"""
    F1G = 2
    """1 Gbit/s"""
    F2_5G = 3
    """2.5 Gbit/s"""
    F5G = 4
    """5 Gbit/s"""
    F10G = 5
    """10 Gbit/s"""
    F25G = 6
    """25 Gbit/s"""
    F40G = 7
    """40 Gbit/s"""
    F50G = 8
    """50 Gbit/s"""
    F100G = 9
    """100 Gbit/s"""


class CaptureSize(IntEnum):
    """Capture size"""

    FULL = 0
    """Capture whole packets"""
    SMALL = 1
    """Capture truncated packets"""


class ReplayParserState(IntEnum):
    OFF = 0
    PARSING = 1


class IsPresent(IntEnum):
    NOT_PRESENT = 0
    PRESENT = 1


class LicenseSpeed(IntEnum):
    UNDEFINED   = 0
    F100M       = 1
    F1G         = 2
    F2_5G       = 3
    F5G         = 4
    F10G        = 5
    F25G        = 6
    F40G        = 7
    F50G        = 8
    F100G       = 9


class TLSVersion(IntEnum):
    """TLS protocol version"""

    SSLV3 = 0
    """SSL v3"""
    TLS10 = 1
    """TLS v1.0"""
    TLS11 = 2
    """TLS v1.1"""
    TLS12 = 3
    """TLS v1.2"""


class ResourceAllocationMode(IntEnum):
    SIMPLE = 0
    ADVANCED = 1


class ReplaySchedulingMode(IntEnum):
    BANDWIDTH = 0
    TIME = 1


class ReplaySyncBasedOn(IntEnum):
    PER_CONN = 0
    PER_USER = 1


# endregion

# region Impairment enums
class CorruptionType(IntEnum):
    """Impairment corruption type"""

    OFF = 0
    """Off"""
    ETH = 1
    """Ethernet"""
    IP = 2
    """IP"""
    UDP = 3
    """UDP"""
    TCP = 4
    """TCP"""
    BER = 5
    """Bit Error Rate"""


class PolicerMode(IntEnum):
    """Policer mode"""

    L1 = 0
    """Policer performed at Layer 1 level. I.e. including the preamble and min inter-packet gap."""
    L2 = 1
    """Policer performed at Layer 2 level. I.e. excluding the preamble and min inter-packet gap"""


class FilterUse(IntEnum):
    """Use of filter."""

    OFF = 0
    """No filtering will be done"""
    AND = 1
    """Filtering will be done"""


class InfoAction(IntEnum):
    """Action of filter."""

    EXCLUDE = 0
    """Matching packets are excluded from the flow"""
    INCLUDE = 1
    """Matching packets are included from the flow"""


class L2PlusPresent(IntEnum):
    """Presence of Layer-2+ protocols"""

    NA = 0
    """No Layer 2+ protocols"""
    VLAN1 = 1
    """One VLAN Tag is present"""
    VLAN2 = 2
    """Two VLAN Tags are present"""
    MPLS = 3
    """MPLS label is present"""


class L3Present(IntEnum):
    """Presence of Layer-3 protocols"""

    NA = 0
    """No Layer 3 protocols"""
    IP4 = 1
    """IPv4 is present"""
    IP6 = 2
    """IPv6 is present"""


class FilterMode(IntEnum):
    """Impairment Filter Mode"""

    BASIC = 0
    """Basic Mode"""
    EXTENDED = 1
    """Extended Mode"""


class ImpairmentLatencyMode(IntEnum):
    """Impairment Latency Mode"""

    NORMAL = 0
    """Normal"""
    EXTENDED = 1
    """Extended"""


class ShadowWorkingSelection(IntEnum):
    """Shadow Working Selection"""

    SHADOW = 0
    """Shadow"""
    WORKING = 1
    """Working"""


class FilterType(IntEnum):
    """Filter Type for Impairment"""

    SHADOW = 0
    """Shadow Copy"""
    WORKING = 1
    """Working Copy"""


class FilterVlanType(IntEnum):
    """VLAN PCP Settings for VLAN Filter"""

    INNER = 0
    """VLAN1 (0) (INNER VLAN Tag is specified for the filter – used also when only 1 VLAN), indicates single/inner VLAN-TPID=0x8100"""
    OUTER = 1
    """VLAN2 (1) (OUTER VLAN Tag is specified for the filter), indicates outer VLAN-TPID=0x88A8"""


class LatencyTypeCustomDist(IntEnum):
    """Latency Type for Custom Distribution"""

    INTERPACKET_DISTRIBUTION = 0
    """Interpacket Distribution"""
    LATENCY_DISTRIBUTION = 1
    """Latency Distribution"""


class ImpairmentTypeIndex(IntEnum):
    """Impairment Type Index"""

    DROP = 0
    """Drop"""
    MISORDER = 1
    """Misorder"""
    LATENCYJITTER = 2
    """Delay/Jitter"""
    DUPLICATION = 3
    """Duplication"""
    CORRUPTION = 4
    """Corruption"""
    POLICER = 5
    """Policer"""
    SHAPER = 6
    """Shaper"""


# endregion

# region TSN enums
class TSNConfigProfile(IntEnum):
    """TSN PTP Configuration profile"""

    AUTOMOTIVE = 0
    """Defaults suitable for automotive testing"""
    IEEE1588V2 = 1
    """Defaults suitable for PTP  testing"""


class TSNPortRole(IntEnum):
    """TSN port role"""

    GRANDMASTER = 0
    """Grandmaster role"""
    SLAVE = 1
    """Slave role"""


class TSNDeviationMode(IntEnum):
    FIXED = 0


class TSNTimeSource(IntEnum):
    """TSN time source"""

    ATOMIC = 0x10
    """Atomic"""
    GPS = 0x20
    """GPS"""
    TERRESTRIAL = 0x30
    """Terrestrial"""
    PTP = 0x40
    """PTP"""
    NTP = 0x50
    """NTP"""
    HAND_SET = 0x60
    """Handset"""
    OTHER = 0x90
    """Other"""
    INTERNAL_OSC = 0xA0
    """Internal oscillator"""


class TSNHistogramSource(IntEnum):
    """Data source for TSN histogram"""

    DRIFT = 0
    """Post-servo offset to Grandmaster"""
    DRIFTPRE = 1
    """Pre-servo offset to Grandmaster"""
    PDELAY = 2
    """PDelay data."""
    NRR = 3
    """Neighbor Rate Ratio data."""


class TSNStatisticsTypes(IntEnum):
    """TSN Statistics Types"""

    ALL = 0
    """All."""
    PACKETCOUNT = 1
    """Packet count."""
    OFFSET = 2
    """Offset."""
    PDELAY = 3
    """PDelay."""
    SYNCRATE = 4
    """Sync rate."""


# endregion

# region ANLT enums


class AutoNegMode(IntEnum):
    """Auto Neg Mode"""

    ANEG_OFF = 0
    """Auto Neg Off"""
    ANEG_ON = 1
    """Auto Neg On"""


class AutoNegTecAbility(IntEnum):
    """Auto Neg Technical Abilities"""

    DEFAULT_TECH_MODE = 0
    """Default Tech Mode"""
    IEEE_10G_KR = 4
    """IEEE 10G KR"""
    IEEE_40G_CR4 = 16
    """IEEE 40G CR4"""
    IEEE_100G_KR4 = 128
    """IEEE 100G KR4"""
    IEEE_100G_CR4 = 256
    """IEEE 100G CR4"""
    IEEE_25GBASE_CRS_KRS = 512
    """IEEE 25GBASE CRS KRS"""
    IEEE_25GBASE_CR_KR = 1024
    """IEEE 25GBASE CR KR"""
    IEEE_50GBASE_CR_KR = 8192
    """IEEE 50GBASE CR KR"""
    IEEE_100GBASE_CR2_KR2 = 16384
    """IEEE 100GBASE CR2 KR2"""
    IEEE_200GBASE_CR4_KR4 = 32768
    """IEEE 200GBASE CR4 KR4"""
    IEEE_100GBASE_KR1 = 65536
    """IEEE 100GBASE KR1"""
    IEEE_200GBASE_KR2 = 131072
    """IEEE 200GBASE KR2"""
    IEEE_400GBASE_KR4 = 262144
    """IEEE 400GBASE KR4"""
    EC_25GBASE_KR1 = 16777216
    """EC 25GBASE KR1"""
    EC_25GBASE_CR1 = 33554432
    """EC 25GBASE CR1"""
    EC_50GBASE_KR2 = 67108864
    """EC 50GBASE KR2"""
    EC_50GBASE_CR2 = 134217728
    """EC 50GBASE CR2"""
    EC_400GBASE_KR8 = 268435456
    """EC 400GBASE KR8"""
    EC_800GBASE_KR8 = 536870912
    """EC 800GBASE KR8"""
    EC_50G_CR1_KR1 = 503
    """EC 50G CR1 KR1"""
    BAM_50G_CR1_KR1 = 504
    """BAM 50G CR1 KR1"""
    BAM_50G_CR2_KR2 = 505
    """BAM 50G CR2 KR2"""
    BAM_100G_CR2_KR2 = 1002
    """BAM 100G CR2 KR2"""
    BAM_100G_CR4_KR4 = 1003
    """BAM 100G CR4 KR4"""
    BAM_200G_CR2_KR2 = 2002
    """BAM 200G CR2 KR2"""
    BAM_400G_CR8_KR8 = 4001
    """BAM 400G CR8 KR8"""


class AutoNegFECOption(IntFlag):
    """Auto Neg FEC Options"""

    DEFAULT_FEC = 0
    """Default FEC"""
    NO_FEC = 1
    """No FEC"""
    FCFEC = 2
    """Firecode FEC"""
    RSFEC_CL91 = 4
    """RS FEC Cl91"""
    RS528 = 256
    """RS 528"""
    RS544 = 512
    """RS 544"""
    RS272 = 1024
    """RS 272"""
    RSFEC_CL161 = 8
    """RS CL 161"""


class AutoNegFECType(IntEnum):
    """Auto Neg FEC Type"""

    PENDING = 0
    """Pending"""
    NO_FEC = 1
    """No FEC"""
    RS_FEC = 513
    """RS FEC"""
    FC_FEC = 257
    """Firecode FEC"""


class AutoNegStatus(IntEnum):
    """Auto Neg Status"""

    UNKNOWN = 0
    """Unknown"""
    ENABLE = 1
    """Enabled"""
    TRANSMIT_DISABLE = 2
    """Transmit Disabled"""
    ABILITY_DETECT = 3
    """Ability Detected"""
    ACKNOWLEDGE_DETECT = 4
    """Acknowledge Detected"""
    COMPLETE_ACKNOWLEDGE = 5
    """Complete Acknowledge"""
    NEXT_PAGE_WAIT = 6
    """Next Page Wait"""
    AN_GOOD_CHECK = 7
    """AN Good Check"""
    AN_GOOD = 8
    """AN Good"""


class AutoNegFECStatus(IntFlag):
    """Auto Neg FEC Status"""

    DEFAULT_FEC = 0
    """Default FEC"""
    NO_FEC = 1
    """No FEC"""
    FC_FEC = 2
    """Firecode FEC"""
    RSFEC_CL91 = 4
    """RS FEC Cl91"""
    RS528 = 256
    """RS 528"""
    RS544 = 512
    """RS 544"""
    RS272 = 1024
    """RS 272"""
    RSFEC_CL161 = 8
    """RS CL 161"""


class LinkTrainingMode(IntEnum):
    """Link Training Mode"""

    START_AFTER_AUTONEG = 0
    """Link training starts automatically after autoneg is completed"""

    STANDALONE = 1
    """Link training procedure is done automatically by the port"""

    DISABLED = 2
    """Link training is disabled"""

    INTERACTIVE = 3
    """Link training in interactive mode, requiring manual operation."""

    UNKNOWN = 255
    """Unknown link training mode"""


class PAM4FrameSize(IntEnum):
    """PAM4 Frame Size"""

    P16K_FRAME = 0
    """16K Frame Size"""
    P4K_FRAME = 1
    """4K Frame Size"""


class LinkTrainingInitCondition(IntEnum):
    """Link Training Initialization Condition"""

    NO_INIT = 0
    """No Initialization"""
    INIT_ENABLED = 1
    """Initialization Enabled"""


class NRZPreset(IntEnum):
    """Link Training NRZ Preset"""

    NRZ_NO_PRESET = 0
    """NRZ without Preset"""
    NRZ_WITH_PRESET = 1
    """NRZ with Preset"""


class TimeoutMode(IntEnum):
    """Link Training Timeout Mode"""

    DEFAULT = 0
    """Default Timeout"""
    DISABLED = 255
    """Timeout Disabled"""


class LinkTrainingStatusMode(IntEnum):
    """Link Training Status Mode"""

    DISABLED = 0
    """Disabled"""
    ENABLED = 1
    """Enabled"""


class LinkTrainingStatus(IntEnum):
    """Link Training Status"""

    NOT_TRAINED = 0
    """Not Trained"""
    TRAINED = 1
    """Trained"""


class LinkTrainingFailureType(IntEnum):
    """Link Training Failure Type"""

    NO_FAILURE = 0
    """No Failure"""
    FRAME_LOCK_ERROR = 1
    """Frame Lock Error"""
    SNR_BELOW_THRESHOLD = 2
    """SNR Below Threshold"""
    TIME_OUT_FAILURE = 3
    """Timeout Failure"""


class Layer1ConfigType(IntEnum):
    """
    .. versionadded:: 1.1

    Enums for PL1_CFG_TMP's type.
    """

    AUTO_LINK_RECOVERY = 0
    """ANLT Auto Link Recovery"""

    AN_LOOPBACK = 1
    """Auto-negotiation loopback config"""

    LT_INITIAL_MODULATION = 2
    """The initial modulation (0=NRZ, 1=PAM4, 2=PAM4_WITH_PRECODING) """

    LL_DEBUG_INFO = 3
    """Return the an/lt module base and RX and TX (serdes index, base address)"""

    LT_TRAINING_ALGORITHM = 4
    """The link training algorithm to use"""

    ANLT_LOG_CONTROL = 5
    """Control what should be logged by anlt"""

    ANLT_STRICT_MODE = 6
    """Set AN/LT strict mode. In strict mode errored framed will be ignored"""

    AN_LT_XLA_MODE = 7
    """Set XLA mode. If enabled XLA dumps will, if triggered, be logged automatically"""


class Layer1LogType(IntEnum):
    """

    .. versionadded:: 1.1

    .. warning::

        Still in beta mode. Subjected to changes

    Enums for PL1_LOG's type.
    """

    AN = 0
    """Log for auto-neg"""

    LT = 1
    """Log for link training"""


class LinkTrainAlgorithm(IntEnum):
    """
    .. versionadded:: 1.2

    Link Training Algorithm

    """

    INTERACTIVE = 0
    """INTERACTIVE"""

    ALG0 = 1
    """ALGORITHM 0"""

    ALGN1 = 2
    """ALGORITHM -1"""


class LinkTrainCmd(IntEnum):
    """
    .. versionadded:: 1.1

    Link Training commands

    """

    CMD_NOP = 0
    """No operation. Used for 'ping' testing"""

    CMD_INC = 1
    """Increment the coeff provided in ARG"""

    CMD_DEC = 2
    """Decrement the coeff provided in ARG"""

    CMD_PRESET = 3
    """Set the preset provided in ARG"""

    CMD_ENCODING = 4
    """Set encoding provided in ARG"""

    CMD_NO_EQ = 5
    """Set the coeff to NO_EQ"""

    CMD_LOCAL_TRAINED = 255
    """Signal training completed"""


class LinkTrainPresets(IntEnum):
    """
    .. versionadded:: 1.1

    Link Training presets

    """

    PRESET_1 = 0
    """Preset 1"""

    PRESET_2 = 1
    """Preset 2"""

    PRESET_3 = 2
    """Preset 3"""

    PRESET_4 = 3
    """Preset 4"""

    PRESET_5 = 4
    """Preset 5"""

    UNKNOWN = 255
    """Unknown coeff"""


class LinkTrainCoeffs(IntEnum):
    """
    .. versionadded:: 1.1


    Link Training coefficients

    """

    PRE = 0
    """Pre coeff c(-1)"""

    MAIN = 1
    """Main coeff c(0)"""

    POST = 2
    """Post coeff c(1)"""

    PRE2 = 3
    """Pre2 coeff c(-2)"""

    PRE3 = 4
    """Pre3 coeff c(-3)"""

    UNKNOWN = 255
    """Unknown coeff"""


class LinkTrainEncoding(IntEnum):
    """
    .. versionadded:: 1.1

    Link Training Encoding

    """

    NRZ = 0
    """NRZ (PAM2)"""

    PAM4 = 1
    """PAM4"""

    PAM4_WITH_PRECODING = 2
    """PAM4 with precoding"""

    UNKNOWN = 255
    """PAM4 with precoding"""


class LinkTrainCmdResults(IntEnum):
    """
    .. versionadded:: 1.1

    Link Training Command Results

    """

    UNKNOWN = 0x00 | 0
    """Unknown result"""

    SUCCESS = 0x00 | 1
    """Command successfully completed"""

    TIMEOUT = 0x00 | 2
    """Command timeout"""

    FAILED = 0x00 | 3
    """Command failed"""

    COEFF_STS_NOT_UPDATED = 0x80 | 0
    """Coeff did not update"""

    COEFF_STS_UPDATED = 0x80 | 1
    """Coeff updated"""

    COEFF_STS_AT_LIMIT = 0x80 | 2
    """Coeff at limit"""

    COEFF_STS_NOT_SUPPORTED = 0x80 | 3
    """Coeff not supported"""

    COEFF_STS_EQ_LIMIT = 0x80 | 4
    """EQ limit reached"""

    COEFF_STS_C_AND_EQ_LIMIT = 0x80 | 6
    """Coeff and EQ limit reached"""


class LinkTrainCmdFlags(IntEnum):
    """
    .. versionadded:: 1.1

    Link Training Command Flags

    """

    NEW = 1
    """New command"""

    IN_PROGRESS = 2
    """Command in progress"""

    DONE = 4
    """Command done"""

    LOCK = 8
    """Link locked"""

    LOCK_LOST = 16
    """Link lock lost"""

    OVERRUN = 32
    """Overrun detected"""


class LinkTrainAnnounce(IntEnum):
    """
    .. versionadded:: 1.1

    Link Training Announce

    """

    TRAINED = 0
    """The lane is trained"""


class AnLtLogControl(IntEnum):
    """
    .. versionadded:: 1.3

    ANLT log control bits

    """

    # 1st nibble
    LOG_TYPE_DEBUG = 0x2
    """debug log output"""

    LOG_TYPE_AN_TRACE = 0x4
    """autonegotiation trace output"""

    LOG_TYPE_LT_TRACE = 0x8
    """link training trace output"""

    # 2nd nibble
    LOG_TYPE_ALG_TRACE = 0x10
    """link training algorithm trace"""

    # 5th nibble
    LOG_TYPE_FSM_PORT = 0x10000
    """port state machine transitions"""

    LOG_TYPE_FSM_ANEG = 0x20000
    """autonegotiation state machine transitions. What we act on"""

    LOG_TYPE_FSM_ANEG_STIMULI = 0x40000
    """autonegotiation stimuli state machine transitions. What we ask"""

    LOG_TYPE_FSM_LT = 0x80000
    """link training state machine transitions"""

    # 6th nibble
    LOG_TYPE_FSM_LT_COEFF = 0x100000
    """link training coefficient state machine transitions. What we act on"""

    LOG_TYPE_FSM_LT_STIMULI = 0x200000
    """link training stimuli state machine transitions. What we ask"""

    LOG_TYPE_FSM_LT_ALG0 = 0x400000
    """link training algorithm 0 state machine transitions"""

    LOG_TYPE_FSM_LT_ALG1 = 0x800000
    """link training algorithm -1 state machine transitions"""


class RxEqExtCap(IntEnum):
    """Rx Equalizer Advanced Capability type."""

    CTLE_LOW = 0
    """CTLE low frequency."""

    CTLE_HIGH = 1
    """CTLE high frequency."""

    AGC = 2
    """Automatic Gain Control"""

    OC = 3
    """Offset Cancellation"""

    CDR = 4
    """Clock and Data Recovery"""

    PRE_FFE_1 = 5
    """Pre Feed-Forward Equalizer #1"""

    PRE_FFE_2 = 6
    """Pre Feed-Forward Equalizer #2"""

    PRE_FFE_3 = 7
    """Pre Feed-Forward Equalizer #3"""

    PRE_FFE_4 = 8
    """Pre Feed-Forward Equalizer #4"""

    PRE_FFE_5 = 9
    """Pre Feed-Forward Equalizer #5"""

    PRE_FFE_6 = 10
    """Pre Feed-Forward Equalizer #6"""

    PRE_FFE_7 = 11
    """Pre Feed-Forward Equalizer #7"""

    PRE_FFE_8 = 12
    """Pre Feed-Forward Equalizer #8"""

    DFE = 13
    """Decision Feedback Equalization"""

    POST_FFE_1 = 14
    """Post Feed-Forward Equalizer #1"""

    POST_FFE_2 = 15
    """Post Feed-Forward Equalizer #2"""

    POST_FFE_3 = 16
    """Post Feed-Forward Equalizer #3"""

    POST_FFE_4 = 17
    """Post Feed-Forward Equalizer #4"""

    POST_FFE_5 = 18
    """Post Feed-Forward Equalizer #5"""

    POST_FFE_6 = 19
    """Post Feed-Forward Equalizer #6"""

    POST_FFE_7 = 20
    """Post Feed-Forward Equalizer #7"""

    POST_FFE_8 = 21
    """Post Feed-Forward Equalizer #8"""

    POST_FFE_9 = 22
    """Post Feed-Forward Equalizer #9"""

    POST_FFE_10 = 23
    """Post Feed-Forward Equalizer #10"""

    POST_FFE_11 = 24
    """Post Feed-Forward Equalizer #11"""

    POST_FFE_12 = 25
    """Post Feed-Forward Equalizer #12"""

    POST_FFE_13 = 26
    """Post Feed-Forward Equalizer #13"""

    POST_FFE_14 = 27
    """Post Feed-Forward Equalizer #14"""

    POST_FFE_15 = 28
    """Post Feed-Forward Equalizer #15"""

    POST_FFE_16 = 29
    """Post Feed-Forward Equalizer #16"""

    POST_FFE_17 = 30
    """Post Feed-Forward Equalizer #17"""

    POST_FFE_18 = 31
    """Post Feed-Forward Equalizer #18"""

    POST_FFE_19 = 32
    """Post Feed-Forward Equalizer #19"""

    POST_FFE_20 = 33
    """Post Feed-Forward Equalizer #20"""

    POST_FFE_21 = 34
    """Post Feed-Forward Equalizer #21"""

    POST_FFE_22 = 35
    """Post Feed-Forward Equalizer #22"""

    POST_FFE_23 = 36
    """Post Feed-Forward Equalizer #23"""


class RxEqExtCapMode(IntEnum):
    """Status for Rx Equalizer Advanced Capability."""

    AUTO = 0
    """Auto."""

    MANUAL = 1
    """Manual."""

    FREEZE = 2
    """Freeze."""

class PreCodingMode(IntEnum):
    """Rx/Tx Pre-Coding Mode."""
    
    OFF = 0
    """Off"""
    
    ON = 1
    """On"""
    
    AUTO = 2
    """Auto"""

class GrayCodingMode(IntEnum):
    """Rx/Tx Gray-Coding Mode."""
    
    OFF = 0
    """Off"""
    
    ON = 1
    """On"""


class Endianness(IntEnum):
    """Endianness (Big/Little Endian)."""
    
    NORMAL = 0
    """Big Endian"""
    
    REVERTED = 1
    """Little Endian"""

class FreyaAutonegMode(IntEnum):
    """Auto Neg Mode"""

    DISABLED = 0
    """Auto Neg Off"""
    ENABLED = 1
    """Auto Neg On"""

class FreyaLinkTrainingMode(IntEnum):
    """Link Training Mode"""

    DISABLED = 0
    """Link training disabled"""

    ENABLED_AUTO = 1
    """Link training in auto mode"""

    ENABLED_INTERACTIVE = 2
    """Link training in interactive mode, requiring manual operation."""

class FreyaTecAbility(IntFlag):
    """Auto Neg Technical Abilities"""

    ETC_800G_CR8_KR8 = 1<<29
    """ETC_800G_CR8_KR8"""
    
    ETC_400G_CR8_KR8 = 1<<28
    """ETC_400G_CR8_KR8"""

    ETC_50G_CR2 = 1<<27
    """ETC_50G_CR2"""

    ETC_50G_KR2 = 1<<26
    """ETC_50G_KR2"""

    ETC_25G_CR = 1<<25
    """ETC_25G_CR"""

    ETC_25G_KR = 1<<24
    """ETC_25G_KR"""

    IEEE_1_6TBASE_CR8_KR8 = 1<<23
    """IEEE_1_6TBASE_CR8_KR8"""

    IEEE_800GBASE_CR4_KR4 = 1<<22
    """IEEE_800GBASE_CR4_KR4"""

    IEEE_400GBASE_CR2_KR2 = 1<<21
    """IEEE_400GBASE_CR2_KR2"""

    IEEE_200GBASE_CR1_KR1 = 1<<20
    """IEEE_200GBASE_CR1_KR1"""

    IEEE_800GBASE_CR8_KR8 = 1<<19
    """IEEE_800GBASE_CR8_KR8"""

    IEEE_400GBASE_CR4_KR4 = 1<<18
    """IEEE_400GBASE_CR4_KR4"""

    IEEE_200GBASE_CR2_KR2 = 1<<17
    """IEEE_200GBASE_CR2_KR2"""

    IEEE_100GBASE_CR1_KR1 = 1<<16
    """IEEE_100GBASE_CR1_KR1"""

    IEEE_200GBASE_CR4_KR4 = 1<<15
    """IEEE_200GBASE_CR4_KR4"""

    IEEE_100GBASE_CR2_KR2 = 1<<14
    """IEEE_100GBASE_CR2_KR2"""

    IEEE_50GBASE_CR_KR = 1<<13
    """IEEE_50GBASE_CR_KR"""

    IEEE_5GBASE_KR = 1<<12
    """IEEE_5GBASE_KR"""

    IEEE_2_5GBASE_KX = 1<<11
    """IEEE_2_5GBASE_KX"""

    IEEE_25GBASE_CR_KR = 1<<10
    """IEEE_25GBASE_CR_KR"""

    IEEE_25GBASE_CR_S_KR_S = 1<<9
    """IEEE_25GBASE_CR_S_KR_S"""

    IEEE_100GBASE_CR4 = 1<<8
    """IEEE_100GBASE_CR4"""

    IEEE_100GBASE_KR4 = 1<<7
    """IEEE_100GBASE_KR4"""

    IEEE_100GBASE_KP4 = 1<<6
    """IEEE_100GBASE_KP4"""

    IEEE_100GBASE_CR10 = 1<<5
    """IEEE_100GBASE_CR10"""

    IEEE_40GBASE_CR4 = 1<<4
    """IEEE_40GBASE_CR4"""

    IEEE_40GBASE_KR4 = 1<<3
    """IEEE_40GBASE_KR4"""

    IEEE_10GBASE_KR = 1<<2
    """IEEE_10GBASE_KR"""

    IEEE_10GBASE_KX4 = 1<<1
    """IEEE_10GBASE_KX4"""

    IEEE_1000BASE_KX = 1<<0
    """IEEE_1000BASE_KX"""

class FreyaFECAbility(IntFlag):
    """Auto Neg FEC ability"""

    RS_FEC_Int = 1<<4
    """RS_FEC_Int"""

    FC_FEC_25G_REQUEST = 1<<3
    """FC_FEC_25G_REQUEST"""

    RS_FEC_25G_REQUEST = 1<<2
    """RS_FEC_25G_REQUEST"""

    FC_FEC_10G_REQUEST = 1<<1
    """FC_FEC_10G_REQUEST"""

    FC_FEC_10G_ABILITY = 1<<0
    """FC_FEC_10G_ABILITY"""

class FreyaPauseAbility(IntFlag):
    """Auto Neg Pause ability"""

    ASYM_PAUSE = 1<<1
    """ASYM_PAUSE"""

    SYM_PAUSE = 1<<0
    """SYM_PAUSE"""

class FreyaTechAbilityHCDStatus(IntEnum):
    """Auto Neg Pause ability"""

    SUCCESS = 1
    """SUCCESS"""

    FAILED = 2
    """FAILED"""

class FreyaOutOfSyncPreset(IntEnum):
    """Link Training out-of-sync preset"""

    IEEE = 0
    """IEEE"""

    CURRENT = 1
    """CURRENT"""

class Layer1Control(IntEnum):
    """Layer 1 control"""

    SAMPLED_SIGNAL_INTEGRITY_SCAN = 0
    """SAMPLED_SIGNAL_INTEGRITY_SCAN"""


class Layer1Opcode(IntEnum):
    """Layer 1 operation code"""

    START_SCAN = 0
    """ for sampled eye scan"""

class FreyaPCSVariant(IntEnum):
    """PCS variant"""

    IEEE = 1
    """IEEE"""

    ETC = 2
    """ETC"""

class FreyaTecAbilityHCD(IntEnum):
    """Auto Neg Technical Abilities"""

    ETC_800G_CR8_KR8 = 29
    """ETC_800G_CR8_KR8"""
    
    ETC_400G_CR8_KR8 = 28
    """ETC_400G_CR8_KR8"""

    ETC_50G_CR2 = 27
    """ETC_50G_CR2"""

    ETC_50G_KR2 = 26
    """ETC_50G_KR2"""

    ETC_25G_CR = 25
    """ETC_25G_CR"""

    ETC_25G_KR = 24
    """ETC_25G_KR"""

    IEEE_1_6TBASE_CR8_KR8 = 23
    """IEEE_1_6TBASE_CR8_KR8"""

    IEEE_800GBASE_CR4_KR4 = 22
    """IEEE_800GBASE_CR4_KR4"""

    IEEE_400GBASE_CR2_KR2 = 21
    """IEEE_400GBASE_CR2_KR2"""

    IEEE_200GBASE_CR1_KR1 = 20
    """IEEE_200GBASE_CR1_KR1"""

    IEEE_800GBASE_CR8_KR8 = 19
    """IEEE_800GBASE_CR8_KR8"""

    IEEE_400GBASE_CR4_KR4 = 18
    """IEEE_400GBASE_CR4_KR4"""

    IEEE_200GBASE_CR2_KR2 = 17
    """IEEE_200GBASE_CR2_KR2"""

    IEEE_100GBASE_CR1_KR1 = 16
    """IEEE_100GBASE_CR1_KR1"""

    IEEE_200GBASE_CR4_KR4 = 15
    """IEEE_200GBASE_CR4_KR4"""

    IEEE_100GBASE_CR2_KR2 = 14
    """IEEE_100GBASE_CR2_KR2"""

    IEEE_50GBASE_CR_KR = 13
    """IEEE_50GBASE_CR_KR"""

    IEEE_5GBASE_KR = 12
    """IEEE_5GBASE_KR"""

    IEEE_2_5GBASE_KX = 11
    """IEEE_2_5GBASE_KX"""

    IEEE_25GBASE_CR_KR = 10
    """IEEE_25GBASE_CR_KR"""

    IEEE_25GBASE_CR_S_KR_S = 9
    """IEEE_25GBASE_CR_S_KR_S"""

    IEEE_100GBASE_CR4 = 8
    """IEEE_100GBASE_CR4"""

    IEEE_100GBASE_KR4 = 7
    """IEEE_100GBASE_KR4"""

    IEEE_100GBASE_KP4 = 6
    """IEEE_100GBASE_KP4"""

    IEEE_100GBASE_CR10 = 5
    """IEEE_100GBASE_CR10"""

    IEEE_40GBASE_CR4 = 4
    """IEEE_40GBASE_CR4"""

    IEEE_40GBASE_KR4 = 3
    """IEEE_40GBASE_KR4"""

    IEEE_10GBASE_KR = 2
    """IEEE_10GBASE_KR"""

    IEEE_10GBASE_KX4 = 1
    """IEEE_10GBASE_KX4"""

    IEEE_1000BASE_KX = 0
    """IEEE_1000BASE_KX"""

# endregion

# region misc enums
class DhcpState(IntEnum):
    DHCP_STATE_UNKNOWN = 0
    DHCP_STATE_RUNNING = 1
    DHCP_STATE_COMPLETED = 2
    DHCP_STATE_FAILED = 3
    
class DhcpVlanState(IntEnum):
    DHCP_VLAN_OFF = 0
    DHCP_VLAN_ON  = 1

class VlanType(IntEnum):
    TYPE_C = 0
    TYPE_S  = 1
    
class ChassisModelNumber(IntEnum):
    NA      = 0
    XB1     = 1
    XB2     = 2
    XB3     = 3
    XB4     = 4
    XB5     = 5
    XB6     = 6
    XB7     = 7
    XB8     = 8
    XB9     = 9
    XB10    = 10
    XB10_5  = 11
    XB11    = 12
    XB12    = 13
    XB13    = 14
    XB14    = 15
    XB15    = 16
    XB16    = 17
    XB17    = 18
    XB18    = 19
    XB19    = 20
    XB20    = 21
    XB21    = 22
    XB22    = 23
    XB23    = 24
    XB33    = 25
    XC1     = 26
    XC2     = 27
    XC3     = 28
    XC4     = 29
    XC5     = 30
    XC6     = 31
    XC7     = 32
    XC8     = 33
    XC9     = 34
    XC10    = 35
    XC11    = 36
    XC12    = 37
    XC13    = 38
    XC14    = 39
    XC15    = 40
    XC16    = 41
    XC17    = 42
    XC18    = 43
    XC19    = 44
    XC20    = 45
    XC21    = 46
    XC22    = 47
    XC23    = 48
    XC24    = 49
    XC25    = 50
    XC26    = 51
    
class ChassisModelName(IntEnum):
    NA                  = 0
    B720                = 1
    B720D               = 2
    B2400               = 3
    Z_01_T_C_ODIN       = 4
    Z_100_Q_C_LOKI      = 5
    Z_10_S_C_ODIN       = 6
    Z_10_C_C_ODIN       = 7
    Z_10_R_C_ODIN       = 8
    Z_10_S_X_C_ODIN     = 9
    Z_01_S_C_ODIN       = 10
    Z_01_S_X_C_ODIN     = 11
    Z_400_Q_C_THOR      = 12
    Z_400_Q_LE_C_THOR   = 13
    Z_800_Q_C_FREYA     = 14
    Z_800_O_C_FREYA     = 15
    Z_800_Q_A_C_FREYA   = 16
    Z_800_O_A_C_FREYA   = 17
    E_100_Q_C_CHIMERA   = 18

class ModuleModelName(IntEnum):
    NA              = 0
    Z_01_T_ODIN     = 1
    Z_100_Q_LOKI    = 2
    Z_10_S_ODIN     = 3
    Z_10_R_ODIN     = 4
    Z_10_S_X_ODIN   = 5
    Z_01_S_ODIN     = 6
    Z_01_S_X_ODIN   = 7
    Z_400_Q_THOR    = 8
    Z_400_Q_LE_THOR = 9
    Z_800_Q_FREYA   = 10
    Z_800_O_FREYA   = 11
    E_100_Q_CHIMERA = 12
    
# endregion

# region FEC CW enums

class FecCodewordBitErrorMaskMode(IntEnum):
    """FEC Codeword Bit Error Mask Mode"""

    UNKNOWN = 0
    """Unknown"""
    STATIC = 1
    """The bit error pattern stay the same for all errored symbols."""
    ROTATE_HIGH = 2
    """The bit error pattern shifts one bit to the most significant bit per errored symbol."""
    INC = 3
    """When mode is set to INC, bitmask will be ignored. Instead, the bit error pattern initiates from 000000001, 000000010, 000000011, continuing up to 111111111, and repeating the sequence as 000000001..."""

# endregion