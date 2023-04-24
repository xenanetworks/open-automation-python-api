class WrongTesterError(Exception):
    def __init__(self) -> None:
        self.msg = "Tester you are trying to connect is of a different type."
        super().__init__(self.msg)


class WrongTesterPasswordError(Exception):
    def __init__(self, password: str) -> None:
        self.password = password
        self.msg = "Can't create session on the tester because the password is incorrect."
        super().__init__(self.msg)


class UnsuportedFirmwareError(Exception):
    def __init__(self, version: float) -> None:
        self.version = version
        self.msg = f"Testers firmware version is to old, current: {self.version} Min required: 446.5"
        super().__init__(self.msg)
