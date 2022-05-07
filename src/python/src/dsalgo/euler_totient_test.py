import unittest

import dsalgo.euler_totient


class Test(unittest.TestCase):
    def test_naive(self) -> None:
        self.assertEqual(dsalgo.euler_totient.naive(100), 40)

    def test_lpf(self) -> None:
        euler_totient = dsalgo.euler_totient.lpf(1 << 10)
        self.assertEqual(
            euler_totient(100),
            40,
        )

        self.assertEqual(euler_totient(13), 12)


if __name__ == "__main__":
    unittest.main()
