from __future__ import annotations
from dataclasses import dataclass
import typing
import functools

from xoa_driver.internals.core.builders import (
    build_get_request,
    build_set_request
)
from xoa_driver.internals.core import interfaces
from xoa_driver.internals.core.token import Token
from xoa_driver.internals.core.transporter.registry import register_command
from xoa_driver.internals.core.transporter.protocol.payload import (
    field,
    RequestBodyStruct,
    ResponseBodyStruct,
    XmpByte,
    XmpInt,
    XmpLong,
    XmpSequence,

)
from .enums import (
    OnOff,
    SourceType,
    PacketDetailSelection,
)


@register_command
@dataclass
class PD_INDICES:
    """
    Obtain or configure histogram indices for each of N histograms.
    """

    code: typing.ClassVar[int] = 140
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        histogram_indices: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()]))
        """list of integers, histogram indices"""

    class SetDataAttr(RequestBodyStruct):
        histogram_indices: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()]))
        """list of integers, histogram indices"""

    def get(self) -> Token[GetDataAttr]:
        """Get the histogram indices for each of N histograms.

        :return: the histogram indices for each of N histograms
        :rtype: PD_INDICES.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, histogram_indices: typing.List[int]) -> Token[None]:
        """Set the histogram indices for each of N histograms.

        :param histogram_indices: histogram indices
        :type histogram_indices: typing.List[int]
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, histogram_indices=histogram_indices))


@register_command
@dataclass
class PD_CREATE:
    """
    Creates a histogram definition with the specified sub-index value.
    """

    code: typing.ClassVar[int] = 141
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _dataset_xindex: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Create a histogram definition with the specified sub-index value.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._dataset_xindex]))


@register_command
@dataclass
class PD_DELETE:
    """
    Delete an existing histogram definition.
    """

    code: typing.ClassVar[int] = 142
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _dataset_xindex: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Delete an existing histogram definition.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._dataset_xindex]))


@register_command
@dataclass
class PD_ENABLE:
    """
    Whether a histogram is currently active on a port. When turned on, all the bucket
    counts are cleared to zero. Subsequently each packet matching the histogram source
    criteria is counted into one of the buckets. While a histogram is enabled its
    parameters cannot be changed.
    """

    code: typing.ClassVar[int] = 143
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _dataset_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded integer, whether the histogram is enabled."""

    class SetDataAttr(RequestBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded integer, whether the histogram is enabled."""

    def get(self) -> Token[GetDataAttr]:
        """Get whether a histogram is currently active on a port.

        :return: whether the histogram is enabled
        :rtype: OnOff
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._dataset_xindex]))

    def set(self, on_off: OnOff) -> Token[None]:
        """Set whether a histogram is currently active on a port.

        :param on_off: whether the histogram is enabled
        :type on_off: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._dataset_xindex], on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable the histogram on the port.
    """

    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable the histogram on the port.
    """


@register_command
@dataclass
class PD_SOURCE:
    """
    The source criteria specifying what is counted, and for which packets, by a
    histogram of a port.
    """

    code: typing.ClassVar[int] = 144
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _dataset_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        source_type: SourceType = field(XmpInt())
        """coded integer, specifying what is counted and for which packets."""
        which_packets: PacketDetailSelection = field(XmpInt())
        """coded integer, specifying a further detail on which packets to count."""
        identity: int = field(XmpInt())
        """integer, test payload id or filter id for the wanted packets."""

    class SetDataAttr(RequestBodyStruct):
        source_type: SourceType = field(XmpInt())
        """coded integer, specifying what is counted and for which packets."""
        which_packets: PacketDetailSelection = field(XmpInt())
        """coded integer, specifying a further detail on which packets to count."""
        identity: int = field(XmpInt())
        """integer, test payload id or filter id for the wanted packets."""

    def get(self) -> Token[GetDataAttr]:
        """Get the source criteria specifying what is counted, and for which packets, by a histogram of a port.

        :return: what is counted and for which packets, a further detail on which packets to count, test payload id or filter id for the wanted packets
        :rtype: PD_SOURCE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._dataset_xindex]))

    def set(self, source_type: SourceType, which_packets: PacketDetailSelection, identity: int) -> Token[None]:
        """Set the source criteria specifying what is counted, and for which packets, by a histogram of a port.

        :param source_type: what is counted and for which packets
        :type source_type: SourceType
        :param which_packets: a further detail on which packets to count
        :type which_packets: PacketDetailSelection
        :param identity: test payload id or filter id for the wanted packets
        :type identity: int
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._dataset_xindex],
                source_type=source_type,
                which_packets=which_packets,
                identity=identity
            )
        )


