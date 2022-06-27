import typing
from dsalgo.kmp_table_0_indexed import kmp_table

T = typing.TypeVar("T")

A = typing.Sequence[T]


def kmp_findall(a: A, pattern: A) -> typing.List[int]:
    # 0-indexed
    p = pattern
    n, m = len(a), len(p)
    f = kmp_table(p)
    j = 0
    indices = []
    for i in range(n):
        while j != 0 and p[j] != a[i]:
            j = f[j - 1]
        if p[j] == a[i]:
            j += 1
        if j == m:
            indices.append(i - m + 1)
            j = f[-1]
    return indices


def test_kmp_findall() -> None:
    s = "abacababc"
    print(kmp_findall(s, "ab"))
