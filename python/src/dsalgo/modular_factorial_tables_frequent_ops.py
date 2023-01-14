import typing


def cumprod(mod: int, a: typing.List[int]) -> typing.List[int]:
    for i in range(len(a) - 1):
        a[i + 1] *= a[i]
        a[i + 1] %= mod
    return a


def make_factorials(
    p: int,
    size: int,
) -> typing.Tuple[typing.List[int], typing.List[int]]:
    fact = list(range(size))
    fact[0] = 1
    fact = cumprod(p, fact)
    ifact = list(range(size, 0, -1))
    ifact[0] = pow(fact[-1], p - 2, p)
    return fact, cumprod(p, ifact)[::-1]


class FactorialTablesFrequentOps:
    mod: int
    fact: typing.List[int]
    ifact: typing.List[int]

    def __init__(self, p: int, size: int) -> None:
        self.mod = p
        self.fact, self.ifact = make_factorials(p, size)

    def p(self, n: int, k: int) -> int:
        if k < 0 or n < k:
            return 0
        return self.fact[n] * self.ifact[n - k] % self.mod

    def c(self, n: int, k: int) -> int:
        return self.p(n, k) * self.ifact[k] % self.mod

    def h(self, n: int, k: int) -> int:
        return self.c(n - 1 + k, k)

    def inv(self, n: int) -> int:
        return self.fact[n - 1] * self.ifact[n] % self.mod

    def inv_p(self, n: int, k: int) -> int:
        assert 0 <= k <= n
        return self.ifact[n] * self.fact[n - k] % self.mod

    def inv_c(self, n: int, k: int) -> int:
        return self.inv_p(n, k) * self.fact[k] % self.mod
