from __future__ import annotations

import struct
from io import BytesIO
from typing import Any, Type, cast

from typing_extensions import Self, dataclass_transform

from . import utils
from .field import FieldSpecs, field
from .descriptor import StructField


class OrderedMeta(type):
    def __new__(cls: Type[Self], clsname: str, bases: tuple[Type], clsdict: dict[str, Any]) -> Self:
        if clsname not in {"RequestBodyStruct", "ResponseBodyStruct"}:
            annotations = utils.resolve_annotations(
                clsdict.get('__annotations__', {}),
                clsdict.get('__module__', None)
            )
            order = []
            for f_name, user_type in annotations.items():
                field_specs = clsdict.get(f_name, None)
                if not isinstance(field_specs, FieldSpecs):
                    raise ValueError(f"Structure Field {f_name!r} must be described with <field method>")
                type_size = struct.calcsize(field_specs.xmp_type.data_format)
                clsdict[f_name] = StructField(field_specs.xmp_type, type_size, user_type)
                order.append((f_name, type_size))
            clsdict['_order'] = order
            clsdict['_is_response'] = any([c.__name__ == "ResponseBodyStruct" for c in bases])
        return super().__new__(cls, clsname, bases, {**clsdict})

    @classmethod
    def __prepare__(cls, clsname: str, bases: tuple) -> dict[str, Any]:
        return dict()


@dataclass_transform(kw_only_default=True, field_descriptors=(field, FieldSpecs))
class RequestBodyStruct(metaclass=OrderedMeta):
    """Request Body class"""
    __slots__ = ("_buffer", "_order")

    def __init__(self, **kwargs) -> None:
        self._buffer = BytesIO()
        for name, t_size in cast(list[tuple[str, int]], self._order):
            if name not in kwargs:
                raise AttributeError(f"[{name}] is required!")
            setattr(self, name, kwargs[name])
        nbytes = self._buffer.getbuffer().nbytes
        padding = bytes(4 - (nbytes % 4) if nbytes % 4 else 0)
        self._buffer.write(padding)

    def to_hex(self) -> str:
        return self.to_bytes().hex()

    def to_bytes(self) -> bytes:
        return self._buffer.getvalue()


class ResponseBodyStruct(metaclass=OrderedMeta):
    """Response Body class"""
    __slots__ = ("_buffer",)

    def __init__(self, packet_body: bytes) -> None:
        self._buffer = memoryview(packet_body).toreadonly()

    def to_hex(self) -> str:
        return self._buffer.hex()

    def to_bytes(self) -> bytes:
        return self._buffer.tobytes()
