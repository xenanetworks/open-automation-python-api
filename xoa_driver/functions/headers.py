################################################################
#
#                   HEADER BUILDER
#
# This script shows you how you can build your own header builder 
# that converts human readable values into hex strings
#
################################################################

from ipaddress import IPv4Address, IPv6Address
from binascii import hexlify
from xoa_driver.misc import Hex
from enum import Enum
from dataclasses import dataclass

class EtherType(Enum):
    IPv4 = 0x0800
    IPv6 = 0x86DD
    VLAN = 0x8100
    QINQ_LEGACY = 0x9100
    QINQ = 0x88A8
    ARP = 0x0806
    MPLS = 0x8847
    eCPRI = 0xAEFE
    NONE = 0xFFFF

class IPProtocol(Enum):
    UDP = 17
    TCP = 6
    NONE = 255

class ARPOpcode(Enum):
    Request = 1
    Reply = 2

class ARPHardwareType(Enum):
    Ethernet = 1


####################################
#           Ethernet               #
####################################
@dataclass
class Ethernet:
    dst_mac: str = "0000.0000.0000"
    src_mac: str = "0000.0000.0000"
    ethertype: EtherType = EtherType.NONE
    
    def __str__(self):
        _dst_mac: str = self.dst_mac.replace(".", "")
        _src_mac: str = self.src_mac.replace(".", "")
        _ethertype: str = '{:04X}'.format(self.ethertype.value)
        return f"{_dst_mac}{_src_mac}{_ethertype}".upper()
    
####################################
#           VLAN               #
####################################

@dataclass
class VLAN:
    pri: int = 0
    dei: int = 0
    id: int = 0
    type: EtherType = EtherType.NONE
    
    def __str__(self):
        _pri_dei: str = '{:01X}'.format((self.pri<<1)+self.dei)
        _id: str = '{:03X}'.format(self.id)
        _type: str = '{:04X}'.format(self.type.value)
        return f"{_pri_dei}{_id}{_type}".upper()
    

####################################
#           ARP                    #
####################################
@dataclass
class ARP:
    hardware_type: ARPHardwareType = ARPHardwareType.Ethernet
    protocol_type: EtherType = EtherType.IPv4
    hardware_size: int = 6
    protocol_size: int = 4
    opcode: ARPOpcode = ARPOpcode.Request
    sender_mac: str = "0000.0000.0000"
    sender_ip: str = "0.0.0.0"
    target_mac: str = "0000.0000.0000"
    target_ip: str = "0.0.0.0"
    
    def __str__(self):
        _hardware_type: str = '{:04X}'.format(self.hardware_type.value)
        _protocol_type: str = '{:04X}'.format(self.protocol_type.value)
        _hardware_size: str = '{:02X}'.format(self.hardware_size)
        _protocol_size: str = '{:02X}'.format(self.protocol_size)
        _opcode: str = '{:04X}'.format(self.opcode.value)
        _sender_mac: str = self.sender_mac.replace(".", "")
        _sender_ip: str = hexlify(IPv4Address(self.sender_ip).packed).decode()
        _target_mac: str = self.target_mac.replace(".", "")
        _target_ip: str = hexlify(IPv4Address(self.target_ip).packed).decode()
        return f"{_hardware_type}{_protocol_type}{_hardware_size}{_protocol_size}{_opcode}{_sender_mac}{_sender_ip}{_target_mac}{_target_ip}".upper()

####################################
#           IPv4                   #
####################################
@dataclass
class IPV4:
    version: int = 4
    header_length: int = 5
    dscp: int = 0
    ecn: int = 0
    total_length: int = 0
    identification: str = "0000"
    flags: int = 0
    offset: int = 0
    ttl: int = 255
    proto: IPProtocol = IPProtocol.NONE
    checksum: str = "0000"
    src: str = "0.0.0.0"
    dst: str = "0.0.0.0"

    def __str__(self):
        _ver: str = '{:01X}'.format(self.version)
        _header_length: str = '{:01X}'.format(self.header_length)
        _dscp_ecn: str = '{:02X}'.format((self.dscp<<2)+self.ecn)
        _total_len: str = '{:04X}'.format(self.total_length)
        _ident: str = self.identification
        _flag_offset: str = '{:04X}'.format((self.flags<<13)+self.offset)
        _ttl: str = '{:02X}'.format(self.ttl)
        _proto: str = '{:02X}'.format(self.proto.value)
        _check: str = self.checksum
        _src: str = hexlify(IPv4Address(self.src).packed).decode()
        _dst: str = hexlify(IPv4Address(self.dst).packed).decode()
        return f"{_ver}{_header_length}{_dscp_ecn}{_total_len}{_ident}{_flag_offset}{_ttl}{_proto}{_check}{_src}{_dst}".upper()

