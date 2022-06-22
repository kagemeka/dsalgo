import typing
import unittest


def newton_method(
    f: typing.Callable[[float], float],
    f_prime: typing.Callable[[float], float],
    x0: float,
    abs_tol: float = 0.0,
    rel_tol: float = 0.0,
    max_iter: int = 1 << 6,
) -> float:
    x = x0

    for _ in range(max_iter):
        diff = f(x) / f_prime(x)
        x -= diff
        if abs(diff) < abs_tol and abs(diff / x) < rel_tol:
            return x
    return x


class Tests(unittest.TestCase):
    def test(self) -> None:
        def f(x: float) -> float:
            return x**2 - 10

        def f_prime(x: float) -> float:
            return 2 * x

        self.assertAlmostEqual(
            newton_method(f, f_prime, 1.0),
            3.1622776601683795,
        )


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
