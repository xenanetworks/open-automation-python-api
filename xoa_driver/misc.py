#: Other types which are used by ports or as a parameter to attribute set method.


from .internals.core.token import Token
from .internals.core.transporter.protocol.payload.types import Hex
from .internals.commands.subtypes import (
    ArpChunk,
    NdpChunk,
    DhcpChunk,
    GroupAddressElem,
    VlanTag,
    QueueStatsElem,
)

import sys

if "xoa_driver.v2" in sys.modules:
    raise ImportError("\33[31mOnly Single interface version is allowed to being use at the same time.\33[0m")

# indices types
from .internals.hli_v1.indices.connection_group.cg import ConnectionGroupIdx as ConnectionGroup
from .internals.hli_v1.indices.filter.base_filter import BaseFilterIdx as BasePortFilter
from .internals.hli_v1.indices.filter.genuine_filter import GenuineFilterIdx as GenuinePortFilter
from .internals.hli_v1.indices.length_term import LengthTermIdx as LengthTerm
from .internals.hli_v1.indices.match_term import MatchTermIdx as MatchTerm
from .internals.hli_v1.indices.port_dataset import PortDatasetIdx as PortDataset
from .internals.hli_v1.indices.streams.base_stream import BaseStreamIdx as BaseStream
from .internals.hli_v1.indices.streams.genuine_stream import GenuineStreamIdx as GenuineStream
from .internals.hli_v1.ports.port_l23.chimera.port_emulation import CFlow as ImpairmentFlow
from .internals.hli_v1.ports.port_l23.chimera.filter_definition.general import ModeBasic as BasicImpairmentFlowFilter
from .internals.hli_v1.ports.port_l23.chimera.filter_definition.general import ModeExtended as ExtendedImpairmentFlowFilter


__all__ = (
    "Token",
    "Hex",
    "ArpChunk",
    "NdpChunk",
    "DhcpChunk",
    "GroupAddressElem",
    "VlanTag",
    "QueueStatsElem",
    "ConnectionGroup",
    "BasePortFilter",
    "GenuinePortFilter",
    "LengthTerm",
    "MatchTerm",
    "PortDataset",
    "BaseStream",
    "GenuineStream",
    "ImpairmentFlow",
    "BasicImpairmentFlowFilter",
    "ExtendedImpairmentFlowFilter",
)
