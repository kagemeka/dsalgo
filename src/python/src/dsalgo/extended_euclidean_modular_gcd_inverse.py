import unittest


def euclidean_mod_gcd_inv(mod: int, n: int) -> tuple[int, int]:
    assert 0 < n < mod
    a, b = n, mod
    x00, x01 = 1, 0  # first row of matrix identity element.
    while b:
        x00, x01 = x01, x00 - a // b * x01
        a, b = b, a % b
    gcd = a
    u = mod // gcd
    if x00 < 0:
        x00 += u
    assert 0 <= x00 < u
    return gcd, x00


class Tests(unittest.TestCase):
    def test(self) -> None:
        # extgcd_modinv(10, 0) runtime error
        assert euclidean_mod_gcd_inv(5, 2) == (1, 3)
        assert euclidean_mod_gcd_inv(18, 12) == (6, 2)
        assert euclidean_mod_gcd_inv(111, 30) == (3, 26)
        # gcd(111, 30) = 3
        # 111 / 3 = 37, 30 / 3 = 10, 10^{-1} \equiv 26 \mod 37


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
