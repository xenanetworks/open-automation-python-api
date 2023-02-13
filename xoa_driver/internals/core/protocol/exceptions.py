from __future__ import annotations
from typing import Type
from .constants import CommandStatus


class XoaStatusException(Exception):
    err_code: CommandStatus | None
    msg: str
    cmd: str


class XoaNoConnectionError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOCONNECTIONS
        self.msg = "Chassis has no available connection slots"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaNoLoggedOnError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOTLOGGEDON
        self.msg = "No command can be submitted before logon"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaNotReservedError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOTRESERVED
        self.msg = "Parameter cannot be set because containing resource not reserved"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaNotWritableError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOTWRITABLE
        self.msg = "Parameter cannot be set because it is not in a writable state"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaNotReadableError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOTREADABLE
        self.msg = "Parameter is write-only"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaNotValidError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOTVALID
        self.msg = "Operation not valid in current state"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaBadHeaderError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADHEADER
        self.msg = "Invalid magic word"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaBadCommandError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADCOMMAND
        self.msg = "Invalid command"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaBadParameterError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADPARAMETER
        self.msg = "Invalid parameter code"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaBadModuleError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADMODULE
        self.msg = "Invalid module index"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaBadPortError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADPORT
        self.msg = "Invalid port index"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaBadIndexError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADINDEX
        self.msg = "Invalid parameter index"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaBadSizeError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADSIZE
        self.msg = "Invalid size of data"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaBadValueError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADVALUE
        self.msg = "Invalid value of data"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaFailedError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.FAILED
        self.msg = "Failed to perform operation"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaMemoryFailureError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.MEMORYFAILURE
        self.msg = "Failed to allocate memory"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaNoPeLicenseError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOLICPE
        self.msg = "No free PE license"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaNoFreePortLicenseError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOLICPORT
        self.msg = "No free Port license"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaNotSupportedError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOTSUPPORTED
        self.msg = "Feature not supported"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaPendingError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.PENDING
        self.msg = "Status return will wait until command has been executed"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaModuleOperationNotSupportedByChassisError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.MODULE_OPERATION_NOT_SUPPORTED_BY_CHASSIS
        self.msg = "module is not supported by chassis - e.g. because multi-image requires x64 OS."
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaXlsFailedError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.XLSFAILED
        self.msg = "Could not establish connection to Xena License Server"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaXlsDeniedError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.XLSDENIED
        self.msg = "Request for resource rejected by Xena License Server"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaXlsInvalidError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.XLSINVALID
        self.msg = "Trying to run Valkyrie VE with VulcanVE-300 resource"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XoaUnknownError(XoaStatusException):
    def __init__(self, cmd) -> None:
        self.err_code = None
        self.msg = "Unknown XOA status"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


__EXCEPTIONS_MAP = {
    CommandStatus.NOCONNECTIONS: XoaNoConnectionError,
    CommandStatus.NOTLOGGEDON: XoaNoLoggedOnError,
    CommandStatus.NOTRESERVED: XoaNotReservedError,
    CommandStatus.NOTWRITABLE: XoaNotWritableError,
    CommandStatus.NOTREADABLE: XoaNotReadableError,
    CommandStatus.NOTVALID: XoaNotValidError,
    CommandStatus.BADHEADER: XoaBadHeaderError,
    CommandStatus.BADCOMMAND: XoaBadCommandError,
    CommandStatus.BADPARAMETER: XoaBadParameterError,
    CommandStatus.BADMODULE: XoaBadModuleError,
    CommandStatus.BADPORT: XoaBadPortError,
    CommandStatus.BADINDEX: XoaBadIndexError,
    CommandStatus.BADSIZE: XoaBadSizeError,
    CommandStatus.BADVALUE: XoaBadValueError,
    CommandStatus.FAILED: XoaFailedError,
    CommandStatus.MEMORYFAILURE: XoaMemoryFailureError,
    CommandStatus.NOLICPE: XoaNoPeLicenseError,
    CommandStatus.NOLICPORT: XoaNoFreePortLicenseError,
    CommandStatus.NOTSUPPORTED: XoaNotSupportedError,
    CommandStatus.PENDING: XoaPendingError,
    CommandStatus.MODULE_OPERATION_NOT_SUPPORTED_BY_CHASSIS: XoaModuleOperationNotSupportedByChassisError,
    CommandStatus.XLSFAILED: XoaXlsFailedError,
    CommandStatus.XLSDENIED: XoaXlsDeniedError,
    CommandStatus.XLSINVALID: XoaXlsInvalidError
}


def get_status_error(cmd_status: CommandStatus) -> Type[XoaStatusException]:
    global __EXCEPTIONS_MAP
    return __EXCEPTIONS_MAP.get(cmd_status, XoaUnknownError)
