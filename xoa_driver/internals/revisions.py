from __future__ import annotations
from enum import Enum
from functools import partial
from typing import Type


class ProductType(Enum):
    VALKYRIE = "VAL_MOD"
    CHIMERA = "CHI_MOD"
    VULCAN = "VUL_MOD"


VALKYRIE_MODULES = {}
CHIMERA_MODULES = {}
VULCAN_MODULES = {}


class RegisterModule:
    """Register revision and it's module class"""

    def __init__(self, product_type: ProductType, rev: str):
        self.product_type = product_type
        self.revision = rev

    def __call__(self, module_type: Type):
        global VALKYRIE_MODULES, CHIMERA_MODULES, VULCAN_MODULES
        store_method = {
            ProductType.VALKYRIE: partial(self.set_module, storage=VALKYRIE_MODULES),
            ProductType.CHIMERA: partial(self.set_module, storage=CHIMERA_MODULES),
            ProductType.VULCAN: partial(self.set_module, storage=VULCAN_MODULES),
        }.get(self.product_type)
        if not store_method:
            raise ValueError("Unknow product.")
        store_method(revision=self.revision, module_type=module_type)
        return module_type

    @staticmethod
    def set_module(storage: dict[str, Type], revision: str, module_type: Type) -> None:
        if revision in storage:
            raise RuntimeError(f"Module of revision: {revision}, is already registered.")
        storage[revision] = module_type


register_valkyrie_module = partial(RegisterModule, product_type=ProductType.VALKYRIE)
register_chimera_module = partial(RegisterModule, product_type=ProductType.CHIMERA)
register_vulcan_module = partial(RegisterModule, product_type=ProductType.VULCAN)

# # region Valkyrie Modules, sorting order: alphabetical

# VALKYRIE_MODULES = {
#     # family_d
#     "Odin-1G-3S-2P-T": modules.MOdin1G3S2PT,
#     "Odin-1G-3S-6P": modules.MOdin1G3S6P,
#     "Odin-1G-3S-6P[b]": modules.MOdin1G3S6P_b,
#     "Odin-1G-3S-6P-E": modules.MOdin1G3S6PE,

#     # family_m
#     "Odin-1G-3S-6P-T1-RJ45": modules.MOdin1G3S6PT1RJ45,

#     # family_e
#     "Odin-5G-4S-6P-CU": modules.MOdin5G4S6PCU,

#     # family_f
#     "Odin-10G-1S-2P": modules.MOdin10G1S2P,
#     "Odin-10G-1S-2P[b]": modules.MOdin10G1S2P_b,
#     "Odin-10G-1S-2P[c]": modules.MOdin10G1S2P_c,
#     "Odin-10G-1S-2P[d]": modules.MOdin10G1S2P_d,
#     "Odin-10G-1S-2P-T": modules.MOdin10G1S2PT,
#     "Odin-10G-1S-6P": modules.MOdin10G1S6P,
#     "Odin-10G-1S-6P[b]": modules.MOdin10G1S6P_b,
#     "Odin-10G-1S-12P": modules.MOdin10G1S12P,

#     # family_e
#     "Odin-10G-3S-2P-CU": modules.MOdin10G3S2PCU,
#     "Odin-10G-3S-6P-CU": modules.MOdin10G3S6PCU,

#     "Odin-10G-5S-6P-CU": modules.MOdin10G5S6PCU,
#     "Odin-10G-5S-6P-CU[b]": modules.MOdin10G5S6PCU_b,

#     # family_combi
#     "Odin-10G-4S-2P-Combi": modules.MOdin10G4S2PCombi,
#     "Odin-10G-4S-2P-Combi[b]": modules.MOdin10G4S2PCombi_b,

#     # family_n
#     "Odin-40G-2S-2P": modules.MOdin40G2S2P,
#     "Odin-40G-2S-2P-B": modules.MOdin40G2S2PB,

#     # family_h
#     "Odin-100G-3S-1P": modules.MThor400G7S1P_d,

#     # family_g
#     "Loki-100G-3S-1P": modules.MLoki100G3S1P,
#     "Loki-100G-3S-1P[b]": modules.MLoki100G3S1P_b,
#     "Loki-100G-3S-1P-SE": modules.MLoki100G3S1PSE,

#     # family_h
#     "Loki-100G-5S-1P": modules.MLoki100G5S1P,

#     # family_i
#     "Loki-100G-5S-2P": modules.MLoki100G5S2P,

#     # family_j
#     "Thor-100G-5S-4P": modules.MThor100G5S4P,

#     # family_k
#     "Thor-400G-7S-1P": modules.MThor400G7S1P,

#     # family_l
#     "Thor-400G-7S-1P[b]": modules.MThor400G7S1P_b,
#     "Thor-400G-7S-1P[c]": modules.MThor400G7S1P_c,
#     "Thor-400G-7S-1P[d]": modules.MThor400G7S1P_d,

#     # family_l1
#     "Freya-800G-1S-1P[a]": modules.MFreya800G1S1P_a,
#     "Freya-800G-1S-1P[b]": modules.MFreya800G1S1P_b,
#     "Freya-800G-1S-1P-OSFP[a]": modules.MFreya800G1S1POSFP_a,
#     "Freya-800G-4S-1P[a]": modules.MFreya800G4S1P_a,
#     "Freya-800G-4S-1P[b]": modules.MFreya800G4S1P_b,
#     "Freya-800G-4S-1P-OSFP[a]": modules.MFreya800G4S1POSFP_a,
# }

# # endregion

# # region Chimera Modules

# CHIMERA_MODULES = {
#     "Chimera-100G-5S-2P": modules.MChi100G5S2P,
#     "Chimera-100G-5S-2P[b]": modules.MChi100G5S2P_b,
#     "Chimera-40G-5S-2P": modules.MChi40G5S2P,
# }

# # endregion

# # region Vulcan Modules

# VULCAN_MODULES = {
#     "Xena L47 Module": modules.ModuleL47,
# }

# # endregion
