import unittest

import dsalgo.combinatorics
import python.src.dsalgo.algebraic_structure


class Test(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