@register_command
@dataclass
class PD_RANGE:
    """
    The bucket ranges used for classifying the packets counted by a histogram of a
    port. The packets are either counted by length, measured in bytes, by inter-
    frame gap to the preceding packet,  also measured in bytes, or by latency in
    transmission measured in nanoseconds.  There are a fixed number of buckets, each
    middle bucket covering a fixed-size range of values which is a power of two.
    The first and last buckets count all the packets that do not fit within the
    ranges of the middle buckets. The buckets are placed at a certain offset by
    specifying the first value that should be counted by the first middle bucket.
    """

    code: typing.ClassVar[int] = 145
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _dataset_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        start: int = field(XmpInt())
        """integer, first value going into the second bucket."""
        step: int = field(XmpInt())
        """integer, the span of each middle bucket:
            (1) 1,2,4,8,16,32,64,128,256,512 (bytes, non-latency histograms).
            (2) 16,32,64,128,...,1048576,2097152 (nanoseconds, latency histograms).
        """
        bucket_count: int = field(XmpInt())
        """integer, the total number of buckets."""

    class SetDataAttr(RequestBodyStruct):
        start: int = field(XmpInt())
        """integer, first value going into the second bucket."""
        step: int = field(XmpInt())
        """integer, the span of each middle bucket:
            (1) 1,2,4,8,16,32,64,128,256,512 (bytes, non-latency histograms).
            (2) 16,32,64,128,...,1048576,2097152 (nanoseconds, latency histograms).
        """
        bucket_count: int = field(XmpInt())
        """integer, the total number of buckets."""

    def get(self) -> Token[GetDataAttr]:
        """Get the bucket ranges used for classifying the packets counted by a histogram of a port.

        :return: first value going into the second bucket, the span of each middle bucket, the total number of buckets
        :rtype: PD_RANGE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._dataset_xindex]))

    def set(self, start: int, step: int, bucket_count: int) -> Token[None]:
        """Set the bucket ranges used for classifying the packets counted by a histogram of a port.
        The packets are either counted by length, measured in bytes, by inter-
        frame gap to the preceding packet,  also measured in bytes, or by latency in
        transmission measured in nanoseconds.  There are a fixed number of buckets, each
        middle bucket covering a fixed-size range of values which is a power of two.
        The first and last buckets count all the packets that do not fit within the
        ranges of the middle buckets. The buckets are placed at a certain offset by
        specifying the first value that should be counted by the first middle bucket.

        :param start: first value going into the second bucket
        :type start: int
        :param step: the span of each middle bucket:
            (1) 1,2,4,8,16,32,64,128,256,512 (bytes, non-latency histograms).
            (2) 16,32,64,128,...,1048576,2097152 (nanoseconds, latency histograms)
        :type step: int
        :param bucket_count: the total number of buckets
        :type bucket_count: int
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._dataset_xindex],
                start=start,
                step=step,
                bucket_count=bucket_count
            )
        )


@register_command
@dataclass
class PD_SAMPLES:
    """
    The current set of counts collected by a histogram for a port. There is one value
    for each bucket, but any trailing zeros are left out. The list is empty if all
    counts are zero.
    """

    code: typing.ClassVar[int] = 146
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _dataset_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        packet_counts: typing.List[int] = field(XmpSequence(types_chunk=[XmpLong()]))
        """list of long integers, the number of packets counted for each bucket."""

    def get(self) -> Token[GetDataAttr]:
        """Get current set of counts collected by a histogram for a port.

        :return: the number of packets counted for each bucket
        :rtype: PD_SAMPLES.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._dataset_xindex]))
