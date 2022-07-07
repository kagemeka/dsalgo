import typing
import unittest

from dsalgo.algebraic_structure import Semiring

T = typing.TypeVar("T")
Mat = typing.List[typing.List[T]]
Op = typing.Callable[[T, T], T]


def matrix_dot(r: Semiring[T]) -> typing.Callable[[Mat, Mat], Mat]:
    def f(a: Mat, b: Mat) -> Mat:
        c = [[r.zero() for _ in range(len(b[0]))] for _ in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    c[i][j] = r.add(c[i][j], r.mul(a[i][k], b[k][j]))
        return c

    return f


class Tests(unittest.TestCase):
    def test(self) -> None:
        r = Semiring[int](
            add=lambda x, y: x + y,
            zero=lambda: 0,
            mul=lambda x, y: x * y,
            one=lambda: 1,
        )
        f = matrix_dot(r)

        a = [[1, 2], [3, 4]]
        b = [[5, 6, 7], [8, 9, 10]]
        assert f(a, b) == [[21, 24, 27], [47, 54, 61]]


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
