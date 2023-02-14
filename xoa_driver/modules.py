#: All available test module types.
import sys

if "xoa_driver.v2" in sys.modules:
    raise ImportError("\33[31mOnly Single interface version is allowed to being use at the same time.\33[0m")

from .internals.hli_v1.modules.modules_l23.module_l23_base import ModuleL23
from .internals.hli_v1.modules.modules_l23.family_d import (
    MOdin1G3S2PT,
    MOdin1G3S6P,
    MOdin1G3S6P_b,
    MOdin1G3S6PE,
)
from .internals.hli_v1.modules.modules_l23.family_e import (
    MOdin5G4S6PCU,
    MOdin10G3S2PCU,
    MOdin10G3S6PCU,
    MOdin10G5S6PCU,
    MOdin10G5S6PCU_b,
)
from .internals.hli_v1.modules.modules_l23.family_f import (
    MOdin10G1S2P,
    MOdin10G1S2P_b,
    MOdin10G1S2P_c,
    MOdin10G1S2P_d,
    MOdin10G1S2PT,
    MOdin10G1S6P,
    MOdin10G1S6P_b,
    MOdin10G1S12P,
)
from .internals.hli_v1.modules.modules_l23.family_g import (
    MLoki100G3S1P,
    MLoki100G3S1P_b,
    MLoki100G3S1PSE,
)
from .internals.hli_v1.modules.modules_l23.family_h import (
    MLoki100G5S1P,
    MOdin100G3S1P,
)
from .internals.hli_v1.modules.modules_l23.family_i import MLoki100G5S2P
from .internals.hli_v1.modules.modules_l23.family_j import MThor100G5S4P
from .internals.hli_v1.modules.modules_l23.family_k import MThor400G7S1P
from .internals.hli_v1.modules.modules_l23.family_l import (
    MThor400G7S1P_b,
    MThor400G7S1P_c,
    MThor400G7S1P_d,
)
from .internals.hli_v1.modules.modules_l23.family_l1 import (
    MFreya800G1S1P_a,
    MFreya800G1S1P_b,
    MFreya800G1S1POSFP_a,
    MFreya800G4S1P_a,
    MFreya800G4S1POSFP_a,
    MFreya800G4S1P_b,
)
from .internals.hli_v1.modules.modules_l23.family_m import MOdin1G3S6PT1RJ45
from .internals.hli_v1.modules.modules_l23.family_n import (
    MOdin40G2S2P,
    MOdin40G2S2PB,
)
from .internals.hli_v1.modules.modules_l23.family_combi import (
    MOdin10G4S2PCombi,
    MOdin10G4S2PCombi_b,
)
from .internals.hli_v1.modules.module_l23ve import ModuleL23VE
from .internals.hli_v1.modules.module_chimera import (
    ModuleChimera,
    MChi100G5S2P,
    MChi100G5S2P_b,
    MChi40G5S2P,
)
from .internals.hli_v1.modules.module_l47 import ModuleL47
from .internals.hli_v1.modules.module_l47ve import ModuleL47VE

import typing

GenericL23Module = typing.Union[
    "MOdin1G3S6P",
    "MOdin1G3S6P_b",
    "MOdin1G3S6PE",
    "MOdin1G3S2PT",
    "MOdin5G4S6PCU",
    "MOdin10G5S6PCU",
    "MOdin10G5S6PCU_b",
    "MOdin10G3S6PCU",
    "MOdin10G3S2PCU",
    "MOdin10G1S2P",
    "MOdin10G1S2P_b",
    "MOdin10G1S2P_c",
    "MOdin10G1S2P_d",
    "MOdin10G1S6P",
    "MOdin10G1S6P_b",
    "MOdin10G1S2PT",
    "MOdin10G1S2P_d",
    "MOdin10G1S12P",
    "MOdin40G2S2P",
    "MOdin40G2S2PB",
    "MOdin100G3S1P",
    "MLoki100G3S1P",
    "MLoki100G3S1P_b",
    "MLoki100G3S1PSE",
    "MLoki100G5S1P",
    "MLoki100G5S2P",
    "MThor100G5S4P",
    "MThor400G7S1P",
    "MThor400G7S1P_b",
    "MThor400G7S1P_c",
    "MThor400G7S1P_d",
    "MFreya800G1S1P_a",
    "MFreya800G1S1P_b",
    "MFreya800G1S1POSFP_a",
    "MFreya800G4S1P_a",
    "MFreya800G4S1P_b",
    "MFreya800G4S1POSFP_a",
    "MOdin1G3S6PT1RJ45",
    "MOdin10G4S2PCombi",
    "MOdin10G4S2PCombi_b",
]

GenericAnyModule = typing.Union[
    GenericL23Module,
    "ModuleL23VE",
    "ModuleChimera",
    "MChi100G5S2P",
    "MChi100G5S2P_b",
    "MChi40G5S2P",
    "ModuleL47",
    "ModuleL47VE",
]

__all__ = (
    "ModuleL23",
    "MOdin1G3S6P",
    "MOdin1G3S6P_b",
    "MOdin1G3S6PE",
    "MOdin1G3S2PT",
    "MOdin5G4S6PCU",
    "MOdin10G5S6PCU",
    "MOdin10G5S6PCU_b",
    "MOdin10G3S6PCU",
    "MOdin10G3S2PCU",
    "MOdin10G1S2P",
    "MOdin10G1S2P_b",
    "MOdin10G1S2P_c",
    "MOdin10G1S2P_d",
    "MOdin10G1S6P",
    "MOdin10G1S6P_b",
    "MOdin10G1S2PT",
    "MOdin10G1S2P_d",
    "MOdin10G1S12P",
    "MOdin40G2S2P",
    "MOdin40G2S2PB",
    "MOdin100G3S1P",
    "MLoki100G3S1P",
    "MLoki100G3S1P_b",
    "MLoki100G3S1PSE",
    "MLoki100G5S1P",
    "MLoki100G5S2P",
    "MThor100G5S4P",
    "MThor400G7S1P",
    "MThor400G7S1P_b",
    "MThor400G7S1P_c",
    "MThor400G7S1P_d",
    "MFreya800G1S1P_a",
    "MFreya800G1S1P_b",
    "MFreya800G1S1POSFP_a",
    "MFreya800G4S1P_a",
    "MFreya800G4S1P_b",
    "MFreya800G4S1POSFP_a",
    "MOdin1G3S6PT1RJ45",
    "MOdin10G4S2PCombi",
    "MOdin10G4S2PCombi_b",
    "ModuleL23VE",
    "ModuleChimera",
    "MChi100G5S2P",
    "MChi100G5S2P_b",
    "MChi40G5S2P",
    "ModuleL47",
    "ModuleL47VE",
    "GenericL23Module",
    "GenericAnyModule",
)
