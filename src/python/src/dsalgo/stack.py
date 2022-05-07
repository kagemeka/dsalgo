import typing

T = typing.TypeVar("T")


class Stack(typing.Generic[T]):
    def __init__(self) -> None:
        self.__data: list[T] = []

    def __len__(self) -> int:
        return len(self.__data)

    def push(self, x: T) -> None:
        self.__data.append(x)

    def pop(self) -> T:
        assert len(self) > 0
        return self.__data.pop()

    def top(self) -> T:
        assert len(self) > 0
        return self.__data[-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
