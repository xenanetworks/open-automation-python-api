"""XP_ 	TSN Extension - Histogram"""
from dataclasses import dataclass
import typing
import functools

from ..protocol.command_builders import (
    build_get_request,
    build_set_request
)
from .. import interfaces
from ..transporter.token import Token
from ..protocol.fields.data_types import *
from ..protocol.fields.field import XmpField
from ..registry import register_command
from .enums import *

@register_command
@dataclass
class XPD_TSNCREATE:
    """
    Create dataset with a specified index. Command fails if index already exists
    """

    code: typing.ClassVar[int] = 4030
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        dataset_id: XmpField[XmpInt] = XmpField(XmpInt)  # integer, Index of dataset to create.

    def set(self, dataset_id: int) -> "Token":
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, dataset_id=dataset_id))


@register_command
@dataclass
class XPD_TSNINDICES:
    """
    Create datasets with the specified indices. This command deletes all pre-
    existing datasets on the port before creating the list of new datasets. No
    configuration or data is preserved.
    """

    code: typing.ClassVar[int] = 4031
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        indices: XmpField[XmpIntList] = XmpField(XmpIntList)  # list of integers, indices of datasets to create.

    @dataclass(frozen=True)
    class GetDataAttr:
        indices: XmpField[XmpIntList] = XmpField(XmpIntList)  # list of integers, indices of datasets to create.

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self) -> "Token":
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
            ),
        )


@register_command
@dataclass
class XPD_TSNSOURCE:
    """
    Select data source for dataset
    """

    code: typing.ClassVar[int] = 4032
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        dataset_id: XmpField[XmpInt] = XmpField(XmpInt)  # integer, index of an already created dataset.
        source: XmpField[XmpInt] = XmpField(XmpInt, choices=TSNSource)  # coded byte, index of an already created dataset.

    @dataclass(frozen=True)
    class GetDataAttr:
        dataset_id: XmpField[XmpInt] = XmpField(XmpInt)  # integer, index of an already created dataset.
        source: XmpField[XmpInt] = XmpField(XmpInt, choices=TSNSource)  # coded byte, index of an already created dataset.

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, dataset_id: int, source: TSNSource) -> "Token":
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, dataset_id=dataset_id, source=source))

    set_drift = functools.partialmethod(set, TSNSource.DRIFT)
    set_driftpre = functools.partialmethod(set, TSNSource.DRIFTPRE)
    set_pdelay = functools.partialmethod(set, TSNSource.PDELAY)
    set_nrr = functools.partialmethod(set, TSNSource.NRR)


@register_command
@dataclass
class XPD_TSNRANGE:
    """
    Bucket configuration for dataset
    """

    code: typing.ClassVar[int] = 4033
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        dataset_id: XmpField[XmpInt] = XmpField(XmpInt)  # integer, index of an already created dataset.
        start: XmpField[XmpInt] = XmpField(XmpInt)  # long integer, First value going into the second bucket. Any data less than start go to bucket 0. Signed long.
        step: XmpField[XmpInt] = XmpField(XmpInt)  # integer, Span of each bucket (except first and last): Power of two: 16, 32, 64, ..., 1048576, 2097152
        count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, Number of buckets, including first + last. Must be greater than 2.

    @dataclass(frozen=True)
    class GetDataAttr:
        dataset_id: XmpField[XmpInt] = XmpField(XmpInt)  # integer, index of an already created dataset.
        start: XmpField[XmpInt] = XmpField(XmpInt)  # long integer, First value going into the second bucket. Any data less than start go to bucket 0. Signed long.
        step: XmpField[XmpInt] = XmpField(XmpInt)  # integer, Span of each bucket (except first and last): Power of two: 16, 32, 64, ..., 1048576, 2097152
        count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, Number of buckets, including first + last. Must be greater than 2.

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, dataset_id: int, start: int, step: int, count: int) -> "Token":
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, dataset_id=dataset_id, start=start, step=step, count=count))


@register_command
@dataclass
class XPD_TSNENABLE:
    """
    Enable or disable dataset configuration on a port.
    """

    code: typing.ClassVar[int] = 4034
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        dataset_id: XmpField[XmpInt] = XmpField(XmpInt)  # integer, index of an already created dataset.
        on_off: XmpField[XmpByte] = XmpField(XmpByte)  # coded byte, on/off dataset configuration on a port.

    @dataclass(frozen=True)
    class GetDataAttr:
        dataset_id: XmpField[XmpInt] = XmpField(XmpInt)  # integer, index of an already created dataset.
        on_off: XmpField[XmpByte] = XmpField(XmpByte)  # coded byte, on/off dataset configuration on a port.

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, dataset_id: int, on_off: int) -> "Token":
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, dataset_id=dataset_id, on_off=on_off))


@register_command
@dataclass
class XPD_TSNSAMPLES:
    """
    Get bucket data for dataset.
    """

    code: typing.ClassVar[int] = 4035
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        dataset_id: XmpField[XmpInt] = XmpField(XmpInt)  # integer, index of an already created dataset.
        values: XmpField[XmpInt] = XmpField(
            XmpInt
        )  # list of long integers, Counter for bucket x. The number of counters is configured with XPD_TSNRANGE. The semantics are of the bucket counters are configured with XPD_TSNSOURCE.

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class XPD_TSNDELETE:
    """
    Delete dataset with specified index. No error is returned if dataset doesn’t
    exist.
    """

    code: typing.ClassVar[int] = 4041
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        dataset_id: XmpField[XmpInt] = XmpField(XmpInt)  # integer, Index of dataset to delete.

    def set(self, dataset_id: int) -> "Token":
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, dataset_id=dataset_id))


