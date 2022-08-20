import unittest

import dsalgo.chinese_remainder_theorem_garner


class Test(unittest.TestCase):
    def test_form(self) -> None:
        pairs = [
            (15, 2),
            (17, 8),
        ]
        self.assertEqual(
            dsalgo.chinese_remainder_theorem_garner.garner_form(pairs),
            212,
        )

    def test_form_mod(self) -> None:
        pairs = [
            (15, 2),
            (17, 8),
        ]
        self.assertEqual(
            dsalgo.chinese_remainder_theorem_garner.garner_modular_form(998_244_353, pairs),
            212,
        )
        self.assertEqual(
            dsalgo.chinese_remainder_theorem_garner.garner_modular_form(100, pairs),
            12,
        )


if __name__ == "__main__":
    unittest.main()
