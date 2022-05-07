from __future__ import annotations

import unittest

import pytest

import dsalgo.suffix_array

TEST_DATA_STRING = [
    (
        "mmiissiissiippii",
        [15, 14, 10, 6, 2, 11, 7, 3, 1, 0, 13, 12, 9, 5, 8, 4],
    ),
    (
        "mississippi",
        [10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2],
    ),
]

TEST_DATA = [
    (
        [1, 1, 0, 0, 3, 3, 0, 0, 3, 3, 0, 0, 2, 2, 0, 0],
        [15, 14, 10, 6, 2, 11, 7, 3, 1, 0, 13, 12, 9, 5, 8, 4],
    ),
    (
        [1, 0, 3, 3, 0, 3, 3, 0, 2, 2, 0],
        [10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2],
    ),
]


@pytest.mark.parametrize(("word", "suffix_array"), TEST_DATA_STRING)
def test(word: str, suffix_array: list[int]) -> None:
    arr = [ord(c) for c in word]
    assert dsalgo.suffix_array.sais_recurse(arr) == suffix_array
    assert dsalgo.suffix_array.doubling_counting_sort(arr) == suffix_array
    assert dsalgo.suffix_array.doubling(arr) == suffix_array


class Test(unittest.TestCase):
    def test_suffix_array(self) -> None:
        arr = [1, 1, 0, 0, 3, 3, 0, 0, 3, 3, 0, 0, 2, 2, 0, 0]
        suffix_array = [15, 14, 10, 6, 2, 11, 7, 3, 1, 0, 13, 12, 9, 5, 8, 4]
        self.assertEqual(dsalgo.suffix_array.sais_recurse(arr), suffix_array)
        self.assertEqual(
            dsalgo.suffix_array.doubling_counting_sort(arr),
            suffix_array,
        )
        self.assertEqual(dsalgo.suffix_array.doubling(arr), suffix_array)
        arr = [1, 0, 3, 3, 0, 3, 3, 0, 2, 2, 0]
        suffix_array = [10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2]
        self.assertEqual(dsalgo.suffix_array.sais_recurse(arr), suffix_array)
        self.assertEqual(
            dsalgo.suffix_array.doubling_counting_sort(arr),
            suffix_array,
        )
        self.assertEqual(dsalgo.suffix_array.doubling(arr), suffix_array)


if __name__ == "__main__":
    unittest.main()
