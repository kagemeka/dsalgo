import typing

import numba as nb
import numpy as np

from dsalgo.numba.graph_theory.tree.segment_tree import S


# set point update, get range minimum
@nb.njit
def seg_op(a: S, b: S) -> S:
    return min(a, b)


@nb.njit
def seg_e() -> S:
    return 1 << 60


# set point update, get range xor
@nb.njit
def seg_op(a: S, b: S) -> S:
    return a ^ b


@nb.njit
def seg_e() -> S:
    return 0
