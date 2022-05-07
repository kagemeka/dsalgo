import unittest

from dsalgo.sort import counting_sort, counting_sort_index


class Test(unittest.TestCase):
    def test_counting_sort_index(self) -> None:
        arr = [4, 3, 0, 6, -1, 6, 3]
        answer = [4, 2, 1, 6, 0, 3, 5]
        self.assertEqual(
            counting_sort_index(arr),
            answer,
        )

    def test_counting_sort(self) -> None:
        arr = [4, 3, 0, 6, -1, 6, 3]
        self.assertEqual(
            counting_sort(arr),
            sorted(arr),
        )


if __name__ == "__main__":
    unittest.main()
