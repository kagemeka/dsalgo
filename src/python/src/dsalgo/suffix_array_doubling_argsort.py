import typing


# destractive for given a, please copy it before calling to keep stable.
def suffix_array(a: typing.List[int]) -> typing.List[int]:
    n = len(a)
    d = 1
    sa = list(range(n))
    while True:
        for i in range(n):
            a[i] <<= 30
            if i + d < n:
                a[i] |= 1 + a[i + d]
        sa.sort(key=lambda i: a[i])
        d <<= 1
        if d >= n:
            return sa
        rank, prev = 0, a[sa[0]]
        for i in sa:
            if a[i] > prev:
                rank += 1
                prev = a[i]
            a[i] = rank
        if rank == n:
            return sa
