import unittest

import dsalgo.numeral_system


class TestClass(unittest.TestCase):
    def test_base_convert_from_ten(self) -> None:
        self.assertEqual(
            dsalgo.numeral_system.base_convert_from_ten(2, 10),
            [0, 1, 0, 1],
        )
        self.assertEqual(
            dsalgo.numeral_system.base_convert_from_ten(-2, 10),
            [0, 1, 1, 1, 1],
        )
        with self.assertRaises(AssertionError):
            dsalgo.numeral_system.base_convert_from_ten(-1, 10)

    def test_base_convert_to_ten(self) -> None:
        self.assertEqual(
            dsalgo.numeral_system.base_convert_to_ten(2, [0, 1, 0, 1]),
            10,
        )
        self.assertEqual(
            dsalgo.numeral_system.base_convert_to_ten(-2, [0, 1, 1, 1, 1]),
            10,
        )
        with self.assertRaises(AssertionError):
            dsalgo.numeral_system.base_convert_to_ten(-1, [0, 1, 0, 1])


if __name__ == "__main__":
    unittest.main()
