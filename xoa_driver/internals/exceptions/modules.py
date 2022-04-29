from typing import Set

class WrongModuleError(Exception):
    def __init__(self, module_revision: str, allowed_revisions: Set[str]) -> None:
        self.module_revision = module_revision
        self.allowed_revisions = allowed_revisions
        self.msg = (
            f"Module of revision <{self.module_revision}> can not be assign to the current tester,\n"
            f"Permitted only modules of next revisions {allowed_revisions}"
        )
        super().__init__(self.msg)