####################################
#           IPv6                   #
####################################
@dataclass
class IPV6:
    version: int = 6
    traff_class: int = 8
    flow_label: int = 0
    payload_length: int = 0
    next_header: IPProtocol = IPProtocol.NONE
    hop_limit: int = 1
    src: str = "2000::2"
    dst: str = "2000::100"

    def __str__(self):
        _ver: str = '{:01X}'.format(self.version)
        _traff_class: str = '{:01X}'.format(self.traff_class)
        _flow_label: str = '{:06X}'.format(self.flow_label)
        _payload_len: str = '{:04X}'.format(self.payload_length)
        _next_header: str = '{:02X}'.format(self.next_header.value)
        _hop_limit: str = '{:02X}'.format(self.hop_limit)
        _src: str = hexlify(IPv6Address(self.src).packed).decode()
        _dst: str = hexlify(IPv6Address(self.dst).packed).decode()
        return f"{_ver}{_traff_class}{_flow_label}{_payload_len}{_next_header}{_hop_limit}{_src}{_dst}".upper()

####################################
#           UDP                    #
####################################
@dataclass
class UDP:
    src_port: int = 0
    dst_port: int = 0
    length: int = 8
    checksum = "0000"

    def __str__(self):
        _src_port: str = '{:04X}'.format(self.src_port)
        _dst_port: str = '{:04X}'.format(self.dst_port)
        _length: str = '{:04X}'.format(self.length)
        _checksum: str = self.checksum
        return f"{_src_port}{_dst_port}{_length}{_checksum}".upper()

####################################
#           TCP                    #
####################################
@dataclass
class TCP:
    src_port: int = 0
    dst_port: int = 0
    seq_num: int = 0
    ack_num: int = 0
    header_length: int = 20
    """Aka. Data Offset (bytes)"""
    rsrvd: int = 0
    """Reserved 000"""
    ae: int = 0
    """Accurate ECN"""
    cwr: int = 0
    """Congestion Window Reduced"""
    ece: int = 0
    """ECN-Echo"""
    urg: int = 0
    """Urgent"""
    ack: int = 0
    """Acknowledgment"""
    psh: int = 0
    """Push"""
    rst: int = 0
    """Rest"""
    syn: int = 0
    """Sync"""
    fin: int = 0
    """Fin"""
    window: int = 0
    checksum: str = "0000"
    urgent_pointer: int = 0

    def __str__(self):
        _src_port: str = '{:04X}'.format(self.src_port)
        _dst_port: str = '{:04X}'.format(self.dst_port)
        _seq_num: str = '{:08X}'.format(self.seq_num)
        _ack_num: str = '{:08X}'.format(self.ack_num)
        if self.header_length % 4 != 0:
            raise Exception("Header Length field (bytes) must be multiple of 4")
        _header_length: str = '{:01X}'.format(int(self.header_length/4))
        _flags: int = 0
        _flags += (self.rsrvd<<9)
        _flags += (self.ae<<8)
        _flags += (self.cwr<<7)
        _flags += (self.ece<<6)
        _flags += (self.urg<<5)
        _flags += (self.ack<<4)
        _flags += (self.psh<<3)
        _flags += (self.rst<<2)
        _flags += (self.syn<<1)
        _flags += (self.fin<<0)
        _flags_str: str = '{:03X}'.format(_flags)
        _window: str = '{:04X}'.format(self.window)
        _checksum: str = self.checksum
        _urgent_pointer: str = '{:04X}'.format(self.urgent_pointer)

        return f"{_src_port}{_dst_port}{_seq_num}{_ack_num}{_header_length}{_flags_str}{_window}{_checksum}{_urgent_pointer}".upper()
    
