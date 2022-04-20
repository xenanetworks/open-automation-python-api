#: All avaliable test port types.


import typing

from .internals.ports.port_l47.main import PortL47

from .internals.ports.port_l23.port_l23ve import PortL23VE
from .internals.ports.port_l23.chimera.port_chimera import PortChimera
from .internals.ports.port_l23.bases.port_l23 import BasePortL23
from xoa_driver.internals.ports.port_l23.family_d.base import (
    POdin1G3S6P,
    POdin1G3S6P_b,
    POdin1G3S6PE,
    POdin1G3S2PT,
)

from xoa_driver.internals.ports.port_l23.family_e.base import (
    POdin5G4S6PCU,
    POdin10G5S6PCU,
    POdin10G5S6PCU_b,
    POdin10G3S6PCU,
    POdin10G3S2PCU,
)

from xoa_driver.internals.ports.port_l23.family_f.base import (
    POdin10G1S2P,
    POdin10G1S2P_b,
    POdin10G1S2P_c,
    POdin10G1S6P,
    POdin10G1S6P_b,
    POdin10G1S2PT,
    POdin10G1S2P_d,
    POdin10G1S12P,
    POdin40G2S2P,
)

from xoa_driver.internals.ports.port_l23.family_g.base import (
    PLoki100G3S1P,
    PLoki100G3S1P_b,
    PLoki100G3S1PSE,
)

from xoa_driver.internals.ports.port_l23.family_h.base import PLoki100G5S1P
from xoa_driver.internals.ports.port_l23.family_i.base import PLoki100G5S2P
from xoa_driver.internals.ports.port_l23.family_j.base import PThor100G5S4P
from xoa_driver.internals.ports.port_l23.family_k.base import PThor400G7S1P
from xoa_driver.internals.ports.port_l23.family_l.base import (
    PThor400G7S1P_b,
    PThor400G7S1P_c,
)

from xoa_driver.internals.ports.port_l23.family_m.base import POdin1G3S6PT1RJ45



GenericL23Port = typing.Union[
        "POdin1G3S6P",
        "POdin1G3S6P_b",
        "POdin1G3S6PE",
        "POdin1G3S2PT",
        "POdin5G4S6PCU",
        "POdin10G5S6PCU",
        "POdin10G5S6PCU_b",
        "POdin10G3S6PCU",
        "POdin10G3S2PCU",
        "POdin10G1S2P",
        "POdin10G1S2P_b",
        "POdin10G1S2P_c",
        "POdin10G1S6P",
        "POdin10G1S6P_b",
        "POdin10G1S2PT",
        "POdin10G1S2P_d",
        "POdin10G1S12P",
        "POdin40G2S2P",
        "PLoki100G3S1P",
        "PLoki100G3S1P_b",
        "PLoki100G3S1PSE",
        "PLoki100G5S1P",
        "PLoki100G5S2P",
        "PThor100G5S4P",
        "PThor400G7S1P",
        "PThor400G7S1P_b",
        "PThor400G7S1P_c",
        "POdin1G3S6PT1RJ45",
    ]

GenericAnyPort = typing.Union[
    GenericL23Port,
    "PortL47",
    "PortL23VE",
    "PortChimera"
]

__all__ = (
    "BasePortL23",
    "POdin1G3S6P",
    "POdin1G3S6P_b",
    "POdin1G3S6PE",
    "POdin1G3S2PT",
    "POdin5G4S6PCU",
    "POdin10G5S6PCU",
    "POdin10G5S6PCU_b",
    "POdin10G3S6PCU",
    "POdin10G3S2PCU",
    "POdin10G1S2P",
    "POdin10G1S2P_b",
    "POdin10G1S2P_c",
    "POdin10G1S6P",
    "POdin10G1S6P_b",
    "POdin10G1S2PT",
    "POdin10G1S2P_d",
    "POdin10G1S12P",
    "POdin40G2S2P",
    "PLoki100G3S1P",
    "PLoki100G3S1P_b",
    "PLoki100G3S1PSE",
    "PLoki100G5S1P",
    "PLoki100G5S2P",
    "PThor100G5S4P",
    "PThor400G7S1P",
    "PThor400G7S1P_b",
    "PThor400G7S1P_c",
    "POdin1G3S6PT1RJ45",
    "PortL47",
    "PortL23VE",
    "PortChimera",
    "GenericL23Port",
    "GenericAnyPort",
)