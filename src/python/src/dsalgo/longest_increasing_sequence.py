from __future__ import annotations

import bisect

from dsalgo.constant import INT_INF


def longest_increasing_sequence(arr: list[int]) -> list[int]:
    """Longest Increasing Sequence.

    Args:
        arr (list[int]): integer array.

    Returns:
        list[int]: result.
    """
    lis = [INT_INF] * len(arr)
    for x in arr:
        lis[bisect.bisect_left(lis, x)] = x
    return lis[: bisect.bisect_left(lis, INT_INF)]


def longest_non_decreasing_sequence(arr: list[int]) -> list[int]:
    """Longest Non Decreasing Sequence.

    Args:
        arr (list[int]): integer array.

    Returns:
        list[int]: result.
    """
    lis = [INT_INF] * len(arr)
    for x in arr:
        lis[bisect.bisect_right(lis, x)] = x
    return lis[: bisect.bisect_left(lis, INT_INF)]
