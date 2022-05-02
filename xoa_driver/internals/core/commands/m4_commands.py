"""
L47 Module Commands
"""
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
class M4_SYSTEMID:
    """
    Return the system identifier of a L47 module.
    """

    code: typing.ClassVar[int] = 803
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        system_id: XmpField[XmpStr] = XmpField(XmpStr)  # string, module system identifier.

    def get(self) -> "Token[GetDataAttr]":
        """Get the system identifier of a L47 module.

        :return: the system identifier of a L47 module.
        :rtype: M4_SYSTEMID.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M4_VERSIONNO:
    """
    Returns a version string containing a combination of information regarding the
    software version and the build environment. The first part of the string is the
    software build version.
    """

    code: typing.ClassVar[int] = 804
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        version_string: XmpField[XmpStr] = XmpField(XmpStr)  # string, module version string.

    def get(self) -> "Token[GetDataAttr]":
        """Get a version string containing a combination of information regarding the software version and the build environment.

        :return: a version string containing a combination of information regarding the software version and the build environment
        :rtype: M4_VERSIONNO.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M4_SYSTEM_STATUS:
    """
    Returns the L47 module system status in a text string.
    """

    code: typing.ClassVar[int] = 805
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        status_string: XmpField[XmpStr] = XmpField(XmpStr)  # string, module status string.

    def get(self) -> "Token[GetDataAttr]":
        """Get the L47 module system status in a text string

        :return: the L47 module system status in a text string
        :rtype: M4_SYSTEM_STATUS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M4_COMPATIBLE_CLIENT_VERSION:
    """
    Returns the recommended and required VulcanMananger client version.
    """

    code: typing.ClassVar[int] = 806
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        recommended_major: XmpField[XmpInt] = XmpField(XmpInt)  # string, recommended major version.
        recommended_minor: XmpField[XmpInt] = XmpField(XmpInt)  # string, recommended minor version.
        recommended_minor_2: XmpField[XmpInt] = XmpField(XmpInt)  # string, recommended minor 2 version.
        recommended_minor_3: XmpField[XmpInt] = XmpField(XmpInt)  # string, recommended minor 3 version.
        required_major: XmpField[XmpInt] = XmpField(XmpInt)  # string, required major version.
        required_minor: XmpField[XmpInt] = XmpField(XmpInt)  # string, required minor version.
        required_minor_2: XmpField[XmpInt] = XmpField(XmpInt)  # string, required minor 2 version.
        required_minor_3: XmpField[XmpInt] = XmpField(XmpInt)  # string, required minor 3 version.

    def get(self) -> "Token[GetDataAttr]":
        """Get the recommended and required VulcanMananger client version.

        :return: the recommended and required VulcanMananger client version.
        :rtype: M4_COMPATIBLE_CLIENT_VERSION.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M4_TIME:
    """
    Returns the module time in millisecond.
    """

    code: typing.ClassVar[int] = 807
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        time_now: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)

    def get(self) -> "Token[GetDataAttr]":
        """Get the module time in millisecond.

        :return: the module time in millisecond.
        :rtype: M4_TIME.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M4_SYSTEM_TIME:
    """
    Sets or returns the modules system time in UTC.
    """

    code: typing.ClassVar[int] = 808
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        year: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the year.
        month: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the month.
        day: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the day of the mont.
        hour: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the hour.
        minute: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the minute.
        second: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the second.

    @dataclass(frozen=True)
    class GetDataAttr:
        year: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the year.
        month: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the month.
        day: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the day of the mont.
        hour: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the hour.
        minute: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the minute.
        second: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the second.

    def get(self) -> "Token[GetDataAttr]":
        """Get the modules system time in UTC.

        :return: the modules system time in UTC.
        :rtype: M4_SYSTEM_TIME.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))

    def set(self, year: int, month: int, day: int, hour: int, minute: int, second: int) -> "Token":
        """Set the modules system time in UTC.

        :param year: the year
        :type year: int
        :param month: the month
        :type month: int
        :param day: the day of the month
        :type day: int
        :param hour: the hour
        :type hour: int
        :param minute: the minute
        :type minute: int
        :param second: the second
        :type second: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, year=year, month=month, day=day, hour=hour, minute=minute, second=second))


@register_command
@dataclass
class M4_MEM_INFO:
    """
    Return the system memory information.
    """

    code: typing.ClassVar[int] = 809
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        year: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, total memory.
        month: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, free memory.

    def get(self) -> "Token[GetDataAttr]":
        """Get the system memory information.

        :return: the system memory information.
        :rtype: M4_MEM_INFO.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M4_CAPTURE_SIZE:
    """
    Specify whether to capture whole packets(large) or truncated packets. When
    truncated (small) is selected only the first 128 bytes of the packet are saved.
    """

    code: typing.ClassVar[int] = 810
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        size: XmpField[XmpByte] = XmpField(XmpByte, choices=CaptureSize)  # coded byte, specifying whether to capture whole packets or truncated packets.

    @dataclass(frozen=True)
    class GetDataAttr:
        size: XmpField[XmpByte] = XmpField(XmpByte, choices=CaptureSize)  # coded byte, specifying whether to capture whole packets or truncated packets.

    def get(self) -> "Token[GetDataAttr]":
        """Get whether to capture whole packets(large) or truncated packets.

        :return: whether to capture whole packets(large) or truncated packets.
        :rtype: M4_CAPTURE_SIZE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))

    def set(self, size: CaptureSize) -> "Token":
        """Set whether to capture whole packets(large) or truncated packets.

        :param size: specifying whether to capture whole packets or truncated packets.
        :type size: CaptureSize
        """
        return Token(self._connection, build_set_request(self, module=self._module, size=size))

    set_full = functools.partialmethod(set, CaptureSize.FULL)
    """Capture whole packets"""
    set_small = functools.partialmethod(set, CaptureSize.SMALL)
    """Capture truncated packets"""


@register_command
@dataclass
class M4_LICENSE_INFO:
    """
    Returns the number of available and free PE licenses. Only 'available' number of PEs
    can simultaneously be assigned to reserved ports.
    """

    code: typing.ClassVar[int] = 820
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        pes_available: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of PEs that are licensed on the module, and can be used simultaneously.
        pes_free: XmpField[XmpInt] = XmpField(
            XmpInt
        )  # integer, number of free PE licenses on the module 1G available: integer, number of 1G licenses on the module, that can be used simultaneously.
        N1g_available: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of 1G speed licenses that are licensed on the module, and can be used simultaneously.
        N1g_free: XmpField[XmpInt] = XmpField(
            XmpInt
        )  # integer, number of 1G speed licenses on the module 1G available: integer, number of 1G licenses on the module, that can be used simultaneously.
        N10g_available: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of 10G speed licenses that are licensed on the module, and can be used simultaneously.
        N10g_free: XmpField[XmpInt] = XmpField(
            XmpInt
        )  # integer, number of free 10G speed licenses on the module 1G available: integer, number of 1G licenses on the module, that can be used simultaneously.
        N25g_available: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of 25G speed licenses that are licensed on the module, and can be used simultaneously.
        N25g_free: XmpField[XmpInt] = XmpField(
            XmpInt
        )  # integer, number of free 25G speed licenses on the module 1G available: integer, number of 1G licenses on the module, that can be used simultaneously.
        N40g_available: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of 40G speed licenses that are licensed on the module, and can be used simultaneously.
        N40g_free: XmpField[XmpInt] = XmpField(
            XmpInt
        )  # integer, number of free 40G speed licenses on the module 1G available: integer, number of 1G licenses on the module, that can be used simultaneously.

    def get(self) -> "Token[GetDataAttr]":
        """Get the number of available and free PE licenses.

        :return: the number of available and free PE licenses
        :rtype: M4_LICENSE_INFO.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M4_REPLAY_PARSE_START:
    """
    Command to start parsing an uploaded Capture File (in PCAP format) intended for
    use in a replay test scenario. The result of the parsing - if successful - is a
    Replay File (in BSON format) with the same name as the Capture File, which can
    be used as parameter to P4G_REPLAY_filename command. If parsing is unsuccessful,
    a Replay File is created containing the parse result. The
    M4_REPLAY_FILE_INFO_BSON command can be used to get information about a Replay
    File - including the parse result. PCAP Capture Files can be uploaded to the L47
    chassis using FTP. The 'root' location of Capture Files uploaded manually by the
    user is /var/ftp/pub/replay/pcap/. Three subdirectories exist: cache/, user/ and
    xena/. cache / and xena/ is used by Vulcan Manager, and user/ is intended for
    manual upload and parsing of Capture Files. A similar directory structure is
    present for Replay Files generated by the parsing, and the 'root' location is
    /var/ftp/pub/replay/bson/.
    """

    code: typing.ClassVar[int] = 830
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        filename: XmpField[XmpStr] = XmpField(XmpStr)  # string, filename (including relative path and excluding the '.pcap' extension).

    def set(self, filename: str) -> "Token":
        """Start parsing an uploaded Capture File

        :param filename: filename (including relative path and excluding the '.pcap' extension).
        :type filename: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, filename=filename))


@register_command
@dataclass
class M4_REPLAY_PARSE_STOP:
    """
    Command to stop parsing a Capture File. Parsing of very large Capture Files may
    take several seconds, and may be aborted using this command. No parameters
    """

    code: typing.ClassVar[int] = 831
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Stop parsing a Capture File.
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
            ),
        )


@register_command
@dataclass
class M4_REPLAY_PARSE_STATE:
    """
    Only one Capture File can be parsed at a time. This command returns the state of
    the parser, which can be PARSING or OFF. M4_REPLAY_PARSE_START command is only
    accepted when the parser state is OFF.
    """

    code: typing.ClassVar[int] = 832
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        state: XmpField[XmpByte] = XmpField(XmpByte, choices=ReplayParserState)  # coded byte, state of the replay parser

    def get(self) -> "Token[GetDataAttr]":
        """Get capture file parsing state.

        :return: capture file parsing state
        :rtype: M4_REPLAY_PARSE_STATE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M4_REPLAY_PARSER_PARAMS:
    """
    Configuration of parameters for the parsing of pcap files.
    """

    code: typing.ClassVar[int] = 833
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        tcp_port: XmpField[XmpInt] = XmpField(XmpInt)  # integer, server TCP Port of dummy TCP connection inserted in UDP only replay files

    @dataclass(frozen=True)
    class GetDataAttr:
        tcp_port: XmpField[XmpInt] = XmpField(XmpInt)  # integer, server TCP Port of dummy TCP connection inserted in UDP only replay files

    def get(self) -> "Token[GetDataAttr]":
        """Get the configuration of parameters for the parsing of pcap files.

        :return: the configuration of parameters for the parsing of pcap files
        :rtype: M4_REPLAY_PARSER_PARAMS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))

    def set(self, tcp_port: int) -> "Token":
        """Set the configuration of parameters for the parsing of pcap files.

        :param tcp_port: server-side TCP port of the dummy TCP connection inserted in UDP.
        :type tcp_port: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, tcp_port=tcp_port))


