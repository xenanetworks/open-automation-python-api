from __future__ import annotations
from typing import Type
from ._constants import CommandStatus


class XmpStatusException(Exception):
    __slots__ = ("err_code", "msg", "cmd",)

    err_code: CommandStatus | None
    msg: str
    cmd: str


class XmpNoConnectionError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOCONNECTIONS
        self.msg = "Chassis has no available connection slots"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpNoLoggedOnError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOTLOGGEDON
        self.msg = "No command can be submitted before logon"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpNotReservedError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOTRESERVED
        self.msg = "Parameter cannot be set because containing resource not reserved"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpNotWritableError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOTWRITABLE
        self.msg = "Parameter cannot be set because it is not in a writable state"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpNotReadableError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOTREADABLE
        self.msg = "Parameter is write-only"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpNotValidError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOTVALID
        self.msg = "Operation not valid in current state"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpBadHeaderError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADHEADER
        self.msg = "Invalid magic word"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpBadCommandError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADCOMMAND
        self.msg = "Invalid command"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpBadParameterError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADPARAMETER
        self.msg = "Invalid parameter code"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpBadModuleError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADMODULE
        self.msg = "Invalid module index"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpBadPortError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADPORT
        self.msg = "Invalid port index"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpBadIndexError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADINDEX
        self.msg = "Invalid parameter index"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpBadSizeError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADSIZE
        self.msg = "Invalid size of data"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpBadValueError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADVALUE
        self.msg = "Invalid value of data"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpFailedError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.FAILED
        self.msg = "Failed to perform operation"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpMemoryFailureError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.MEMORYFAILURE
        self.msg = "Failed to allocate memory"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpNoPeLicenseError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOLICPE
        self.msg = "No free PE license"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpNoFreePortLicenseError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOLICPORT
        self.msg = "No free Port license"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpNotSupportedError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOTSUPPORTED
        self.msg = "Feature not supported"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpPendingError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.PENDING
        self.msg = "Status return will wait until command has been executed"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpModuleOperationNotSupportedByChassisError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.MODULE_OPERATION_NOT_SUPPORTED_BY_CHASSIS
        self.msg = "module is not supported by chassis - e.g. because multi-image requires x64 OS."
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpXlsFailedError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.XLSFAILED
        self.msg = "Could not establish connection to Xena License Server"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpXlsDeniedError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.XLSDENIED
        self.msg = "Request for resource rejected by Xena License Server"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpXlsInvalidError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.XLSINVALID
        self.msg = "Trying to run Valkyrie VE with VulcanVE-300 resource"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpUnknownError(XmpStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = None
        self.msg = "Unknown XOA status"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


__EXCEPTIONS_MAP = {
    CommandStatus.NOCONNECTIONS: XmpNoConnectionError,
    CommandStatus.NOTLOGGEDON: XmpNoLoggedOnError,
    CommandStatus.NOTRESERVED: XmpNotReservedError,
    CommandStatus.NOTWRITABLE: XmpNotWritableError,
    CommandStatus.NOTREADABLE: XmpNotReadableError,
    CommandStatus.NOTVALID: XmpNotValidError,
    CommandStatus.BADHEADER: XmpBadHeaderError,
    CommandStatus.BADCOMMAND: XmpBadCommandError,
    CommandStatus.BADPARAMETER: XmpBadParameterError,
    CommandStatus.BADMODULE: XmpBadModuleError,
    CommandStatus.BADPORT: XmpBadPortError,
    CommandStatus.BADINDEX: XmpBadIndexError,
    CommandStatus.BADSIZE: XmpBadSizeError,
    CommandStatus.BADVALUE: XmpBadValueError,
    CommandStatus.FAILED: XmpFailedError,
    CommandStatus.MEMORYFAILURE: XmpMemoryFailureError,
    CommandStatus.NOLICPE: XmpNoPeLicenseError,
    CommandStatus.NOLICPORT: XmpNoFreePortLicenseError,
    CommandStatus.NOTSUPPORTED: XmpNotSupportedError,
    CommandStatus.PENDING: XmpPendingError,
    CommandStatus.MODULE_OPERATION_NOT_SUPPORTED_BY_CHASSIS: XmpModuleOperationNotSupportedByChassisError,
    CommandStatus.XLSFAILED: XmpXlsFailedError,
    CommandStatus.XLSDENIED: XmpXlsDeniedError,
    CommandStatus.XLSINVALID: XmpXlsInvalidError
}


def get_status_error(cmd_status: CommandStatus | None) -> Type[XmpStatusException]:
    global __EXCEPTIONS_MAP
    if cmd_status is None:
        return XmpUnknownError
    return __EXCEPTIONS_MAP.get(cmd_status, XmpUnknownError)
