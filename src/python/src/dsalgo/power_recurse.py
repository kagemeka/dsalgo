import typing
import unittest

from dsalgo.algebraic_structure import Group, Monoid, Semigroup

T = typing.TypeVar("T")


def power_recurse(g: Semigroup[T]) -> typing.Callable[[T, int], T]:
    def f(x: T, n: int) -> T:
        if n == 0:
            return typing.cast(Monoid[T], g).e()
        if n < 0:
            return f(typing.cast(Group[T], g).inv(x), -n)
        if n == 1:
            return x
        y = f(x, n >> 1)
        y = g.op(y, y)
        if n & 1:
            y = g.op(y, x)
        return y

    return f


class Tests(unittest.TestCase):
    def test(self) -> None:
        g = Group[int](lambda x, y: x + y, lambda: 0, lambda x: -x)
        f = power_recurse(g)
        print(f(2, 100), 200)


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