@register_command
@dataclass
class M4_REPLAY_FILE_LIST_BSON:
    """
    Works as ``M4_REPLAY_FILE_LIST``, but returns the file list formatted as a BSON
    document.
    """

    code: typing.ClassVar[int] = 840
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        bson: XmpField[XmpByteList] = XmpField(XmpByteList)  # list of hex bytes, bson document containing the file list

    def get(self) -> "Token[GetDataAttr]":
        """Get the replay file list in BSON document format.

        :return: the replay file list in BSON format
        :rtype: M4_REPLAY_FILE_LIST_BSON.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M4_REPLAY_FILE_LIST:
    """
    Returns a list of Replay Files (``.bson`` files) in the 'user' Replay File
    directory (``/var/ftp/pub/replay/bson/user/``).
    """

    code: typing.ClassVar[int] = 841
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        file_list: XmpField[XmpStr] = XmpField(XmpStr)  # string, comma separated list of filenames excluding the '.bson' extension.

    def get(self) -> "Token[GetDataAttr]":
        """Generate a list of Replay Files in BSON document on the tester.

        :return: a list of Replay Files in BSON document on the tester
        :rtype: M4_REPLAY_FILE_LIST.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M4_CAPTURE_FILE_LIST_BSON:
    """
    Works as ``M4_CAPTURE_FILE_LIST``, but returns the file list formatted as a BSON
    document.
    """

    code: typing.ClassVar[int] = 842
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        bson: XmpField[XmpByteList] = XmpField(XmpByteList)  # list of hex bytes, bson document containing the file list

    def get(self) -> "Token[GetDataAttr]":
        """Get the capture file list in BSON document.

        :return: the capture file list in BSON document
        :rtype: M4_CAPTURE_FILE_LIST_BSON.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M4_CAPTURE_FILE_LIST:
    """
    Returns a list of Capture Files (``.pcap`` files) in the 'user' Capture File
    directory (``/var/ftp/pub/replay/pcap/user/``).
    """

    code: typing.ClassVar[int] = 843
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        file_list: XmpField[XmpStr] = XmpField(XmpStr)  # string, comma separated list of filenames excluding the '.pcap' extension.

    def get(self) -> "Token[GetDataAttr]":
        """Generate a list of Capture Files in BSON document on the tester.

        :return: list of Capture Files in BSON document on the tester
        :rtype: M4_CAPTURE_FILE_LIST.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M4_REPLAY_FILE_DELETE:
    """
    Command to delete a Replay File (``.bson`` file) in the Replay File directory
    (``/var/ftp/pub/replay/bson/``). For information about the location and directory
    structure for the Replay Files, see: M4_REPLAY_PARSE_START
    """

    code: typing.ClassVar[int] = 845
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        filename: XmpField[XmpStr] = XmpField(XmpStr)  # string, file name (including relative path and excluding the '.bson' extension).

    def set(self, filename: str) -> "Token":
        """Delete a Replay File in the Replay File directory.

        :param filename: file name (including relative path and excluding the ``.bson`` extension).
        :type filename: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, filename=filename))


@register_command
@dataclass
class M4_CAPTURE_FILE_DELETE:
    """
    Command to delete a Capture File (``.pcap`` file) in the Capture File directory
    (``/var/ftp/pub/replay/pcap/``). For information about the location and directory
    structure for the Capture Files, see: M4_REPLAY_PARSE_START
    """

    code: typing.ClassVar[int] = 846
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        filename: XmpField[XmpStr] = XmpField(XmpStr)  # string, file name (including relative path and excluding the '.pcap' extension).

    def set(self, filename: str) -> "Token":
        """Delete a Capture File in the Capture File directory.

        :param filename: file name (including relative path and excluding the ``.pcap`` extension).
        :type filename: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, filename=filename))


@register_command
@dataclass
class M4_TLS_CIPHER_SUITES:
    """
    Returns a list of supported TLS Cipher Suites.
    """

    code: typing.ClassVar[int] = 852
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        cipher_suites: XmpField[XmpHexList] = XmpField(XmpHexList)  # list of hex bytes, list of IANA values of supported cipher suites

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of supported TLS Cipher Suites.

        :return: list of IANA values of supported cipher suites
        :rtype: M4_TLS_CIPHER_SUITES.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


