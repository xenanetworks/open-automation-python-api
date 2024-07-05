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

####################################
#           Ethernet               #
####################################
class Ethernet:
    def __init__(self):
        self.dst_mac = "0000.0000.0000"
        self.src_mac = "0000.0000.0000"
        self.ethertype = "FFFF"
    
    def __str__(self):
        _dst_mac = self.dst_mac.replace(".", "")
        _src_mac = self.src_mac.replace(".", "")
        _ethertype = self.ethertype
        return f"{_dst_mac}{_src_mac}{_ethertype}".upper()
    
####################################
#           VLAN               #
####################################
class VLAN:
    def __init__(self):
        self.pri = 0
        self.dei = 0
        self.id = 0
        self.type = "FFFF"
    
    def __str__(self):
        _pri_dei = '{:01X}'.format((self.pri<<1)+self.dei)
        _id = '{:03X}'.format(self.id)
        _type = self.type
        return f"{_pri_dei}{_id}{_type}".upper()
    

####################################
#           ARP                    #
####################################
class ARP:
    def __init__(self):
        self.hardware_type: str = "0001"
        self.protocol_type: str = "0800"
        self.hardware_size: str = "06"
        self.protocol_size: str = "04"
        self.opcode: str = "0001"
        self.sender_mac = "0000.0000.0000"
        self.sender_ip = "0.0.0.0"
        self.target_mac = "0000.0000.0000"
        self.target_ip = "0.0.0.0"
    
    def __str__(self):
        _hardware_type = self.hardware_type
        _protocol_type = self.protocol_type
        _hardware_size = self.hardware_size
        _protocol_size = self.protocol_size
        _sender_mac = self.sender_mac.replace(".", "")
        _sender_ip = hexlify(IPv4Address(self.sender_ip).packed).decode()
        _target_mac = self.target_mac.replace(".", "")
        _target_ip = hexlify(IPv4Address(self.target_ip).packed).decode()
        return f"{_hardware_type}{_protocol_type}{_hardware_size}{_protocol_size}{_sender_mac}{_sender_ip}{_target_mac}{_target_ip}".upper()

####################################
#           IPv4                   #
####################################
class IPV4:
    def __init__(self):
        self.version = 4
        self.header_length = 5
        self.dscp = 0
        self.ecn = 0
        self.total_length = 42
        self.identification = "0000"
        self.flags = 0
        self.offset = 0
        self.ttl = 255
        self.proto = 255
        self.checksum = "0000"
        self.src = "0.0.0.0"
        self.dst = "0.0.0.0"

    def __str__(self):
        _ver = '{:01X}'.format(self.version)
        _header_length = '{:01X}'.format(self.header_length)
        _dscp_ecn = '{:02X}'.format((self.dscp<<2)+self.ecn)
        _total_len = '{:04X}'.format(self.total_length)
        _ident = self.identification
        _flag_offset = '{:04X}'.format((self.flags<<13)+self.offset)
        _ttl = '{:02X}'.format(self.ttl)
        _proto = '{:02X}'.format(self.proto)
        _check = self.checksum
        _src = hexlify(IPv4Address(self.src).packed).decode()
        _dst = hexlify(IPv4Address(self.dst).packed).decode()
        return f"{_ver}{_header_length}{_dscp_ecn}{_total_len}{_ident}{_flag_offset}{_ttl}{_proto}{_check}{_src}{_dst}".upper()

####################################
#           IPv6                   #
####################################
class IPV6:
    def __init__(self):
        self.version = 6
        self.traff_class = 8
        self.flow_label = 0
        self.payload_length = 0
        self.next_header = "11"
        self.hop_limit = 1
        self.src = "2000::2"
        self.dst = "2000::100"

    def __str__(self):
        _ver = '{:01X}'.format(self.version)
        _traff_class = '{:01X}'.format(self.traff_class)
        _flow_label = '{:06X}'.format(self.flow_label)
        _payload_len = '{:04X}'.format(self.payload_length)
        _next_header = self.next_header
        _hop_limit = '{:02X}'.format(self.hop_limit)
        _src = hexlify(IPv6Address(self.src).packed).decode()
        _dst = hexlify(IPv6Address(self.dst).packed).decode()
        return f"{_ver}{_traff_class}{_flow_label}{_payload_len}{_next_header}{_hop_limit}{_src}{_dst}".upper()

