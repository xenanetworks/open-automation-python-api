class WrongTesterError(Exception):
    def __init__(self) -> None:
        self.msg = "Tester you are trying to connect is of a different type."
        super().__init__(self.msg)

class WrongTesterPasswordError(Exception):
    def __init__(self, password: str) -> None:
        self.password = password
        self.msg = f"Can't create session on the tester because the password is incorrect."
        super().__init__(self.msg)

