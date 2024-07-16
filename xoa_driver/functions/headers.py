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
class Ethernet:

    def __init__(self):
        self.dst_mac: str = "0000.0000.0000"
        self.src_mac: str = "0000.0000.0000"
        self.ethertype: EtherType = EtherType.NONE
    
    def __str__(self):
        _dst_mac: str = self.dst_mac.replace(".", "")
        _src_mac: str = self.src_mac.replace(".", "")
        _ethertype: str = '{:04X}'.format(self.ethertype.value)
        return f"{_dst_mac}{_src_mac}{_ethertype}".upper()
    
####################################
#           VLAN               #
####################################
class VLAN:
    def __init__(self):
        self.pri: int = 0
        self.dei: int = 0
        self.id: int = 0
        self.type: EtherType = EtherType.NONE
    
    def __str__(self):
        _pri_dei: str = '{:01X}'.format((self.pri<<1)+self.dei)
        _id: str = '{:03X}'.format(self.id)
        _type: str = '{:04X}'.format(self.type.value)
        return f"{_pri_dei}{_id}{_type}".upper()
    

####################################
#           ARP                    #
####################################
class ARP:
    def __init__(self):
        self.hardware_type: ARPHardwareType = ARPHardwareType.Ethernet
        self.protocol_type: EtherType = EtherType.IPv4
        self.hardware_size: int = 6
        self.protocol_size: int = 4
        self.opcode: ARPOpcode = ARPOpcode.Request
        self.sender_mac: str = "0000.0000.0000"
        self.sender_ip: str = "0.0.0.0"
        self.target_mac: str = "0000.0000.0000"
        self.target_ip: str = "0.0.0.0"
    
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
class IPV4:
    def __init__(self):
        self.version: int = 4
        self.header_length: int = 5
        self.dscp: int = 0
        self.ecn: int = 0
        self.total_length: int = 0
        self.identification: str = "0000"
        self.flags: int = 0
        self.offset: int = 0
        self.ttl: int = 255
        self.proto: IPProtocol = IPProtocol.NONE
        self.checksum: str = "0000"
        self.src: str = "0.0.0.0"
        self.dst: str = "0.0.0.0"

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
class IPV6:
    def __init__(self):
        self.version: int = 6
        self.traff_class: int = 8
        self.flow_label: int = 0
        self.payload_length: int = 0
        self.next_header: IPProtocol = IPProtocol.NONE
        self.hop_limit: int = 1
        self.src: str = "2000::2"
        self.dst: str = "2000::100"

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
class UDP:
    def __init__(self):
        self.src_port: int = 0
        self.dst_port: int = 0
        self.length: int = 8
        self.checksum = "0000"

    def __str__(self):
        _src_port: str = '{:04X}'.format(self.src_port)
        _dst_port: str = '{:04X}'.format(self.dst_port)
        _length: str = '{:04X}'.format(self.length)
        _checksum: str = self.checksum
        return f"{_src_port}{_dst_port}{_length}{_checksum}".upper()

####################################
#           TCP                    #
####################################
class TCP:
    def __init__(self):
        self.src_port: int = 0
        self.dst_port: int = 0
        self.seq_num: int = 0
        self.ack_num: int = 0
        self.header_length: int = 20
        """Aka. Data Offset (bytes)"""
        self.rsrvd: int = 0
        """Reserved 000"""
        self.ae: int = 0
        """Accurate ECN"""
        self.cwr: int = 0
        """Congestion Window Reduced"""
        self.ece: int = 0
        """ECN-Echo"""
        self.urg: int = 0
        """Urgent"""
        self.ack: int = 0
        """Acknowledgment"""
        self.psh: int = 0
        """Push"""
        self.rst: int = 0
        """Rest"""
        self.syn: int = 0
        """Sync"""
        self.fin: int = 0
        """Fin"""
        self.window: int = 0
        self.checksum: str = "0000"
        self.urgent_pointer: int = 0

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
class PTP:
    def __init__(self):
        self.version_ptp: int = 1
        self.version_network: int = 1
        self.subdomain: str = "5f44464c540000000000000000000000"
        self.message_type: int = 1
        self.source_comm_tech: int = 1
        self.source_uuid: str = "0030051d1e27"
        self.source_port_id: int = 1
        self.seq_id: int = 94
        self.control_field: int = 0
        self.flags: str = "0008"
        self.original_timestamp_sec: int = 1163594296
        self.original_timestamp_nsec: int = 247015000
        self.epoch_num: int = 0
        self.current_utc_offset: int = 0
        self.gm_comm_tech: int = 1
        self.gm_clock_uuid: str = "0030051d1e27"
        self.gm_port_id: int = 0
        self.gm_seq_id: int = 94
        self.gm_clock_stratum: int = 4
        self.gm_clock_id: str = "44464c54"
        self.gm_clock_variance: int = -4000
        self.gm_preferred: int = 0
        self.gm_is_boundary_clock: int = 0
        self.sync_interval: int = 1
        self.local_clock_variance: int = -4000
        self.local_step_removed: int = 0
        self.local_clock_stratum: int = 4
        self.local_clock_id: str = "44464c54"
        self.parent_comm_tech: int = 1
        self.parent_clock_uuid: str = "0030051D1E27"
        self.parent_port_id: int = 0
        self.est_master_variance: int = 0
        self.est_master_drift: int = 0
        self.utc_reasonable: int = 1

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
class eCPRIGeneralDataTransfer:
    def __init__(self):
        self.protocol_rev: int = 1
        self.c_bit: int = 0
        self.message_type: str = "03"
        self.payload_size = 24
        self.pc_id: str= "12345678"
        self.seq_id: str = "87654321"
        self.user_data: str = "0f0e0d0c0b0a09080706050403020100"

    def __str__(self):
        _tmp: str = '{:02X}'.format((self.protocol_rev<<4)+self.c_bit)
        _message_type: str = self.message_type
        _payload_size: str = '{:04X}'.format(self.payload_size)
        _pc_id: str = self.pc_id
        _seq_id: str = self.seq_id
        _user_data: str = self.user_data
        return f"{_tmp}{_message_type}{_payload_size}{_pc_id}{_seq_id}{_user_data}".upper()