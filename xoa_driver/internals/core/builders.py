from __future__ import annotations
from .transporter.protocol.struct_request import Request
from .transporter.protocol._constants import CommandType
from .transporter._typings import (
    ICmdOnlySet,
    ICmdOnlyGet,
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
