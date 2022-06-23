import typing

import unittest

T = typing.TypeVar("T")
G = typing.List[typing.List[T]]


def floyd_warshall(g: G, inf: T) -> G:
    n = len(g)
    for k in range(n):
        for i in range(n):
            d0 = g[i][k]
            if d0 == inf:
                continue
            for j in range(n):
                d1 = g[k][j]
                if d1 == inf or d0 + d1 >= g[i][j]:
                    continue
                g[i][j] = d0 + d1
    return g


class Tests(unittest.TestCase):
    def test(self) -> None:
        inf = 1 << 60
        g = [
            [0, 12, inf, inf, 18],
            [12, 0, 14, inf, inf],
            [inf, 14, 0, 7, inf],
            [inf, inf, 7, 0, 9],
            [18, inf, inf, 9, 0],
        ]
        self.assertEqual(
            floyd_warshall(g),
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
