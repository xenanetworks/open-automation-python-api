from __future__ import annotations
from typing import Type
from ._constants import CommandStatus


class XmpStatusException(Exception):
    __slots__ = ("err_code", "msg", "cmd",)

    err_code: CommandStatus | None
    msg: str
    cmd: str


class XmpNoConnectionError(XmpStatusException):
    """Chassis has no available connection slots (NOCONNECTIONS)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOCONNECTIONS
        self.msg = f"Chassis has no available connection slots ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpNoLoggedOnError(XmpStatusException):
    """No command can be submitted before logon (NOTLOGGEDON)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOTLOGGEDON
        self.msg = f"No command can be submitted before logon ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpNotReservedError(XmpStatusException):
    """Command cannot be set because resource not reserved (NOTRESERVED)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOTRESERVED
        self.msg = f"Command cannot be set because resource not reserved ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpNotWritableError(XmpStatusException):
    """Command cannot be set because it is not in a writable state (NOTWRITABLE)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOTWRITABLE
        self.msg = f"Command cannot be set because it is not in a writable state ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpNotReadableError(XmpStatusException):
    """Command is write-only (NOTREADABLE)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOTREADABLE
        self.msg = f"Command is write-only ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpNotValidError(XmpStatusException):
    """Operation not valid in current state (NOTVALID)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOTVALID
        self.msg = f"Operation not valid in current state ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpBadHeaderError(XmpStatusException):
    """Invalid magic word (BADHEADER)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADHEADER
        self.msg = f"Invalid magic word ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpBadCommandError(XmpStatusException):
    """Invalid command (BADCOMMAND)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADCOMMAND
        self.msg = f"Invalid command ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpBadParameterError(XmpStatusException):
    """Invalid command code (BADPARAMETER)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADPARAMETER
        self.msg = f"Invalid command code ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpBadModuleError(XmpStatusException):
    """Bad module index (BADMODULE)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADMODULE
        self.msg = f"Bad module index ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpBadPortError(XmpStatusException):
    """Bad port index (BADPORT)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADPORT
        self.msg = f"Bad port index ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpBadIndexError(XmpStatusException):
    """Bad index (BADINDEX)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADINDEX
        self.msg = f"Bad index ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpBadSizeError(XmpStatusException):
    """Invalid data size (BADSIZE)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADSIZE
        self.msg = f"Invalid data size ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpBadValueError(XmpStatusException):
    """Invalid data value (BADVALUE)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.BADVALUE
        self.msg = f"Invalid data value ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpFailedError(XmpStatusException):
    """Failed to perform operation (FAILED)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.FAILED
        self.msg = f"Failed to perform operation ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpMemoryFailureError(XmpStatusException):
    """Failed to allocate memory (MEMORYFAILURE)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.MEMORYFAILURE
        self.msg = f"Failed to allocate memory ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpNoPeLicenseError(XmpStatusException):
    """o free PE license (NOLICPE)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOLICPE
        self.msg = f"No free PE license ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpNoFreePortLicenseError(XmpStatusException):
    """No free Port license (NOLICPORT)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOLICPORT
        self.msg = f"No free Port license ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpNotSupportedError(XmpStatusException):
    """Command not supported (NOTSUPPORTED)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.NOTSUPPORTED
        self.msg = f"Command not supported ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpPendingError(XmpStatusException):
    """Status return will wait until command has been execute (PENDING)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.PENDING
        self.msg = f"Pending status reply until command has been executed ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpModuleOperationNotSupportedByChassisError(XmpStatusException):
    """Module not supported by chassis (MODULE_OPERATION_NOT_SUPPORTED_BY_CHASSIS)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.MODULE_OPERATION_NOT_SUPPORTED_BY_CHASSIS
        self.msg = f"Module not supported by chassis ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpXlsFailedError(XmpStatusException):
    """Could not establish connection to Xena License Server (XLSFAILED)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.XLSFAILED
        self.msg = f"Could not establish connection to Xena License Server ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpXlsDeniedError(XmpStatusException):
    """Request for resource rejected by Xena License Server (XLSDENIED)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.XLSDENIED
        self.msg = f"Request for resource rejected by Xena License Server ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpXlsInvalidError(XmpStatusException):
    """Trying to run Valkyrie VE with VulcanVE-300 resource (XLSINVALID)"""
    def __init__(self, cmd) -> None:
        self.err_code = CommandStatus.XLSINVALID
        self.msg = f"Trying to run Valkyrie VE with VulcanVE-300 resource ({self.err_code.name})"
        self.cmd = cmd
        super().__init__(f"{self.cmd}: {self.msg}")


class XmpUnknownError(XmpStatusException):
    """Unknown XOA status (None)"""
    def __init__(self, cmd) -> None:
        self.err_code = None
        self.msg = f"Unknown XOA status (None)"
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
