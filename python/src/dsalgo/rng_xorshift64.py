import typing
import unittest


def xorshift64(seed: int) -> int:
    MASK = (1 << 64) - 1
    x = seed
    x ^= x << 13
    x &= MASK
    x ^= x >> 7
    x ^= x << 17
    return x & MASK


def rng_xorshift64(seed: int = 88172645463325252) -> typing.Callable[[], int]:
    x = seed

    def rng() -> int:
        nonlocal x
        x = xorshift64(x)
        return x

    return rng


class Tests(unittest.TestCase):
    def test(self) -> None:
        rng = rng_xorshift64()
        ANS = [
            8748534153485358512,
            3040900993826735515,
            3453997556048239312,
        ]
        for i in range(3):
            assert rng() == ANS[i]


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
