from functools import partial
from xoa_driver.internals.utils.rev_tool import RegisterModule

VALKYRIE_MODULES = {}
CHIMERA_MODULES = {}
VULCAN_MODULES = {}


register_valkyrie_module = partial(RegisterModule, modules_store=VALKYRIE_MODULES)
register_chimera_module = partial(RegisterModule, modules_store=CHIMERA_MODULES)
register_vulcan_module = partial(RegisterModule, modules_store=VULCAN_MODULES)
