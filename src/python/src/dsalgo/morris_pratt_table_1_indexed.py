import typing

T = typing.TypeVar("T")


def morris_pratt_table(a: typing.Sequence[T]) -> typing.List[int]:
    # 1-indexed
    n = len(a)
    lb = [0] * (n + 1)
    lb[0] = d = -1
    for i in range(n):
        while d != -1 and a[d] != a[i]:
            d = lb[d]
        d += 1
        lb[i + 1] = d
    return lb
