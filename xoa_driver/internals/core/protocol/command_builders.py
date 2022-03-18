from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import struct_header
from . import struct_response
from . import struct_request
from .constants import (
    CommandType,
    NOTHING,
)
from xoa_driver.internals.core.interfaces import (
    ICmdOnlySet,
    ICmdOnlyGet,
    CMD_TYPE,
)

def build_set_request(cls: ICmdOnlySet, **kwargs) -> "struct_request.Request":
    indices = kwargs.pop("indices", [])
    module = kwargs.pop("module", NOTHING)
    port = kwargs.pop("port", NOTHING)
    req_values = cls.SetDataAttr(**kwargs)  # type: ignore
    set_get = CommandType.COMMAND_VALUE.value
    return struct_request.Request(
        type(cls).__name__,
        indices, 
        set_get, 
        cls.code, 
        module, 
        port, 
        req_values
    )

def build_get_request(cls: ICmdOnlyGet, **kwargs) -> "struct_request.Request":
    indices = kwargs.pop("indices", [])
    module = kwargs.pop("module", NOTHING)
    port = kwargs.pop("port", NOTHING)
    req_values = None
    set_get = CommandType.COMMAND_QUERY.value
    return struct_request.Request(
        type(cls).__name__,
        indices, 
        set_get, 
        cls.code, 
        module, 
        port, 
        req_values
    )


def build_from_bytes(cls: CMD_TYPE, header: "struct_header.ResponseHeader", data: bytes) -> "struct_response.Response":
    """Parse bytes retrieved from server to Response structure."""
    properties_structure = getattr(cls, "GetDataAttr", None)
    return struct_response.Response(header, cls.__name__, data, properties_structure)