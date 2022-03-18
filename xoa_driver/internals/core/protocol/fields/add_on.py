from typing import ( 
    get_args,
    Type,
    ClassVar,
    TypeVar,
)

T = TypeVar("T")

def add_on(data_class: Type) -> Type:
    class AddOn(data_class):
        size: ClassVar[int] = sum(
            get_args(field_type)[0].size 
            for field_type in data_class.__annotations__.values()
        )
        is_add_on: ClassVar[bool] = True
        __qualname__ = data_class.__name__

        @classmethod
        def from_bytes(cls: Type[T], data: bytes) -> "T":
            dic = {}
            pointer = 0
            for field_name, field_type in data_class.__annotations__.items():
                typings = get_args(field_type)[0]
                reading_size = typings.size
                read_bytes = data[pointer : pointer + reading_size]
                pointer += reading_size
                dic[field_name] = typings.from_bytes(read_bytes)

            return cls(**dic)

        def __bytes__(self) -> bytes:
            result = b"".join(
                bytes(getattr(self, field_name)) 
                for field_name in data_class.__annotations__.keys()
            )
            return result

    AddOn.__name__ = data_class.__name__
    return AddOn

