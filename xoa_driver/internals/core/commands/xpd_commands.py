#: L23 Port TSN Extension Histogram Commands

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
    Create a histogram with a specified index. Command fails if index already exists.
    """

    code: typing.ClassVar[int] = 4030
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _dataset_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Create a histogram with a specified index.
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._dataset_xindex]))


@register_command
@dataclass
class XPD_TSNINDICES:
    """
    Create histograms with the specified indices. This command deletes all pre-
    existing histograms on the port before creating the list of new histograms. No
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
        """Get a list ofg indices of the histograms on a TSN port.

        :return: a list ofg indices of the histograms on a TSN port.
        :rtype: XPD_TSNINDICES.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self) -> "Token":
        """Create histograms with the specified indices.
        """
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
    Select data source for a historgram.
    """

    code: typing.ClassVar[int] = 4032
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _dataset_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        source: XmpField[XmpInt] = XmpField(XmpInt, choices=TSNHistogramSource)  # coded byte, index of an already created dataset.

    @dataclass(frozen=True)
    class GetDataAttr:
        source: XmpField[XmpInt] = XmpField(XmpInt, choices=TSNHistogramSource)  # coded byte, index of an already created dataset.

    def get(self) -> "Token[GetDataAttr]":
        """Get the data source of a historgram.

        :return: data source of a historgram.
        :rtype: XPD_TSNSOURCE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._dataset_xindex]))

    def set(self, source: TSNHistogramSource) -> "Token":
        """Set the data source for a historgram.

        :param source: index of an already created histogram.
        :type source: TSNHistogramSource
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._dataset_xindex], source=source))

    set_drift = functools.partialmethod(set, source=TSNHistogramSource.DRIFT)
    """Select post-servo offset to Grandmaster as data source."""
    set_driftpre = functools.partialmethod(set, source=TSNHistogramSource.DRIFTPRE)
    """Select pre-servo offset to Grandmaster as data source."""
    set_pdelay = functools.partialmethod(set, source=TSNHistogramSource.PDELAY)
    """Select PDelay data as data source."""
    set_nrr = functools.partialmethod(set, source=TSNHistogramSource.NRR)
    """Select Neighbor Rate Ratio data as data source."""


@register_command
@dataclass
class XPD_TSNRANGE:
    """
    Bucket configuration for a histogram.
    """

    code: typing.ClassVar[int] = 4033
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _dataset_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        start: XmpField[XmpInt] = XmpField(XmpInt)  # long integer, First value going into the second bucket. Any data less than start go to bucket 0. Signed long.
        step: XmpField[XmpInt] = XmpField(XmpInt)  # integer, Span of each bucket (except first and last): Power of two: 16, 32, 64, ..., 1048576, 2097152
        count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, Number of buckets, including first + last. Must be greater than 2.

    @dataclass(frozen=True)
    class GetDataAttr:
        start: XmpField[XmpInt] = XmpField(XmpInt)  # long integer, First value going into the second bucket. Any data less than start go to bucket 0. Signed long.
        step: XmpField[XmpInt] = XmpField(XmpInt)  # integer, Span of each bucket (except first and last): Power of two: 16, 32, 64, ..., 1048576, 2097152
        count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, Number of buckets, including first + last. Must be greater than 2.

    def get(self) -> "Token[GetDataAttr]":
        """Get the bucket configuration of the histogram.

        :return: the bucket configuration of the histogram.
        :rtype: XPD_TSNRANGE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._dataset_xindex]))

    def set(self, start: int, step: int, count: int) -> "Token":
        """Set the bucket configuration of the histogram.

        :param start: First value going into the second bucket. Any data less than start go to bucket 0.
        :type start: int
        :param step: Span of each bucket (except first and last): Power of two: 16, 32, 64, ..., 1048576, 2097152
        :type step: int
        :param count: Number of buckets, including first + last. Must be greater than 2.
        :type count: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._dataset_xindex], start=start, step=step, count=count))


@register_command
@dataclass
class XPD_TSNENABLE:
    """
    Enable or disable histogram configuration on a TSN port.
    """

    code: typing.ClassVar[int] = 4034
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _dataset_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte)  # coded byte, on/off dataset configuration on a port.

    @dataclass(frozen=True)
    class GetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte)  # coded byte, on/off dataset configuration on a port.

    def get(self) -> "Token[GetDataAttr]":
        """Get histogram enable/disable status on the TSN port.

        :return: histogram enable/disable status on the TSN port.
        :rtype: XPD_TSNENABLE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._dataset_xindex]))

    def set(self, on_off: int) -> "Token":
        """Enable or disable histogram configuration on a TSN port. 

        :param on_off: histogram enable/disable status on the TSN port.
        :type on_off: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._dataset_xindex], on_off=on_off))


@register_command
@dataclass
class XPD_TSNSAMPLES:
    """
    Get bucket data for a histogram.
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
        """Get bucket data for a histogram.

        :return: bucket data for a histogram.
        :rtype: XPD_TSNSAMPLES.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class XPD_TSNDELETE:
    """
    Delete a histogram with the specified index. No error is returned if the histogram does not exist.
    """

    code: typing.ClassVar[int] = 4041
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _dataset_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Delete a histogram with the specified index.
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._dataset_xindex]))


