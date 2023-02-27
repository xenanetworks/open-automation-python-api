from __future__ import annotations

from io import BytesIO
from typing import (
    Any,
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
from .exceptions import (
    FieldDeclarationError,
    FirmwareVersionError,
)


RESPONSE_CLS_NAME = "ResponseBodyStruct"
SKIP_CLASSES = (
    "RequestBodyStruct",
    RESPONSE_CLS_NAME,
)


class Order:
    __slots__ = ("is_response", "__ordered_names", "__ordered_items", "__dynamic_fields")

    def __init__(self, is_response: bool = False) -> None:
        self.is_response = is_response
        self.__ordered_names: tuple[str, ...] = tuple()
        self.__ordered_items: list[FieldSpecs] = []
        self.__dynamic_fields: list[FieldSpecs] = []

    def __str__(self) -> str:
        offsets = ", ".join(str(i.offset) for i in self.__ordered_items)
        sizes = ", ".join(str(i.bsize) for i in self.__ordered_items)
        return f"Offsets: {offsets}\nSizes:   {sizes}"

    def add(self, item: FieldSpecs, name: str) -> None:
        self.__ordered_names += (name,)
        self.__ordered_items.append(item)
        if self.is_response and item.is_dynamic:
            self.__dynamic_fields.append(item)

    @property
    def field_names(self) -> tuple[str, ...]:
        return self.__ordered_names

    def update_offsets(self) -> None:
        for position_idx, field_specs in enumerate(self.__ordered_items):
            field_specs.offset = sum(early_item.bsize for early_item in self.__ordered_items[:position_idx])

    def calc_dynamic_fields(self, buffer: memoryview) -> None:
        if not self.__dynamic_fields:
            return None
        for field_specs in self.__dynamic_fields:
            field_specs.calc_bsize(buffer)
        self.update_offsets()


class OrderedMeta(type):
    def __new__(cls: Type[Self], clsname: str, bases: tuple[Type], clsdict: dict[str, Any]) -> Self:
        if clsname not in SKIP_CLASSES:
            is_response = any(iter(cls_.__name__ == RESPONSE_CLS_NAME for cls_ in bases))
            annotations = utils.resolve_annotations(
                clsdict.get('__annotations__', {}),
                clsdict.get('__module__', None)
            )
            order = Order(is_response)
            for field_name, client_type in annotations.items():
                field_specs = clsdict.get(field_name, None)
                if not isinstance(field_specs, FieldSpecs):
                    raise FieldDeclarationError(field_name)
                clsdict[field_name] = FieldDescriptor(field_specs, client_type, is_response)
                order.add(field_specs, field_name)
            order.update_offsets()
            clsdict['_order'] = order
        return super().__new__(cls, clsname, bases, {**clsdict})

    @classmethod
    def __prepare__(cls, clsname: str, bases: tuple) -> dict[str, Any]:
        return dict()


@dataclass_transform(kw_only_default=True, field_descriptors=(field, FieldSpecs,))  # type: ignore[Pylance, folse positive]
class RequestBodyStruct(metaclass=OrderedMeta):
    """Request Body class"""

    __slots__ = ("_buffer", "_order", "__stored")

    def __init__(self, **kwargs) -> None:
        self._buffer = BytesIO()
        order = cast(Order, self._order)
        for name in order.field_names:
            if name not in kwargs:
                raise AttributeError(f"[{name}] is required!")
            setattr(self, name, kwargs[name])
        self.__stored = kwargs
        nbytes = self.nbytes()
        padding = bytes(4 - (nbytes % 4) if nbytes % 4 else 0)
        self._buffer.write(padding)

    def __repr__(self) -> str:
        cls_name = f"{self.__class__.__qualname__}"
        vals = ", ".join(f"{n}={v!r}" for n, v in self.__stored.items())
        return f"{cls_name}({vals})"

    def nbytes(self) -> int:
        return self._buffer.getbuffer().nbytes

    def to_hex(self) -> str:
        return self.to_bytes().hex()

    def to_bytes(self) -> bytes:
        return self._buffer.getvalue()


class ResponseBodyStruct(metaclass=OrderedMeta):
    """Response Body class"""

    __slots__ = ("_buffer", "_order")

    def __init__(self, packet_body: bytes | bytearray | memoryview) -> None:
        self._buffer = memoryview(packet_body).toreadonly()
        order = cast(Order, self._order)
        order.calc_dynamic_fields(self._buffer)

    def __repr__(self) -> str:
        cls_name = f"{self.__class__.__qualname__}"
        vals = ", ".join(f"{n}={v!r}" for n, v in zip(self._order.field_names, self.to_tuple()))
        return f"{cls_name}({vals})"

    def to_tuple(self) -> tuple:
        def get_val(fn: str) -> Any:
            try:
                val = getattr(self, fn)
            except FirmwareVersionError:
                return "NOT_SUPORTED_BY_FIRMWARE"
            else:
                return val
        return tuple(map(get_val, self._order.field_names))

    def to_hex(self) -> str:
        return self._buffer.hex()

    def to_bytes(self) -> bytes:
        return self._buffer.tobytes()
