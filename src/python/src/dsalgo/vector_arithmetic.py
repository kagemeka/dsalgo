from __future__ import annotations

import abc
import dataclasses
import math
import typing


@dataclasses.dataclass
class Vector:
    coordinate: list[int | float]


# def


@dataclasses.dataclass
class VectorElement(abc.ABC):
    def __iter__(self) -> typing.Iterator[int]:
        return iter(dataclasses.astuple(self))

    def clone(self):
        return self.__class__(*self)

    def __add__(self, other):
        x = self.clone()
        for f in dataclasses.fields(x):
            f = f.name
            i = getattr(x, f)
            j = getattr(other, f)
            setattr(x, f, i + j)
        return x

    def __iadd__(self, other):
        return self + other

    def __neg__(self):
        return self.__class__(
            *(-getattr(self, f.name) for f in dataclasses.fields(self))
        )

    def __sub__(self, other):
        return self + -other

    def __isub__(self, other):
        return self - other

    def __matmul__(self, other):
        p = 0
        for f in dataclasses.fields(self):
            f = f.name
            i = getattr(self, f)
            j = getattr(other, f)
            p += i * j
        return p

    def __mul__(self, r: float):
        x = self.clone()
        for f in dataclasses.fields(x):
            f = f.name
            i = getattr(x, f)
            setattr(x, f, r * i)
        return x

    def __imul__(self, r: float):
        return self * r

    def __rmul__(self, r: float):
        return self * r

    def __truediv__(self, r: float):
        return self * (1 / r)

    def __itruediv__(self, r: float):
        return self / r

    @property
    def norm(self):
        s = sum(x**2 for x in self.asdict().values())
        return math.sqrt(s)

    @classmethod
    def define(cls, n):
        vector = dataclasses.make_dataclass(
            cls_name="vector",
            fields=[(f"x{i}", float, 0) for i in range(n)],
            bases=(cls,),
        )
        return vector

    def asdict(self):
        return dataclasses.asdict(self)


@dataclasses.dataclass
class Vector2D(Vector):
    x: float = 0
    y: float = 0

    def cross(
        self,
        other,
    ) -> float:
        res = self.x * other.y
        res -= self.y * other.x
        return res
