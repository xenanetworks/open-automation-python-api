from xoa_driver import modules

# region Vlkyrie Modules

valkyrie_modules = {
    # family_d
    "Odin-1G-3S-6P-E": modules.MOdin1G3S6PE,
    "Odin-1G-3S-6P": modules.MOdin1G3S6P,
    "Odin-1G-3S-6P[b]": modules.MOdin1G3S6P_b,
    "Odin-1G-3S-2P-T": modules.MOdin1G3S2PT,
    
    # family_e
    "Odin-5G-4S-6P-CU": modules.MOdin5G4S6PCU,
    "Odin-10G-5S-6P-CU": modules.MOdin10G5S6PCU,
    "Odin-10G-5S-6P-CU[b]": modules.MOdin10G5S6PCU_b,
    "Odin-10G-3S-6P-CU": modules.MOdin10G3S6PCU,
    "Odin-10G-3S-2P-CU": modules.MOdin10G3S2PCU,
    
    # family_f
    "Odin-10G-1S-2P": modules.MOdin10G1S2P,
    "Odin-10G-1S-2P[b]": modules.MOdin10G1S2P_b,
    "Odin-10G-1S-2P[c]": modules.MOdin10G1S2P_c,
    "Odin-10G-1S-6P": modules.MOdin10G1S6P,
    "Odin-10G-1S-6P[b]": modules.MOdin10G1S6P_b,
    "Odin-10G-1S-2P-T": modules.MOdin10G1S2PT,
    "Odin-10G-1S-2P[d]": modules.MOdin10G1S2P_d,
    "Odin-10G-1S-12P": modules.MOdin10G1S12P,
    
    # family_g
    "Loki-100G-3S-1P": modules.MLoki100G3S1P,
    "Loki-100G-3S-1P[b]": modules.MLoki100G3S1P_b,
    "Loki-100G-3S-1P-SE": modules.MLoki100G3S1PSE,
    
    # family_h
    "Loki-100G-5S-1P": modules.MLoki100G5S1P,
    
    # family_i
    "Loki-100G-5S-2P": modules.MLoki100G5S2P,
    
    # family_j
    "Thor-100G-5S-4P": modules.MThor100G5S4P,
    
    # family_k
    "Thor-400G-7S-1P": modules.MThor400G7S1P,
    
    # family_l
    "Thor-400G-7S-1P[b]": modules.MThor400G7S1P_b,
    "Thor-400G-7S-1P[c]": modules.MThor400G7S1P_c,
    
    # family_m
    "Odin-1G-3S-6P-T1-RJ45": modules.MOdin1G3S6PT1RJ45,
    
    # family_n
    "Odin-40G-2S-2P": modules.MOdin40G2S2P,
}

# endregion

chimera_modules = {
    "Chimera-100G-5S-2P": modules.ModuleChimera,
}

vulcan_modules = {
    "Xena L47 Module": modules.ModuleL47,
}
