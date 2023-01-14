# Algebraic Structure
from __future__ import annotations

import dataclasses
import typing

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
    add: typing.Callable[[T, T], T]
    zero: typing.Callable[[], T]
    mul: typing.Callable[[T, T], T]
    one: typing.Callable[[], T]


@dataclasses.dataclass
class Ring(Semiring[T]):
    add_inv: typing.Callable[[T], T]
