from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    P4G_TIME_HIST_CONF,
    P4G_PAYLOAD_HIST_CONF,
    P4G_TRANSACTION_HIST_CONF,
    P4G_APP_TRANSACTION_HIST,
    P4G_RECALC_TIME_HIST,
    P4G_RECALC_PAYLOAD_HIST,
    P4G_RECALC_TRANSACTION_HIST,
)


class GConfigHistogram:
    """L47 Histogram Config"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.time = P4G_TIME_HIST_CONF(conn, module_id, port_id, group_idx)
        """Sets the start value and the interval size for the time histograms
        
        :type: P4G_TIME_HIST_CONF
        """

        self.payload = P4G_PAYLOAD_HIST_CONF(conn, module_id, port_id, group_idx)
        """Sets the start value and the interval size for the payload histograms.
        
        :type: P4G_PAYLOAD_HIST_CONF
        """

        self.transaction = P4G_TRANSACTION_HIST_CONF(conn, module_id, port_id, group_idx)
        """Sets the start value and the interval size for the transaction histogram.
        
        :type: P4G_TRANSACTION_HIST_CONF
        """


class GRecalculatesHistogram:
    """L47 Histogram Recalculation."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.time = P4G_RECALC_TIME_HIST(conn, module_id, port_id, group_idx)
        """Recalculates connection time histograms
        
        :type: P4G_RECALC_TIME_HIST
        """

        self.payload = P4G_RECALC_PAYLOAD_HIST(conn, module_id, port_id, group_idx)
        """Recalculates connection payload histograms
        
        :type: P4G_RECALC_PAYLOAD_HIST
        """

        self.transaction = P4G_RECALC_TRANSACTION_HIST(conn, module_id, port_id, group_idx)
        """Recalculates transaction histograms
        
        :type: P4G_RECALC_TRANSACTION_HIST
        """


class GHistogram:
    """L47 Histogram."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.transaction = P4G_APP_TRANSACTION_HIST(conn, module_id, port_id, group_idx)
        """Returns a histogram over completed request/response transactions per connection.
        
        :type: P4G_APP_TRANSACTION_HIST
        """

        self.recalculates = GRecalculatesHistogram(conn, module_id, port_id, group_idx)
        """L47 Histogram Recalculation.
        
        :type: GRecalculatesHistogram
        """
        
        self.config = GConfigHistogram(conn, module_id, port_id, group_idx)
        """L47 Histogram Config
        
        :type: GConfigHistogram
        """
