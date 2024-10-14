class WrongTesterError(Exception):
    """Tester you are trying to connect is of a different type"""
    def __init__(self) -> None:
        self.msg = "Tester you are trying to connect is of a different type."
        super().__init__(self.msg)


class WrongTesterPasswordError(Exception):
    """Cannot create session on the tester because the password is incorrect"""
    def __init__(self, password: str) -> None:
        self.password = password
        self.msg = "Can't create session on the tester because the password is incorrect."
        super().__init__(self.msg)


class UnsupportedFirmwareError(Exception):
    """Testers firmware version is too old"""
    def __init__(self, version: float) -> None:
        self.version = version
        self.msg = f"Testers firmware version is too old, current: {self.version}. Minimum required: 446.5"
        super().__init__(self.msg)
