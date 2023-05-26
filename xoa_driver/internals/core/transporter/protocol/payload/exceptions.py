from __future__ import annotations


class XmpException(Exception):
    ...


class FirmwareVersionError(XmpException):
    def __init__(self, cmd_name: str, field_name: str, min_version: int | None) -> None:
        self.cmd_name = cmd_name
        self.field_name = field_name
        self.min_version = min_version
        self.msg = f"The field: [{self.field_name}] of command {self.cmd_name} is available only from the firmware version: {self.min_version}"
        super().__init__(self.msg)


class FieldDeclarationError(TypeError):
    def __init__(self, f_name: str) -> None:
        self.msg = f"Structure Field {f_name!r} must be described with <field method>"
        super().__init__(self.msg)
