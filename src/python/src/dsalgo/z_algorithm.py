import typing

T = typing.TypeVar("T")


def z_algorithm(a: typing.Sequence[T]) -> typing.List[int]:
    n = len(a)
    lcp = [0] * n
    l = 0
    for i in range(1, n):
        r = l + lcp[l]
        d = 0 if r <= i else min(lcp[i - l], r - i)
        while i + d < n and a[i + d] == a[d]:
            d += 1
        lcp[i] = d
        if i + d > r:
            l = i
    lcp[0] = n
    return lcp
