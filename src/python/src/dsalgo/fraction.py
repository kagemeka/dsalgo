from __future__ import annotations

import math

# import typing


# def lcm(a: int, b: int) -> int:
#     return a // math.gcd(a, b) * b


# Fraction = typing.TypeVar("Fraction")


class Fraction:
    upper: int
    lower: int

    def __init__(self, upper: int, lower: int) -> None:
        self.upper = upper
        self.lower = lower

    def normalize(self) -> None:
        g = math.gcd(self.upper, self.lower)
        self.upper //= g
        self.lower //= g
        if self.lower < 0:
            self.lower *= -1
            self.upper *= -1

    def __add__(self, rhs: Fraction) -> Fraction:
        l = math.lcm(self.lower, rhs.lower)
        # l = lcm(self.lower, rhs.lower)
        a, b = l // self.lower, l // rhs.lower
        return Fraction(self.upper * a + rhs.upper * b, l)

    def __neg__(self) -> Fraction:
        return Fraction(-self.upper, self.lower)

    def __sub__(self, rhs: Fraction) -> Fraction:
        return self + -rhs

    def __mul__(self, rhs: Fraction) -> Fraction:
        return Fraction(self.upper * rhs.upper, self.lower * rhs.lower)

    def __pow__(self, n: int) -> Fraction:
        if n == 0:
            return Fraction(1, 1)
        x = self ** (n >> 1)
        x = x * x
        if n & 1:
            x *= self
        return x

    def __repr__(self) -> str:
        return f"{self.upper}/{self.lower}"

    def floor(self) -> int:
        self.normalize()
        return self.upper // self.lower

    def ceil(self) -> int:
        floor = self.floor()
        if floor * self.lower == self.upper:
            return floor
        else:
            return floor + 1

    def __le__(self, rhs: Fraction) -> bool:
        res = self - rhs
        res.normalize()
        return res.upper <= 0

    def __eq__(self, rhs: Fraction) -> bool:
        return (self - rhs).upper == 0


def to_fraction(number: str) -> Fraction:
    parts = number.split(".")
    if len(parts) == 1:
        return Fraction(int(parts[0]), 1)
    assert len(parts) == 2
    p = 10 ** len(parts[1])
    return Fraction(int(parts[0]) * p + int(parts[1]), p)
