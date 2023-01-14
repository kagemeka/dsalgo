import unittest


def sa_is(a: list[int]) -> list[int]:
    mn = min(a)
    a = [x - mn + 1 for x in a]
    a.append(0)
    n = len(a)
    m = max(a) + 1
    is_s = [True] * n
    for i in range(n - 2, -1, -1):
        is_s[i] = is_s[i + 1] if a[i] == a[i + 1] else a[i] < a[i + 1]
    is_lms = [not is_s[i - 1] and is_s[i] for i in range(n)]
    lms = [i for i in range(n) if is_lms[i]]
    bucket = [0] * m
    for x in a:
        bucket[x] += 1

    def induce(lms: list[int]) -> list[int]:
        nonlocal n, a, m, bucket, is_s
        sa = [-1] * n
        sa_idx = bucket.copy()
        for i in range(m - 1):
            sa_idx[i + 1] += sa_idx[i]
        for i in lms[::-1]:
            sa_idx[a[i]] -= 1
            sa[sa_idx[a[i]]] = i

        sa_idx = bucket.copy()
        s = 0
        for i in range(m):
            s, sa_idx[i] = s + sa_idx[i], s
        for i in range(n):
            i = sa[i] - 1
            if i < 0 or is_s[i]:
                continue
            sa[sa_idx[a[i]]] = i
            sa_idx[a[i]] += 1

        sa_idx = bucket.copy()
        for i in range(m - 1):
            sa_idx[i + 1] += sa_idx[i]
        for i in range(n - 1, -1, -1):
            i = sa[i] - 1
            if i < 0 or not is_s[i]:
                continue
            sa_idx[a[i]] -= 1
            sa[sa_idx[a[i]]] = i
        return sa

    lms_idx = [i for i in induce(lms) if is_lms[i]]
    ranks = [-1] * n
    ranks[-1] = rank = 0
    for i in range(len(lms_idx) - 1):
        j, k = lms_idx[i], lms_idx[i + 1]
        for d in range(n):
            if a[j + d] != a[k + d]:
                rank += 1
                break
            if d > 0 and is_lms[j + d]:
                rank += not is_lms[k + d]
                break
        ranks[k] = rank
    ranks = [i for i in ranks if i >= 0]
    if rank == len(lms_idx) - 1:
        lms_order = [-1] * len(lms_idx)
        for i, r in enumerate(ranks):
            lms_order[r] = i
    else:
        lms_order = sa_is(ranks)
    return induce([lms[i] for i in lms_order])[1:]


class Tests(unittest.TestCase):
    def test(self) -> None:
        s = [1, 1, 0, 0, 3, 3, 0, 0, 3, 3, 0, 0, 2, 2, 0, 0]
        ans = [15, 14, 10, 6, 2, 11, 7, 3, 1, 0, 13, 12, 9, 5, 8, 4]
        assert sa_is(s) == ans


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
