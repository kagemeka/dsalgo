import typing


T = typing.TypeVar("T")


def kmp_table(a: typing.Sequence[T]) -> typing.List[int]:
    # 1-indexed
    n = len(a)
    f = [0] * (n + 1)
    f[0] = d = -1
    for i in range(n):
        while d != -1 and a[d] != a[i]:
            d = f[d]
        d += 1
        f[i + 1] = f[d] if i + 1 < n and a[d] == a[i + 1] else d
    return f
