from __future__ import annotations
from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from . import struct_header
from . import struct_response
from . import struct_request
from .constants import CommandType

from .payload import ResponseBodyStruct
from xoa_driver.internals.core.interfaces import (
    ICmdOnlySet,
    ICmdOnlyGet,
    CMD_TYPE,
)


def build_set_request(cls: ICmdOnlySet, **kwargs) -> "struct_request.Request":
    indices = kwargs.pop("indices", [])
    module = kwargs.pop("module", None)
    port = kwargs.pop("port", None)
    req_values = cls.SetDataAttr(**kwargs)
    return struct_request.Request(
        class_name=type(cls).__name__,
        cmd_type=CommandType.COMMAND_VALUE,
        cmd_code=cls.code,
        module_index=module,
        port_index=port,
        indices=indices,
        values=req_values
    )


def build_get_request(cls: ICmdOnlyGet, **kwargs) -> "struct_request.Request":
    indices = kwargs.pop("indices", [])
    module = kwargs.pop("module", None)
    port = kwargs.pop("port", None)
    req_values = None
    return struct_request.Request(
        class_name=type(cls).__name__,
        cmd_type=CommandType.COMMAND_QUERY,
        cmd_code=cls.code,
        module_index=module,
        port_index=port,
        indices=indices,
        values=req_values
    )


def build_from_bytes(cls: Type[CMD_TYPE], header: "struct_header.ResponseHeader", data: bytearray) -> "struct_response.Response":
    """Parse bytes retrieved from server to Response structure."""
    properties_structure: Type[ResponseBodyStruct] | None = getattr(cls, "GetDataAttr", None)
    return struct_response.Response(
        class_name=cls.__name__,
        header=header,
        buffer=data,
        response_struct=properties_structure
    )
