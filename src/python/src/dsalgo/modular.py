from __future__ import annotations

import abc
import enum
import typing


def add(mod: int, lhs: int, rhs: int) -> int:
    assert 0 <= lhs < mod and 0 <= rhs < mod
    res = lhs + rhs
    if res >= mod:
        res -= mod
    return res


def neg(mod: int, x: int) -> int:
    assert 0 <= x < mod
    return mod - x


def subtract(mod: int, lhs: int, rhs: int) -> int:
    assert 0 <= lhs < mod and 0 <= rhs < mod
    return add(mod, lhs, neg(mod, rhs))


def multiply(mod: int, lhs: int, rhs: int) -> int:
    assert 0 <= lhs < mod and 0 <= rhs < mod
    return lhs * rhs % mod


def divide(p: int, lhs: int, rhs: int) -> int:
    assert 0 <= lhs < p and 0 <= rhs < p
    return multiply(p, lhs, invert_fermat(p, rhs))


def pow_recurse(mod: int, x: int, n: int) -> int:
    assert n >= 0
    if n == 0:
        return 1
    y = pow_recurse(mod, x, n >> 1)
    y = y * y % mod
    if n & 1:
        y = y * x % mod
    return y


def pow_(mod: int, x: int, n: int) -> int:
    assert n >= 0
    y = 1
    while n:
        if n & 1:
            y = y * x % mod
        x = x * x % mod
        n >>= 1
    return y


def invert_naive(mod: int, n: int) -> int:
    return pow(n, -1, mod)


def invert_euler_theorem(mod: int, n: int) -> int:
    ...


def invert_fermat(p: int, n: int) -> int:
    # TODO: check primality if possible O(\log{N})
    # or if impossible, we do not guarantee the correctness of the result.
    return pow(n, p - 2, p)


def invert_extended_euclidean(mod: int, n: int) -> int | None:
    import dsalgo.euclidean_algorithm

    assert mod > 1
    gcd, x = dsalgo.euclidean_algorithm.extended_euclidean_gcd_modular_inverse(mod, n)
    return x if gcd == 1 else None


def inverse_table_naive(p: int, n: int) -> list[int]:
    ...


def inverse_table(p: int, n: int) -> list[int]:
    fact, inv_fact = factorial(n - 1, p), factorial_inverse(n, p)
    for i in range(n - 1):
        inv_fact[i + 1] = inv_fact[i + 1] * fact[i] % p
    return inv_fact


def cumprod(mod: int, arr: list[int]) -> list[int]:
    arr = arr.copy()
    for i in range(len(arr) - 1):
        arr[i + 1] = arr[i + 1] * arr[i] % mod
    return arr


def factorial(mod: int, n: int) -> list[int]:
    fact = list(range(n))
    fact[0] = 1
    return cumprod(mod, fact)


def factorial_inverse(p: int, n: int) -> list[int]:
    ifact = list(range(1, n + 1))
    ifact[-1] = pow(factorial(p, n)[-1], -1, p)
    return cumprod(p, ifact[::-1])[::-1]


ADD_IDENTITY = 0
MUL_IDENTITY = 1


class Modulo(enum.IntEnum):
    MOD_1_000_7 = enum.auto()
    MOD_998_244_353 = enum.auto()
    MOD_1_000_000_007 = enum.auto()
    MOD_1_000_000_009 = enum.auto()


class Modular:
    __mod: int

    def __init__(self, modulo: int) -> None:
        self.__mod = modulo

    def add(self, lhs: int, rhs: int) -> int:
        return add(self.__mod, lhs, rhs)

    def neg(self, x: int) -> int:
        return neg(self.__mod, x)

    def subtract(self, lhs: int, rhs: int) -> int:
        return subtract(self.__mod, lhs, rhs)

    def multiply(self, lhs: int, rhs: int) -> int:
        return multiply(self.__mod, lhs, rhs)

    def pow(self, x: int, n: int) -> int:
        return pow(x, n, self.__mod)


class PrimeModular(Modular):
    def divide(self, lhs: int, rhs: int) -> int:
        return divide(self.__mod, lhs, rhs)

    def invert(self, n: int) -> int:
        return invert_naive(self.__mod, n)


class ModularElement(abc.ABC):
    _mod: typing.ClassVar[int]
    __value: int

    def __init__(self, value: int) -> None:
        value %= self.mod
        self.__value = value

    @property
    def value(self) -> int:
        return self.__value

    @property
    def mod(self) -> int:
        return self._mod

    def __repr__(self) -> str:
        return f"{self.value}"

    # def __clone(self) -> Modular:
    #     return self.__class__(self._value)

    def __add__(self, rhs: ModularElement) -> ModularElement:
        return self.__class__(self.value + rhs.value)

    def __iadd__(self, rhs: ModularElement) -> ModularElement:
        return self + rhs

    def __radd__(self, lhs: int) -> int:
        return (self.__class__(lhs) + self).value

    def __neg__(self) -> ModularElement:
        return self.__class__(-self.value)

    def __sub__(self, rhs: ModularElement) -> ModularElement:
        return self + -rhs

    def __isub__(self, rhs: ModularElement) -> ModularElement:
        return self - rhs

    def __rsub__(self, lhs: int) -> int:
        return (self.__class__(lhs) - self).value

    def __mul__(self, rhs: ModularElement) -> ModularElement:
        return self.__class__(self.value * rhs.value)

    def __imul__(self, rhs: ModularElement) -> ModularElement:
        return self * rhs

    def __rmul__(self, lhs: int) -> int:
        return (self.__class__(lhs) * self).value

    def invert(self) -> ModularElement:
        return self.__class__(invert_fermat(self.mod, self.value))

    def __truediv__(self, rhs: ModularElement) -> ModularElement:
        assert rhs.value >= 1
        return self * rhs.invert()

    def __itruediv__(self, rhs: ModularElement) -> ModularElement:
        return self / rhs

    def __rtruediv__(self, lhs: int) -> int:
        return (self.__class__(lhs) / self).value

    def __floordiv__(self, rhs: ModularElement) -> ModularElement:
        return self / rhs

    def __ifloordiv__(self, rhs: ModularElement) -> ModularElement:
        return self // rhs

    def __rfloordiv__(self, lhs: int) -> int:
        return lhs / self

    def __pow__(self, n: int) -> ModularElement:
        return self.__class__(pow(self.value, n, self.mod))

    def __ipow__(self, n: int) -> ModularElement:
        return self**n

    def __eq__(self, rhs: object) -> bool:
        if not isinstance(rhs, ModularElement):
            raise NotImplementedError
        return self.value == rhs.value


def define_static_modular_element(
    prime_mod: int,
) -> typing.Type[ModularElement]:
    class Mint(ModularElement):
        _mod: typing.ClassVar[int] = prime_mod

    return Mint


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
