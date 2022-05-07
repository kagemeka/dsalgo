import unittest

import dsalgo.shortest_path


class TestJohnsonSparse(unittest.TestCase):
    def test(self) -> None:
        graph = [
            [(1, 12), (4, 18)],
            [(0, 12), (2, 14)],
            [(1, 14), (3, 7)],
            [(2, 7), (4, 9)],
            [(0, 18), (3, 9)],
        ]
        dists = dsalgo.shortest_path.johnson_sparse(graph)
        self.assertEqual(
            dists,
            [
                [0, 12, 26, 27, 18],
                [12, 0, 14, 21, 30],
                [26, 14, 0, 7, 16],
                [27, 21, 7, 0, 9],
                [18, 30, 16, 9, 0],
            ],
        )

    def test_negative_cycle(self) -> None:
        graph = [
            [(1, -1)],
            [(2, -1)],
            [(0, -1)],
        ]
        with self.assertRaises(dsalgo.shortest_path.NegativeCycleError):
            dsalgo.shortest_path.johnson_sparse(graph)


class TestFloydWarshall(unittest.TestCase):
    def test(self) -> None:
        graph = [
            [None, 12, None, None, 18],
            [12, None, 14, None, None],
            [None, 14, None, 7, None],
            [None, None, 7, None, 9],
            [18, None, None, 9, None],
        ]
        dists = dsalgo.shortest_path.floyd_warshall(graph)
        self.assertEqual(
            dists,
            [
                [0, 12, 26, 27, 18],
                [12, 0, 14, 21, 30],
                [26, 14, 0, 7, 16],
                [27, 21, 7, 0, 9],
                [18, 30, 16, 9, 0],
            ],
        )

    def test_negative_cycle(self) -> None:
        graph = [[None, -1, None], [None, None, -1], [-1, None, None]]
        with self.assertRaises(dsalgo.shortest_path.NegativeCycleError):
            dsalgo.shortest_path.floyd_warshall(graph)


if __name__ == "__main__":
    unittest.main()
