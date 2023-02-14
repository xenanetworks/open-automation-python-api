from __future__ import annotations

from xoa_driver.ports import GenericAnyPort
from xoa_driver.internals.core import interfaces as itf


def _get_ctx(port: GenericAnyPort) -> tuple["itf.IConnection", int, int]:
    return port._conn, port.kind.module_id, port.kind.port_id
