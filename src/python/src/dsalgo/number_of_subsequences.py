from __future__ import annotations

import collections
import typing

from dsalgo.type import T


def number_of_subsequences(
    arr: typing.Sequence[T],
    mod: int | None = None,
) -> int:
    n = len(arr)
    dp = [0] * (n + 1)
    dp[0] = 1
    prev_index: typing.DefaultDict[T, int] = collections.defaultdict(int)
    for i in range(n):
        j, prev_index[arr[i]] = prev_index[arr[i]], i + 1
        dp[i + 1] = dp[i] * 2
        if j != 0:
            dp[i + 1] -= dp[j - 1]
        if mod:
            dp[i + 1] %= mod
    return dp[-1]
