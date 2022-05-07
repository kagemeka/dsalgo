import unittest

import dsalgo.verbal_arithmetic


class Test(unittest.TestCase):
    def test(self) -> None:
        words = ["send", "more"]
        result = "money"
        answer = dsalgo.verbal_arithmetic.verbal_arithmetic_from_str(
            words,
            result,
            lo=0,
            hi=10,
        )
        self.assertEqual(
            answer,
            [{"d": 7, "e": 5, "m": 1, "n": 6, "o": 0, "r": 8, "s": 9, "y": 2}],
        )


if __name__ == "__main__":
    unittest.main()
