from __future__ import annotations


class XoaException(Exception):
    ...


class TransporterException(XoaException):
    ...


class XoaConnectionTimeoutError(XoaException):
    def __init__(self, host: str, port: int, seconds_timeout: int) -> None:
        self.host = host
        self.port = port
        self.seconds_timeout = seconds_timeout
        self.msg = f"Can't establish the connect to {host}:{port}, in period of {seconds_timeout} sec."
        super().__init__(self.msg)


class XoaConnectionError(XoaException):
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.msg = f"Can't connect to {host}:{port}"
        super().__init__(self.msg)


class RepeatedRequestID(TransporterException):
    def __init__(self, request_identifier: int,) -> None:
        self.msg = f"""
        Got repeated request id {request_identifier}.
        This is a bug of xenaserver returning the same request identifier twice.
        """
        self.request_identifier = request_identifier
        super().__init__(self.msg)


class XoaLostFuture(XoaException):
    def __init__(self, req_id: int, cls_name: str) -> None:
        self.req_id = req_id
        self.cls_name = cls_name
        self.msg = f"Command was sent but the response handler was not registered {req_id} {cls_name}."
        super().__init__(self.msg)
