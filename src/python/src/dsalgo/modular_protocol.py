import typing


class Modulus(typing.Protocol):
    @classmethod
    def value(cls) -> int:
        ...


class DynamicModulus(Modulus):
    __value: typing.ClassVar[int]
    __is_set: typing.ClassVar[int] = False

    @classmethod
    def set(cls, value: int) -> None:
        assert 2 <= value < 1 << 31 and not cls.__is_set
        cls.__value = value
        cls.__is_set = True

    @classmethod
    def value(cls) -> int:
        assert cls.__is_set
        return cls.__value


_M = typing.TypeVar("_M", bound=Modulus)


class Modular(typing.Generic[_M]):
    __value: int

    def __init__(self, value: int) -> None:
        ...


class Mod998_244_353(Modulus):
    @classmethod
    def value(cls) -> int:
        return 998_244_353


class RuntimeMod(DynamicModulus):
    ...
