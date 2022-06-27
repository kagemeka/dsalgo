import typing


T = typing.TypeVar("T")


def kmp_table(a: typing.Sequence[T]) -> typing.List[int]:
    # 0-indexed
    n = len(a)
    f = [0] * n  # failure function (would be accessed at mismatch)
    d = 0
    for i in range(1, n):
        while d != 0 and a[d] != a[i]:
            d = f[d - 1]
        if a[d] == a[i]:
            d += 1
        f[i] = f[d - 1] if d != 0 and i + 1 < n and a[d] == a[i + 1] else d
    return f
