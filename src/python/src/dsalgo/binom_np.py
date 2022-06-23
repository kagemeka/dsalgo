import typing


def make_choose(p: int, n: int) -> typing.Callable[[int, int], int]:
    ...


class ModChooseNP:
    def __init__(self, mod: int, n: int) -> None:
        self.__mod = mod
        self.__fact = factorial_np(mod, n)
        self.__ifact = factorial_inverse_np(mod, n)

    def __call__(self, n: int, k: int) -> int:
        mod, fact, ifact = self.__mod, self.__fact, self.__ifact
        ok = (0 <= k) & (k <= n)
        return fact[n] * ifact[n - k] % mod * ifact[k] % mod * ok

    def inv(self, n: int, k: int) -> int:
        mod, fact, ifact = self.__mod, self.__fact, self.__ifact
        ok = (0 <= k) & (k <= n)
        return ifact[n] * fact[n - k] % mod * fact[k] % mod * ok


class NChooseNP:
    def __call__(
        self,
        r: int,
    ) -> int:
        return self[r]

    def __getitem__(
        self,
        r: int,
    ) -> int:
        return self.__a[r]

    def __init__(
        self,
        n: int,
        rmax: int,
        modulo: int,
    ) -> None:
        r, m = rmax, modulo
        fn = ModFactorial(m)
        a = np.arange(
            n + 1,
            n - r,
            -1,
        )
        a[0] = 1
        a = fn.cumprod(a)
        a *= fn.inv(r + 1)
        self.__a = a % m

    def __len__(self) -> int:
        return self.__a.size
