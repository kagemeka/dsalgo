import unittest

import dsalgo.strongly_connected_components


class Tests(unittest.TestCase):
    def test_kosaraju(self) -> None:
        graph: list[list[int]] = [[1, 3], [2], [3], []]
        labels = dsalgo.strongly_connected_components.kosaraju(graph)
        self.assertEqual(
            labels,
            [0, 1, 2, 3],
        )

    def test_path_based(self) -> None:
        graph: list[list[int]] = [[1, 3], [2], [3], []]
        labels = dsalgo.strongly_connected_components.path_based(graph)
        self.assertEqual(
            labels,
            [3, 2, 1, 0],
        )

    def test_tarjan_lowlink(self) -> None:
        graph: list[list[int]] = [[1, 3], [2], [3], []]
        labels = dsalgo.strongly_connected_components.tarjan_lowlink(graph)
        self.assertEqual(
            labels,
            [3, 2, 1, 0],
        )


if __name__ == "__main__":
    unittest.main()
