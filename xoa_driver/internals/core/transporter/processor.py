from __future__ import annotations
import asyncio
from typing import Generator, Protocol, Type
from ..protocol.command_builders import build_from_bytes
from ..registry import get_command

class Stream(Protocol):
    async def read(self) -> Generator[tuple, None, None]:
        ...


class PacketsProcessor:

    def __init__(self, stream: Stream) -> None:
        self.__stream = stream
        self.__evt_do_job = asyncio.Event()
        self.__consumer: asyncio.Task | None = None

    @property
    def is_running(self) -> bool:
        return not (self.__consumer is None or self.__consumer.done())

    def start(self) -> None:
        if self.is_running:
            return None
        self.__evt_do_job.set()
        self.__consumer = asyncio.create_task(self.__consume())
        # self.__consumer.add_done_callback(self.__handle_exceptions)

    def stop(self) -> None:
        if not self.is_running:
            return None
        self.__evt_do_job.clear()
        self.__consumer.cancel()  # type: ignore[ReportOptionalMemberAccess]
        self.__consumer = None

    async def __consume(self) -> None:
        async for header, body_bytes in self.__stream.read():
            print(header, body_bytes)
            response = self.__serialize_to_response(header, body_bytes)
            if response.header.is_pushed:
                self.__handle_push_response(response)
            else:
                self.__handle_param_response(response)
            if not self.__evt_do_job.is_set():
                return None


    # def __handle_exceptions(self, fut: "asyncio.Future") -> None:
    #     if e := fut.exception():
    #         print(e)

    # def __handle_push_response(self, response: Response) -> None:
    #     # self.__log.push_obj(response)
    #     self.events_observer.dispatch(
    #         response.header.cmd_code,
    #         response
    #     )

    # def __handle_param_response(self, response: Response) -> None:
    #     # self.__log.response_obj(response)
    #     future = self.cmd_mngr.get_result_future(response)
    #     if not future:
    #         raise t_ex.LostFuture(response)
    #     if not response.is_ok:
    #         future.set_exception(t_ex.BadStatus(response))
    #     else:
    #         future.set_result(response.values)

    # async def process_data(self, header, data: memoryview) -> None:
    #     try:
    #         response = await self.__serialize_to_response(header, data)
    #     except t_ex.RepeatedRequestID as e:
    #         self.__log.error(f"{e} Original Data: {data}")
    #     else:
    #         if response.header.is_pushed:
    #             self.__handle_push_response(response)
    #         else:
    #             self.__handle_param_response(response)

    def __serialize_to_response(self, header, body_bytes: bytearray) -> Response:
        """Applying received bytes to structured representation."""

        command_idx: int | None = (
            header.cmd_code
            if header.is_pushed
            else self.cmd_mngr.get_command_handler_id(
                header.request_identifier
            )
        )
        if not command_idx:
            raise t_ex.RepeatedRequestID(header)
        xmc_type = get_command(command_idx)
        return build_from_bytes(xmc_type, header, body_bytes)
        # xmc_type: Type[x_types.CMD_TYPE] | None = self.commands_registry.get(command_idx, None)
        # if not xmc_type:
        #     raise t_ex.NotImplementedCommand(header)
        
        
