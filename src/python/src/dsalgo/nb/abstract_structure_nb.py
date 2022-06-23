import numba

from dsalgo.type import S


@numba.njit
def operation(a: S, b: S) -> S:
    ...


@numba.njit
def identity() -> S:
    ...
