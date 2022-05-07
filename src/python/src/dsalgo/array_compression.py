from __future__ import annotations

import dataclasses


class ArrayCompression:
    """

    Examples:
    >>> a = [3, 10, 2, 5]
    >>> compress = ArrayCompression(a)
    >>> compressed = [compress(x) for x in a]
    >>> compressed
    [1, 3, 0, 2]
    >>> equal_to_original = [compress.retrieve(x) for x in compressed]
    >>> equal_to_original
    [3, 10, 2, 5]
    """

    __values: list[int]

    def __init__(self, array: list[int]) -> None:
        self.__values = sorted(set(array))

    def __call__(self, value: int) -> int:
        import bisect

        i = bisect.bisect_left(self.__values, value)
        if i >= len(self.__values) or self.__values[i] != value:
            raise KeyError
        return i

    def retrieve(self, key: int) -> int:
        return self.__values[key]


@dataclasses.dataclass
class CompressionResult:
    compressed_array: list[int]
    values: list[int]


def compress(array: list[int]) -> CompressionResult:
    import bisect

    values = sorted(set(array))
    return CompressionResult(
        [bisect.bisect_left(values, value) for value in array],
        values,
    )
