import unittest

import dsalgo._util

import dsalgo.modular


class TestElement(unittest.TestCase):
    def test(self) -> None:
        Mint = dsalgo.modular.define_static_modular_element(10**9 + 7)

        a = 0
        b = Mint(1)
        a += b
        print(a)


class TestInvertExtendedEuclidean(unittest.TestCase):
    def test(self) -> None:
        mod = 17
        x = dsalgo._util.unwrap(
            dsalgo.modular.invert_extended_euclidean(mod, 15)
        )
        self.assertGreaterEqual(x, 0)
        self.assertLess(x, mod)
        self.assertEqual(15 * x % mod, 1)
        self.assertEqual(x, 8)


if __name__ == "__main__":
    unittest.main()
