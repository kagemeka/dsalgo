import typing

from dsalgo.type import T


def count_common_subsequences(
    a: typing.Sequence[T],
    b: typing.Sequence[T],
    mod: typing.Optional[int],
) -> int:
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        dp[i + 1][0] = 1
    for j in range(m):
        dp[0][j + 1] = 1
    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1]
            if a[i] != b[j]:
                dp[i + 1][j + 1] -= dp[i][j]
            if mod:
                dp[i + 1][j + 1] %= mod
    return dp[-1][-1]
