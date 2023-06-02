from __future__ import annotations
from functools import (
    cached_property,
    partial,
)

from io import BytesIO
from typing import (
    Any,
    ClassVar,
    Generator,
    Iterator,
    NamedTuple,
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
from .descriptor import (
    ResponseFieldDescr,
    RequestFieldDescr
)
from .exceptions import (
    FieldDeclarationError,
    FirmwareVersionError,
)


RESPONSE_CLS_NAME = "ResponseBodyStruct"
SKIP_CLASSES = (
    "RequestBodyStruct",
    RESPONSE_CLS_NAME,
)


class CellInfo(NamedTuple):
    fmt: str
    offset: int
    bsize: int | None


class Cell:
    __slots__ = (
        "name",
        "spec",
        "_prev",
        "_next"
    )

    def __init__(self, name: str, spec: FieldSpecs) -> None:
        self.name = name
        self.spec = spec

        self._prev: Cell | None = None
        self._next: Cell | None = None

    def info(self, buff: memoryview | None = None, offset: int = 0) -> CellInfo:
        bsize = self.spec.calc_bsize(buff, offset)
        fmt = self.spec.format(bsize)
        return CellInfo(fmt, offset, bsize)

    @property
    def is_dynamic(self) -> bool:
        return self.spec.is_dynamic


class Order:
    __slots__ = (
        "__start",
        "__head",
        "__head_idx",
        "__stencil",
        "__dict__",
    )

    def __init__(self) -> None:
        self.__start: Cell | None = None
        self.__head: Cell | None = None
        self.__head_idx: int = -1
        self.__stencil: tuple[tuple[str, int], ...] = ()

    def __iter__(self):
        temp = self.__start
        while temp is not None:
            yield temp
            temp = temp._next

    def __reversed__(self):
        temp = self.__head
        while temp is not None:
            yield temp
            temp = temp._prev

    @cached_property
    def is_dynamic(self) -> bool:
        """Computed only once, Determinate if structure is contain types with dynamic lenght or not"""
        return any(c.is_dynamic for c in self)

    @property
    def field_names(self) -> Iterator[str]:
        """Get iterator of ordered fields names"""
        return iter(itm.name for itm in self)

    def append(self, name: str, data: FieldSpecs) -> int:
        """Append field structure"""
        self.__head_idx += 1
        c = Cell(name, data)
        if not self.__start:
            self.__start = c
        if self.__head:
            self.__head._next = c
            c._prev = self.__head
        self.__head = c
        return self.__head_idx

    def bake(self) -> None:
        """Bake tuple of the offsets for static length structures, at the defenition time."""
        if self.is_dynamic:
            return None
        self.__stencil = tuple(self.__construct_stencil(None))

    def get_stencil(self, buffer: memoryview) -> tuple[tuple[str, int], ...]:
        """Get offsets for the instance. If struct is static get baked offsets, otherwise compute them for the individual instance"""
        if self.is_dynamic:
            return tuple(self.__construct_stencil(buffer))
        return self.__stencil

    def __construct_stencil(self, buffer: memoryview | None) -> Generator[tuple[str, int], None, None]:
        """An private method for construct stencils items."""
        current_node = self.__start
        cumulative_sum = 0

        while current_node is not None:
            info_tuple = current_node.info(buffer, cumulative_sum)
            yield (info_tuple.fmt, cumulative_sum)
            cumulative_sum += info_tuple.bsize or 0
            current_node = current_node._next


class OrderedMeta(type):
    def __new__(cls: Type[Self], clsname: str, bases: tuple[Type], clsdict: dict[str, Any]) -> Self:
        if clsname not in SKIP_CLASSES:
            is_response = any(iter(cls_.__name__ == RESPONSE_CLS_NAME for cls_ in bases))
            annotations = utils.resolve_annotations(
                clsdict.get('__annotations__', {}),
                clsdict.get('__module__', None)
            )
            clsdict = cls._prepare_order(
                annotations=annotations,
                clsdict=clsdict,
                is_response=is_response
            )
        return super().__new__(cls, clsname, bases, clsdict)

    @classmethod
    def __prepare__(cls, clsname: str, bases: tuple) -> dict[str, Any]:
        return dict()

    @staticmethod
    def _prepare_order(annotations: dict[str, Any], clsdict: dict[str, Any], is_response: bool) -> dict[str, Any]:
        clsdict["_order"] = order = Order()
        for field_name, client_type in annotations.items():
            field_specs = clsdict.get(field_name, None)
            if not isinstance(field_specs, FieldSpecs):
                raise FieldDeclarationError(field_name)
            position_idx = order.append(field_name, field_specs)
            descriptor = ResponseFieldDescr if is_response else RequestFieldDescr
            clsdict[field_name] = descriptor(
                idx=position_idx,
                specs=field_specs,
                user_type=client_type,
            )
        order.bake()
        return clsdict


@dataclass_transform(kw_only_default=True, field_descriptors=(field, FieldSpecs,))  # type: ignore[Pylance, false positive]
class RequestBodyStruct(metaclass=OrderedMeta):
    """Request Body class"""

    __slots__ = ("_buffer", "_order", "__stored", "__nbytes")

    def __init__(self, **kwargs) -> None:
        self._buffer = BytesIO()
        for name in cast(Order, self._order).field_names:
            if name not in kwargs:
                raise AttributeError(f"[{name}] is required!")
            setattr(self, name, kwargs[name])
        self.__stored = kwargs
        self.__nbytes = self._buffer.getbuffer().nbytes
        padding = bytes(4 - (self.__nbytes % 4) if self.__nbytes % 4 else 0)
        self._buffer.write(padding)

    def __repr__(self) -> str:
        cls_name = f"{self.__class__.__qualname__}"
        vals = ", ".join(
            f"{n}={v!r}" for n, v in self.__stored.items()
        )
        return f"{cls_name}({vals})"

    def nbytes(self) -> int:
        """Return number of byffer bytes"""
        return self.__nbytes

    def nbytes_with_padding(self) -> int:
        return self._buffer.getbuffer().nbytes

    def to_dict(self) -> dict[str, Any]:
        """Get Dict representation of the object"""
        return self.__stored

    def to_hex(self) -> str:
        """Get buffer as hex string"""
        return self.to_bytes().hex()

    def to_bytes(self) -> bytes:
        """Get buffer as bytes"""
        return self._buffer.getvalue()


def get_val(inst: object, fn: str) -> Any:
    """
    An helper method for get a value fro mobject and in case if FirmwareVersionError swap the value as not supported.

    IMPORTANT: only used in conversion to tuple, dict
    """
    # TODO: Allow to skip not supported values for tuple and dict
    try:
        val = getattr(inst, fn)
    except FirmwareVersionError:
        return "NOT_SUPORTED_BY_FIRMWARE"
    else:
        return val


class ResponseBodyStruct(metaclass=OrderedMeta):
    """Response Body class"""

    __slots__ = ("_buffer", "_order", "_stencil")
    _order: ClassVar[Order]

    def __init__(self, packet_body: bytes | bytearray | memoryview) -> None:
        self._buffer = memoryview(packet_body).toreadonly()
        self._stencil = self._order.get_stencil(self._buffer)

    def __repr__(self) -> str:
        cls_name = self.__class__.__qualname__
        vals = ", ".join(
            f"{n}={v!r}" for n, v in self.to_dict().items()
        )
        return f"{cls_name}({vals})"

    def nbytes(self) -> int:
        """Return number of byffer bytes"""
        return self._buffer.nbytes

    def to_tuple(self) -> tuple:
        """Get py values as tuple"""
        get_val_ = partial(get_val, self)
        return tuple(map(get_val_, self._order.field_names))

    def to_dict(self) -> dict[str, Any]:
        """Get Dict representation of the object"""
        return {
            name: get_val(self, name)
            for name in self._order.field_names
        }

    def to_hex(self) -> str:
        """Get buffer as hex string"""
        return self._buffer.hex()

    def to_bytes(self) -> bytes:
        """Get buffer as bytes"""
        return self._buffer.tobytes()
