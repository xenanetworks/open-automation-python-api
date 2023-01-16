from __future__ import annotations

from io import BytesIO
from typing import (
    Any,
    Tuple,
    Type,
    cast,
)

from typing_extensions import (
    Self,
    dataclass_transform,
)

from . import utils
from .field import (
    FieldSpecs,
    field,
)
from .descriptor import FieldDescriptor
from .exceptions import FieldDeclarationError


RESPONSE_CLS_NAME = "ResponseBodyStruct"
SKIP_CLASSES = (
    "RequestBodyStruct",
    RESPONSE_CLS_NAME,
)


def update_dynamic_sz_field() -> None:
    ...


class OrderedMeta(type):
    def __new__(cls: Type[Self], clsname: str, bases: tuple[Type], clsdict: dict[str, Any]) -> Self:
        if clsname not in SKIP_CLASSES:
            is_response = any(iter(cls_.__name__ == RESPONSE_CLS_NAME for cls_ in bases))
            annotations = utils.resolve_annotations(
                clsdict.get('__annotations__', {}),
                clsdict.get('__module__', None)
            )
            order = []
            for f_name, user_type in annotations.items():
                field_specs = clsdict.get(f_name, None)
                if not isinstance(field_specs, FieldSpecs):
                    raise FieldDeclarationError(f_name)
                clsdict[f_name] = FieldDescriptor(field_specs, user_type, is_response)
                order.append((f_name, field_specs.bsize))
                if is_response and field_specs.is_dynamic:
                    ...


            clsdict['_order'] = tuple(order)
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
        for name, _ in cast(Tuple[Tuple[str, int], ...], self._order):
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

    __slots__ = ("_buffer", "__dynamic_fields")

    def __init__(self, packet_body: bytes) -> None:
        self._buffer = memoryview(packet_body).toreadonly()
        for field in __dynamic_fields:
            firld.

    def __update_offsets(self) -> None:
        if cast(bool, self.__dynamic):
            ...

    def to_hex(self) -> str:
        return self._buffer.hex()

    def to_bytes(self) -> bytes:
        return self._buffer.tobytes()
