# mypy: ignore-errors

import typing

import unittest


T = typing.TypeVar("T")


G = typing.List[typing.List[T]]
F = typing.Callable[[T, T, T], T]
Cb = typing.Callable[[int, G], None]


def floyd_warshall(f: F, g: G, cb: typing.Optional[Cb] = None) -> G:
    n = len(g)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = f(g[i][j], g[i][k], g[k][j])
        if cb:
            cb(k, g)
    return g


class Tests(unittest.TestCase):
    def test(self) -> None:
        inf = float("inf")
        g = [
            [0, 12, inf, inf, 18],
            [12, 0, 14, inf, inf],
            [inf, 14, 0, 7, inf],
            [inf, inf, 7, 0, 9],
            [18, inf, inf, 9, 0],
        ]

        def f(x: int, y: int, z: int) -> int:
            return min(x, y + z)

        self.assertEqual(
            floyd_warshall(f, g),
            [
                [0, 12, 26, 27, 18],
                [12, 0, 14, 21, 30],
                [26, 14, 0, 7, 16],
                [27, 21, 7, 0, 9],
                [18, 30, 16, 9, 0],
            ],
        )


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
