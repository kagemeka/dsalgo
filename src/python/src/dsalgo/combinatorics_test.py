import unittest

import dsalgo.algebraic_structure
import dsalgo.combinatorics


class Test(unittest.TestCase):
    def test_pascal_triangle(self) -> None:
        CHOOSE_TABLE_5 = [
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 2, 1, 0, 0],
            [1, 3, 3, 1, 0],
            [1, 4, 6, 4, 1],
        ]
        monoid = dsalgo.algebraic_structure.Monoid[int](
            operation=lambda x, y: x + y,
            identity=lambda: 0,
        )
        self.assertEqual(
            dsalgo.combinatorics.pascal_triangle(monoid, lambda: 1, 5),
            CHOOSE_TABLE_5,
        )

    def test_combinations(self) -> None:
        ANSWER_5_3 = [
            (0, 1, 2),
            (0, 1, 3),
            (0, 1, 4),
            (0, 2, 3),
            (0, 2, 4),
            (0, 3, 4),
            (1, 2, 3),
            (1, 2, 4),
            (1, 3, 4),
            (2, 3, 4),
        ]
        self.assertEqual(
            list(dsalgo.combinatorics.combinations(5, 3)),
            ANSWER_5_3,
        )
        self.assertEqual(
            sorted(list(dsalgo.combinatorics.combinations_next_comb(5, 3))),
            ANSWER_5_3,
        )

    def test_permutations(self) -> None:

        ANSWER_4_2 = [
            (0, 1),
            (0, 2),
            (0, 3),
            (1, 0),
            (1, 2),
            (1, 3),
            (2, 0),
            (2, 1),
            (2, 3),
            (3, 0),
            (3, 1),
            (3, 2),
        ]

        ANSWER_3 = [
            (0, 1, 2),
            (0, 2, 1),
            (1, 0, 2),
            (1, 2, 0),
            (2, 0, 1),
            (2, 1, 0),
        ]

        self.assertEqual(
            list(dsalgo.combinatorics.permutations(4, 2)),
            ANSWER_4_2,
        )
        self.assertEqual(
            list(dsalgo.combinatorics.permutations(3)),
            ANSWER_3,
        )

        self.assertEqual(
            sorted(list(dsalgo.combinatorics.permutations_dfs(4, 2))),
            ANSWER_4_2,
        )
        self.assertEqual(
            sorted(list(dsalgo.combinatorics.permutations_dfs(3))),
            ANSWER_3,
        )

        self.assertEqual(
            list(dsalgo.combinatorics.permutations_next_perm(3)),
            ANSWER_3,
        )

    def test_repeated_permutations(self) -> None:

        ANSWER_4_2 = [
            (0, 0),
            (0, 1),
            (0, 2),
            (0, 3),
            (1, 0),
            (1, 1),
            (1, 2),
            (1, 3),
            (2, 0),
            (2, 1),
            (2, 2),
            (2, 3),
            (3, 0),
            (3, 1),
            (3, 2),
            (3, 3),
        ]
        self.assertEqual(
            list(dsalgo.combinatorics.repeated_permutations_dfs(4, 2)),
            ANSWER_4_2,
        )


if __name__ == "__main__":
    unittest.main()