####################################
#           UDP                    #
####################################
class UDP:
    def __init__(self):
        self.src_port = 0
        self.dst_port = 0
        self.length = 0
        self.checksum = 0

    def __str__(self):
        _src_port = '{:04X}'.format(self.src_port)
        _dst_port = '{:04X}'.format(self.dst_port)
        _length = '{:04X}'.format(self.length)
        _checksum = '{:04X}'.format(self.checksum)
        return f"{_src_port}{_dst_port}{_length}{_checksum}".upper()

####################################
#           TCP                    #
####################################
class TCP:
    def __init__(self):
        self.src_port = 0
        self.dst_port = 0
        self.seq_num = 0
        self.ack_num = 0
        self.header_length = 20
        """Aka. Data Offset (bytes)"""
        self.RSRVD = 0
        """Reserved 000"""
        self.ae = 0
        """Accurate ECN"""
        self.cwr = 0
        """Congestion Window Reduced"""
        self.ece = 0
        """ECN-Echo"""
        self.urg = 0
        """Urgent"""
        self.ack = 0
        """Acknowledgment"""
        self.psh = 0
        """Push"""
        self.rst = 0
        """Rest"""
        self.syn = 0
        """Sync"""
        self.fin = 0
        """Fin"""
        self.window = 0
        self.checksum = 0
        self.urgent_pointer = 0

    def __str__(self):
        _src_port = '{:04X}'.format(self.src_port)
        _dst_port = '{:04X}'.format(self.dst_port)
        _seq_num = '{:08X}'.format(self.seq_num)
        _ack_num = '{:08X}'.format(self.ack_num)
        if self.header_length % 4 != 0:
            raise Exception("Header Length field (bytes) must be multiple of 4")
        _header_length = '{:01X}'.format(int(self.header_length/4))
        _flags = 0
        _flags += (self.RSRVD<<9)
        _flags += (self.ae<<8)
        _flags += (self.cwr<<7)
        _flags += (self.ece<<6)
        _flags += (self.urg<<5)
        _flags += (self.ack<<4)
        _flags += (self.psh<<3)
        _flags += (self.rst<<2)
        _flags += (self.syn<<1)
        _flags += (self.fin<<0)
        _flags = '{:03X}'.format(_flags)
        _window = '{:04X}'.format(self.window)
        _checksum = '{:04X}'.format(self.checksum)
        _urgent_pointer = '{:04X}'.format(self.urgent_pointer)

        return f"{_src_port}{_dst_port}{_seq_num}{_ack_num}{_header_length}{_flags}{_window}{_checksum}{_urgent_pointer}".upper()
    
