from typing import NamedTuple

class ModuleKind(NamedTuple):
    """NamedTuple of id's of module."""
    module_id: int 

class PortKind(NamedTuple):
    """NamedTuple of id's of module, port."""
    module_id: int 
    port_id: int


class IndicesKind(NamedTuple):
    """NamedTuple of id's of module, port, and xindex."""
    module_id: int 
    port_id: int 
    index_id: int