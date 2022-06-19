from __future__ import annotations

import dataclasses
import typing

# from dsalgo.type import T

T = typing.TypeVar("T")


@dataclasses.dataclass
class Magma(typing.Generic[T]):
    op: typing.Callable[[T, T], T]


@dataclasses.dataclass
class Semigroup(Magma[T]):
    ...


@dataclasses.dataclass
class Monoid(Semigroup[T]):
    e: typing.Callable[[], T]


@dataclasses.dataclass
class Group(Monoid[T]):
    inv: typing.Callable[[T], T]


@dataclasses.dataclass
class Semiring(typing.Generic[T]):
    ...


@dataclasses.dataclass
class Ring(Semiring[T]):
    ...