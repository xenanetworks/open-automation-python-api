from typing import (
    NamedTuple,
    Type,
    TypeVar,
)
from xoa_driver.internals.core.commands import P_CAPABILITIES

T = TypeVar("T", bound="CapID")

class CapID(NamedTuple):
    """ID generated based on the port capability"""
    
    can_set_autoneg: int
    can_eee: int
    can_hw_reg_access: int
    can_tcvr_mii_reg_access: int
    can_adv_phy_man: int
    can_mdi_mdix: int
    can_dyn_traffic_change: int
    can_pcs_pma_config: int
    can_fec: int
    can_fec_stats: int
    can_tx_eq: int
    can_rx_retune: int
    can_manipulate_preamble: int
    can_set_link_train: int
    can_link_flap: int
    can_auto_neg_base_r: int
    can_pma_error_pulse: int
    
    @classmethod
    def create_from_capabilities(cls: Type[T], cap: P_CAPABILITIES.GetDataAttr) -> T:
        return cls(
            int(cap.can_set_autoneg),
            int(cap.can_eee),
            int(cap.can_hw_reg_access),
            int(cap.can_tcvr_mii_reg_access),
            int(cap.can_adv_phy_man),
            int(cap.can_mdi_mdix),
            int(cap.can_dyn_traffic_change),
            int(cap.can_pcs_pma_config),
            int(cap.can_fec),
            int(cap.can_fec_stats),
            int(cap.can_tx_eq),
            int(cap.can_rx_retune),
            int(cap.can_manipulate_preamble),
            int(cap.can_set_link_train),
            int(cap.can_link_flap),
            int(cap.can_auto_neg_base_r),
            int(cap.can_pma_error_pulse),
        )
    
    def to_int(self) -> int:
        return int("".join(str(ele) for ele in self), 2)
    
    def __eq__(self, other: "CapID") -> bool:
        if isinstance(other, CapID):
            return self.to_int() == other.to_int()
        return False
    
    def __ne__(self, other: "CapID") -> bool:
        return not self.__eq__(other)