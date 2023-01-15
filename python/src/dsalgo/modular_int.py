from __future__ import annotations

import abc
import typing
import unittest

"""toggle comments for pypy (instead of future_annotations)"""
# # mypy: ignore-errors
# Modint = typing.TypeVar("Modint")
# Intlike = typing.Union[Modint, int]
""""""


class Modint(abc.ABC):
    mod: typing.ClassVar[int]
    value: int

    def __init__(self, value: int) -> None:
        self.value = value % self.mod

    @classmethod
    def new(cls, x: Intlike) -> Modint:
        return (
            typing.cast(Modint, x)
            if type(x) != int
            else cls(typing.cast(int, x))
        )

    def __repr__(self) -> str:
        return f"{self.value}"

    def clone(self) -> Modint:
        return self.new(self.value)

    def __add__(self, rhs: Intlike) -> Modint:
        return self.new(self.value + self.new(rhs).value)

    def __neg__(self) -> Modint:
        return self.new(-self.value)

    def __mul__(self, rhs: Intlike) -> Modint:
        return self.new(self.value * self.new(rhs).value)

    def inv(self) -> Modint:
        return self ** (self.mod - 2)
        # return self**-1  # RE in pypy

    def __sub__(self, rhs: Intlike) -> Modint:
        return self + -self.new(rhs)

    def __truediv__(self, rhs: Intlike) -> Modint:
        return self * self.new(rhs).inv()

    def __iadd__(self, rhs: Intlike) -> Modint:
        return self + self.new(rhs)

    def __isub__(self, rhs: Intlike) -> Modint:
        return self - self.new(rhs)

    def __imul__(self, rhs: Intlike) -> Modint:
        return self * self.new(rhs)

    def __itruediv__(self, rhs: Intlike) -> Modint:
        return self / self.new(rhs)

    def __radd__(self, lhs: int) -> int:
        return (self.new(lhs) + self).value

    def __rsub__(self, lhs: int) -> int:
        return (self.new(lhs) - self).value

    def __rmul__(self, lhs: int) -> int:
        return (self.new(lhs) * self).value

    def __rtruediv__(self, lhs: int) -> int:
        return (self.new(lhs) / self).value

    def __pow__(self, n: int) -> Modint:
        return self.new(pow(self.value, n, self.mod))

    def __ipow__(self, n: int) -> Modint:
        return self**n

    def __eq__(self, rhs: object) -> bool:
        if not isinstance(rhs, Modint):
            raise NotImplementedError
        return self.value == rhs.value


Intlike = Modint | int


def define_modint(p: int) -> typing.Type[Modint]:
    class Mint(Modint):
        mod = p

    return Mint


class Tests(unittest.TestCase):
    def test(self) -> None:
        Mint = define_modint(1_000_000_007)
        a = Mint(-1)
        print(a)
        print(2 * a)
        print(a * 2)
        b = a
        a.value = 1
        a /= 2
        print(b)


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
