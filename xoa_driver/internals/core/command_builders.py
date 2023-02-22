from __future__ import annotations
from typing import Type
from .protocol.struct_header import ResponseHeader
from .protocol.struct_request import Request
from .protocol.struct_response import Response
from .protocol._constants import CommandType
from .interfaces import (
    ICmdOnlySet,
    ICmdOnlyGet,
    CMD_TYPE
)


def build_set_request(cls: ICmdOnlySet, **kwargs) -> Request:
    indices = kwargs.pop("indices", [])
    module = kwargs.pop("module", None)
    port = kwargs.pop("port", None)
    req_values = cls.SetDataAttr(**kwargs)
    return Request(
        class_name=type(cls).__name__,
        cmd_type=CommandType.COMMAND_VALUE,
        cmd_code=cls.code,
        module_index=module,
        port_index=port,
        indices=indices,
        values=req_values
    )


def build_get_request(cls: ICmdOnlyGet, **kwargs) -> Request:
    indices = kwargs.pop("indices", [])
    module = kwargs.pop("module", None)
    port = kwargs.pop("port", None)
    req_values = None
    return Request(
        class_name=type(cls).__name__,
        cmd_type=CommandType.COMMAND_QUERY,
        cmd_code=cls.code,
        module_index=module,
        port_index=port,
        indices=indices,
        values=req_values
    )


def create_response_obj(cmd: Type[CMD_TYPE], header: ResponseHeader, data: bytes) -> Response:
    """Parse bytes retrieved from server to Response structure."""
    return Response(
        class_name=cmd.__name__,
        header=header,
        buffer=data,
        response_struct=getattr(cmd, "GetDataAttr", None)
    )
