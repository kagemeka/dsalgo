from __future__ import annotations

import typing


class Order(typing.Protocol):
    def __le__(self, rhs: Order) -> bool:
        ...

    def __lt__(self, rhs: Order) -> bool:
        ...