####################################
#           PTP                    #
####################################
@dataclass
class PTP:
    version_ptp: int = 1
    version_network: int = 1
    subdomain: str = "5f44464c540000000000000000000000"
    message_type: int = 1
    source_comm_tech: int = 1
    source_uuid: str = "0030051d1e27"
    source_port_id: int = 1
    seq_id: int = 94
    control_field: int = 0
    flags: str = "0008"
    original_timestamp_sec: int = 1163594296
    original_timestamp_nsec: int = 247015000
    epoch_num: int = 0
    current_utc_offset: int = 0
    gm_comm_tech: int = 1
    gm_clock_uuid: str = "0030051d1e27"
    gm_port_id: int = 0
    gm_seq_id: int = 94
    gm_clock_stratum: int = 4
    gm_clock_id: str = "44464c54"
    gm_clock_variance: int = -4000
    gm_preferred: int = 0
    gm_is_boundary_clock: int = 0
    sync_interval: int = 1
    local_clock_variance: int = -4000
    local_step_removed: int = 0
    local_clock_stratum: int = 4
    local_clock_id: str = "44464c54"
    parent_comm_tech: int = 1
    parent_clock_uuid: str = "0030051D1E27"
    parent_port_id: int = 0
    est_master_variance: int = 0
    est_master_drift: int = 0
    utc_reasonable: int = 1

    def __str__(self):
        _version_ptp: str = '{:04X}'.format(self.version_ptp)
        _version_network: str = '{:04X}'.format(self.version_network)
        _subdomain: str = self.subdomain
        _message_type: str = '{:02X}'.format(self.message_type)
        _source_comm_tech: str = '{:02X}'.format(self.source_comm_tech)
        _source_uuid: str = self.source_uuid
        _source_port_id: str = '{:04X}'.format(self.source_port_id)
        _sequence_id: str = '{:04X}'.format(self.seq_id)
        _control_field: str = '{:02X}'.format(self.control_field)
        _flags: str = self.flags
        _original_timestamp_sec: str = '{:016X}'.format(self.original_timestamp_sec)
        _original_timestamp_nsec: str = '{:016X}'.format(self.original_timestamp_nsec)
        _epoch_num: str = '{:04X}'.format(self.epoch_num)
        _current_utc_offset: str = '{:04X}'.format(self.current_utc_offset)
        _gm_comm_tech: str = '{:02X}'.format(self.gm_comm_tech)
        _gm_clock_uuid: str = self.gm_clock_uuid
        _gm_port_id: str = '{:04X}'.format(self.gm_port_id)
        _gm_seq_id: str = '{:04X}'.format(self.gm_seq_id)
        _gm_clock_stratum: str = '{:02X}'.format(self.gm_clock_stratum)
        _gm_clock_id: str = self.gm_clock_id
        _gm_clock_variance: str = '{:04X}'.format(self.gm_clock_variance & ((1 << 16)-1))
        _gm_preferred: str = '{:02X}'.format(self.gm_preferred)
        _gm_is_boundary_clock: str = '{:02X}'.format(self.gm_is_boundary_clock)
        _sync_interval: str = '{:02X}'.format(self.sync_interval)
        _local_clock_variance: str = '{:04X}'.format(self.local_clock_variance & ((1 << 16)-1))
        _local_step_removed: str = '{:04X}'.format(self.local_step_removed & ((1 << 16)-1))
        _local_clock_stratum: str = '{:02X}'.format(self.local_clock_stratum)
        _local_clock_id: str = self.local_clock_id
        _parent_comm_tech: str = '{:02X}'.format(self.parent_comm_tech)
        _parent_clock_uuid: str = self.parent_clock_uuid
        _parent_port_id: str = '{:04X}'.format(self.parent_port_id)
        _est_master_variance: str = '{:04X}'.format(self.est_master_variance & ((1 << 16)-1))
        _est_master_drift: str = '{:08X}'.format(self.est_master_drift & ((1 << 16)-1))
        _utc_reasonable: str = '{:02X}'.format(self.utc_reasonable)

        return f"{_version_ptp}{_version_network}{_subdomain}{_message_type}{_source_comm_tech}{_source_uuid}{_source_port_id}{_sequence_id}{_control_field}00{_flags}00000000{_original_timestamp_sec}{_original_timestamp_nsec}{_epoch_num}{_current_utc_offset}00{_gm_comm_tech}{_gm_clock_uuid}{_gm_port_id}{_gm_seq_id}000000{_gm_clock_stratum}{_gm_clock_id}0000{_gm_clock_variance}00{_gm_preferred}00{_gm_is_boundary_clock}000000{_sync_interval}0000{_local_clock_variance}0000{_local_step_removed}000000{_local_clock_stratum}{_local_clock_id}00{_parent_comm_tech}{_parent_clock_uuid}0000{_parent_port_id}0000{_est_master_variance}{_est_master_drift}000000{_utc_reasonable}".upper()
    
####################################
#  eCPRI GeneralDataTransfer       #
####################################
@dataclass
class eCPRIGeneralDataTransfer:
    protocol_rev: int = 1
    c_bit: int = 0
    message_type: str = "03"
    payload_size = 24
    pc_id: str= "12345678"
    seq_id: str = "87654321"
    user_data: str = "0f0e0d0c0b0a09080706050403020100"

    def __str__(self):
        _tmp: str = '{:02X}'.format((self.protocol_rev<<4)+self.c_bit)
        _message_type: str = self.message_type
        _payload_size: str = '{:04X}'.format(self.payload_size)
        _pc_id: str = self.pc_id
        _seq_id: str = self.seq_id
        _user_data: str = self.user_data
        return f"{_tmp}{_message_type}{_payload_size}{_pc_id}{_seq_id}{_user_data}".upper()