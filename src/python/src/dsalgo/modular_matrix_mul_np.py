# mypy: ignore-errors

import typing
import unittest

import numpy as np
import numpy.typing as npt


# np.dot cause overflow.
def mul(mod: int, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return (a[:, None, :] * b.T[None, ...] % mod).sum(axis=-1) % mod


class Test(unittest.TestCase):
    def test(self) -> None:
        MOD = 1_000_000_007
        a = np.array([[-1, 0], [0, -1]])
        b = np.array([[0, 1, 1], [1, 0, 1]])
        print(a)
        print(b)
        print(mul(MOD, a, b))
        ans = np.array([[0, -1, -1], [-1, 0, -1]])
        ans %= MOD
        assert np.all(mul(MOD, a, b) == ans)


if __name__ == "__main__":
    import unittest

    unittest.main()
