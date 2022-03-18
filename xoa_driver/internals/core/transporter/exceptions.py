from .. import protocol

class EstablishConnectionError(Exception):
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.msg = f"Can't connect to {host}:{port}"
        super().__init__(self.msg)

class BadStatus(Exception):
    def __init__(self, response: protocol.Response) -> None:
        self.msg = f"Bad status {response.command_status!r} of {response.class_name}!\n{response}"
        self.response = response
        super().__init__(self.msg)


class NotImplementedCommand(Exception):
    def __init__(self, header: protocol.ResponseHeader) -> None:
        self.msg = f"Server sending command which is not implemented {header.cmd_code}."
        self.response_header = header
        super().__init__(self.msg)


class RepeatedRequestID(Exception):
    def __init__(self, header: protocol.ResponseHeader) -> None:
        self.msg = f"""
        Got repeated request id {header.request_identifier}, {header}. 
        This is a bug of xenaserver returning the same request identifier twice.
        """ 
        self.response_header = header
        super().__init__(self.msg)


class LostFuture(Exception):
    def __init__(self, response: protocol.Response) -> None:
        self.msg = f"Lost Future {response.header.request_identifier} {response.class_name}."
        self.response = response
        super().__init__(self.msg)


# class TooShortData(Exception):
#     def __init__(self, data: bytes) -> None:
#         self.data = data
#         self.msg = f"{data} is too short."
#         super().__init__(self.msg)