####################################
#           PTP                    #
####################################
class PTP:
    def __init__(self):
        self.version_ptp = 1
        self.version_network = 1
        self.subdomain = "5F44464c540000000000000000000000"
        self.message_type = 1
        self.source_comm_tech = 1
        self.source_uuid = "0030051D1E27"
        self.source_port_id = 1
        self.seq_id = 94
        self.control_field = 0
        self.flags = "0008"
        self.original_timestamp_sec = 1163594296
        self.original_timestamp_nsec = 247015000
        self.epoch_num = 0
        self.current_utc_offset = 0
        self.gm_comm_tech = 1
        self.gm_clock_uuid = "0030051D1E27"
        self.gm_port_id = 0
        self.gm_seq_id = 94
        self.gm_clock_stratum = 4
        self.gm_clock_id = "44464c54"
        self.gm_clock_variance = -4000
        self.gm_preferred = 0
        self.gm_is_boundary_clock = 0
        self.sync_interval = 1
        self.local_clock_variance = -4000
        self.local_step_removed = 0
        self.local_clock_stratum = 4
        self.local_clock_id = "44464c54"
        self.parent_comm_tech = 1
        self.parent_clock_uuid = "0030051D1E27"
        self.parent_port_id = 0
        self.est_master_variance = 0
        self.est_master_drift = 0
        self.utc_reasonable = 0

    def __str__(self):
        _version_ptp = '{:04X}'.format(self.version_ptp)
        _version_network = '{:04X}'.format(self.version_network)
        _subdomain = self.subdomain
        _message_type = '{:02X}'.format(self.message_type)
        _source_comm_tech = '{:02X}'.format(self.source_comm_tech)
        _source_uuid = self.source_uuid
        _source_port_id = '{:04X}'.format(self.source_port_id)
        _sequence_id = '{:04X}'.format(self.seq_id)
        _control_field = '{:02X}'.format(self.control_field)
        _flags = self.flags
        _original_timestamp_sec = '{:08X}'.format(self.original_timestamp_sec)
        _original_timestamp_nsec = '{:08X}'.format(self.original_timestamp_nsec)
        _epoch_num = '{:04X}'.format(self.epoch_num)
        _current_utc_offset = '{:04X}'.format(self.current_utc_offset)
        _gm_comm_tech = '{:02X}'.format(self.gm_comm_tech)
        _gm_clock_uuid = self.gm_clock_uuid
        _gm_port_id = '{:04X}'.format(self.gm_port_id)
        _gm_seq_id = '{:04X}'.format(self.gm_seq_id)
        _gm_clock_stratum = '{:02X}'.format(self.gm_clock_stratum)
        _gm_clock_id = self.gm_clock_id
        _gm_clock_variance = '{:04X}'.format(self.gm_clock_variance & ((1 << 16)-1))
        _gm_preferred = '{:02X}'.format(self.gm_preferred)
        _gm_is_boundary_clock = '{:02X}'.format(self.gm_is_boundary_clock)
        _sync_interval = '{:02X}'.format(self.sync_interval)
        _local_clock_variance = '{:04X}'.format(self.local_clock_variance & ((1 << 16)-1))
        _local_step_removed = '{:04X}'.format(self.local_step_removed & ((1 << 16)-1))
        _local_clock_stratum = '{:02X}'.format(self.local_clock_stratum)
        _local_clock_id = self.local_clock_id
        _parent_comm_tech = '{:02X}'.format(self.parent_comm_tech)
        _parent_clock_uuid = self.parent_clock_uuid
        _parent_port_id = '{:04X}'.format(self.parent_port_id)
        _est_master_variance = '{:04X}'.format(self.est_master_variance & ((1 << 16)-1))
        _est_master_drift = '{:08X}'.format(self.est_master_drift & ((1 << 16)-1))
        _utc_reasonable = '{:02X}'.format(self.utc_reasonable)

        return f"{_version_ptp}{_version_network}{_subdomain}{_message_type}{_source_comm_tech}{_source_uuid}{_source_port_id}{_sequence_id}{_control_field}00{_flags}00000000{_original_timestamp_sec}{_original_timestamp_nsec}{_epoch_num}{_current_utc_offset}00{_gm_comm_tech}{_gm_clock_uuid}{_gm_port_id}{_gm_seq_id}000000{_gm_clock_stratum}{_gm_clock_id}0000{_gm_clock_variance}00{_gm_preferred}00{_gm_is_boundary_clock}000000{_sync_interval}0000{_local_clock_variance}0000{_local_step_removed}000000{_local_clock_stratum}{_local_clock_id}00{_parent_comm_tech}{_parent_clock_uuid}0000{_parent_port_id}0000{_est_master_variance}{_est_master_drift}000000{_utc_reasonable}".upper()
    
####################################
#  eCPRI GeneralDataTransfer       #
####################################
class eCPRIGeneralDataTransfer:
    def __init__(self):
        self.protocol_rev = 1
        self.c_bit = 0
        self.message_type = "03"
        self.payload_size = 24
        self.pc_id = "12345678"
        self.seq_id = "87654321"
        self.user_data = "0f0e0d0c0b0a09080706050403020100"

    def __str__(self):
        _tmp = '{:02X}'.format((self.protocol_rev<<4)+self.c_bit)
        _message_type = self.message_type
        _payload_size = '{:04X}'.format(self.payload_size)
        _pc_id = self.pc_id
        _seq_id = self.seq_id
        _user_data = self.user_data
        return f"{_tmp}{_message_type}{_payload_size}{_pc_id}{_seq_id}{_user_data}".upper()