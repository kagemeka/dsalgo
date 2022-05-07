import dataclasses
import typing

from dsalgo.type import T


@dataclasses.dataclass
class Vector(typing.Generic[T]):
    data: list[T]
