import typing

import numpy as np
import numpy.typing as npt

import unittest


# np.dot cause overflow.
def dot(
    mod: int,
    a: npt.NDArray[np.int64],
    b: npt.NDArray[np.int64],
) -> npt.NDArray[np.int64]:
    assert np.ndim(a) == np.ndim(b) == 2 and a.shape[1] == b.shape[0]
    return typing.cast(
        npt.NDArray[np.int64],
        (a[:, None, :] * b.T[None, ...] % mod).sum(axis=-1) % mod,
    )


class Test(unittest.TestCase):
    def test(self) -> None:
        MOD = 1_000_000_007
        a = np.array([[-1, 0], [0, -1]])
        b = np.array([[0, 1, 1], [1, 0, 1]])
        print(a)
        print(b)
        print(dot(MOD, a, b))
        ans = np.array([[0, -1, -1], [-1, 0, -1]])
        ans %= MOD
        assert np.all(dot(MOD, a, b) == ans)


if __name__ == "__main__":
    import unittest

    unittest.main()
