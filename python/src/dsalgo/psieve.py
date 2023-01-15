import typing
import unittest

from dsalgo.isqrt import isqrt


def enumerate_primes(sz: int) -> typing.Generator[int, None, None]:
    if sz <= 2:
        return
    yield 2
    is_p = [True] * (sz >> 1)
    for i in range(3, sz, 2):
        if not is_p[i >> 1]:
            continue
        yield i
        for j in range(i * i >> 1, sz >> 1, i):
            is_p[j] = False


def erat_rs(lt: int) -> typing.Callable[[int, int], typing.List[int]]:
    # eratosthenes range sieve
    ps = list(enumerate_primes(isqrt(lt) + 1))

    def query(l: int, h: int) -> typing.List[int]:
        assert l <= h <= lt
        a: typing.List[int] = []
        if h <= 2:
            return a
        if l < 2:
            l = 2
        if l & 1 == 0:
            if l == 2:
                a.append(2)
            l += 1
        if l == h:
            return a
        sz = (h - l + 1) >> 1
        is_p = [True] * sz
        for i in ps[1:]:
            mn = i * i
            if mn >= h:
                break
            mn = max(mn, (l + i - 1) // i * i)
            if mn & 1 == 0:
                mn += i
            for j in range((mn - l) >> 1, sz, i):
                is_p[j] = False
        for i in range(sz):
            if is_p[i]:
                a.append(l + (i << 1))
        return a

    return query


class Tests(unittest.TestCase):
    def test_erat(self) -> None:
        assert list(enumerate_primes(2)) == []
        assert list(enumerate_primes(100)) == [
            2,
            3,
            5,
            7,
            11,
            13,
            17,
            19,
            23,
            29,
            31,
            37,
            41,
            43,
            47,
            53,
            59,
            61,
            67,
            71,
            73,
            79,
            83,
            89,
            97,
        ]

    def test_erat_rs(self) -> None:
        query = erat_rs(1 << 40)
        assert len(query(999999990000, 1000000000000)) == 337


if __name__ == "__main__":
    import doctest

    # unittest.main()
    # doctest.testmod(verbose=True)
    for x in enumerate_primes(100000000):
        # print(x)
        ...
