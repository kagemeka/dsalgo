import unittest

import dsalgo.primality


class TestSieveOfEratosThenes(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            dsalgo.primality.sieve_of_eratosthenes(sieve_size=20),
            [
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                False,
                False,
                False,
                True,
                False,
                True,
                False,
                False,
                False,
                True,
                False,
                True,
            ],
        )


class TestMillerRabin(unittest.TestCase):
    def test(self) -> None:
        for _ in range(100):
            self.assertFalse(dsalgo.primality.miller_rabin_test(561))
            self.assertFalse(dsalgo.primality.miller_rabin_test(512461))

    def test_32(self) -> None:
        self.assertFalse(dsalgo.primality.miller_rabin_test_32(561))
        self.assertFalse(dsalgo.primality.miller_rabin_test_32(512461))

    def test_64(self) -> None:
        self.assertFalse(dsalgo.primality.miller_rabin_test_64(561))
        self.assertFalse(dsalgo.primality.miller_rabin_test_64(512461))

    def test_64_v2(self) -> None:
        self.assertFalse(dsalgo.primality.miller_rabin_test_64_v2(561))
        self.assertFalse(dsalgo.primality.miller_rabin_test_64_v2(512461))


class TestFermat(unittest.TestCase):
    def test(self) -> None:
        for _ in range(100):
            self.assertTrue(dsalgo.primality.fermat_test(998244353))
            self.assertFalse(
                dsalgo.primality.fermat_test(561, check_times=100)
            )
            self.assertFalse(
                dsalgo.primality.fermat_test(512461, check_times=200)
            )


if __name__ == "__main__":
    unittest.main()
