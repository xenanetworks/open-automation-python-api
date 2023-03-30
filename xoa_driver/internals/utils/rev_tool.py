from __future__ import annotations
from typing import Type


class RegisterModule:
    """Register revision and it's module class"""

    def __init__(self, modules_store: dict[str, Type], rev: str) -> None:
        self.modules_store = modules_store
        self.revision = rev

    def __call__(self, module_type: Type):
        if self.revision in self.modules_store:
            raise RuntimeError(f"Module of revision: {self.revision}, is already registered.")
        self.modules_store[self.revision] = module_type
        return module_type


# register_valkyrie_module = partial(RegisterModule, modules_store=VALKYRIE_MODULES)
# register_chimera_module = partial(RegisterModule, modules_store=CHIMERA_MODULES)
# register_vulcan_module = partial(RegisterModule, modules_store=VULCAN_MODULES)

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
#     "Loki-100G-3S-1P-B": modules.MLoki100G3S1PB,

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
#     "Chimera-40G-2S-2P": modules.MChi40G2S2P,
# }

# # endregion

# # region Vulcan Modules

# VULCAN_MODULES = {
#     "Xena L47 Module": modules.ModuleL47,
# }

# # endregion
