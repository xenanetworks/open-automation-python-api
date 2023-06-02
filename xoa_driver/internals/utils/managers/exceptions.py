class XoaResourceError(Exception):
    ...


class WrongTesterError(XoaResourceError):
    def __init__(self) -> None:
        self.msg = "Connected tester is of the wrong type!"
        super().__init__(self.msg)


class NoSuchModuleError(XoaResourceError):
    def __init__(self, module_id: int) -> None:
        self.module_id = module_id
        self.msg = f"No such module {module_id}!"
        super().__init__(self.msg)


class NoSuchPortError(XoaResourceError):
    def __init__(self, port_id: int) -> None:
        self.port_id = port_id
        self.msg = f"No such port {port_id}!"
        super().__init__(self.msg)
