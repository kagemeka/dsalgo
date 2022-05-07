from __future__ import annotations

import dataclasses
import typing

from dsalgo.type import T


@dataclasses.dataclass
class Semigroup(typing.Generic[T]):
    operation: typing.Callable[[T, T], T]


@dataclasses.dataclass
class Monoid(Semigroup[T]):
    identity: typing.Callable[[], T]


@dataclasses.dataclass
class Group(Monoid[T]):
    invert: typing.Callable[[T], T]


@dataclasses.dataclass
class Semiring(typing.Generic[T]):
    ...


@dataclasses.dataclass
class Ring(Semiring[T]):
    ...
