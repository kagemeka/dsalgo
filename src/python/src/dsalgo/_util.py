from __future__ import annotations

import typing

from dsalgo.type import T

Exportable = typing.Union[typing.Callable, typing.Type]


def export_module(obj: Exportable) -> Exportable:
    import sys

    module = sys.modules[obj.__module__]
    if hasattr(module, "__all__"):
        name = obj.__name__
        all_ = module.__all__
        if name not in all_:
            all_.append(name)
    else:
        module.__all__ = [obj.__name__]
    return obj


def unwrap(item: T | None) -> T:
    assert item is not None
    return item
