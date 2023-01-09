

class FieldDeclarationError(TypeError):
    def __init__(self, f_name: str) -> None:
        self.msg = f"Structure Field {f_name!r} must be described with <field method>"
        super().__init__(self.msg)
