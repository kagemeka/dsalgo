import unittest

from dsalgo.extended_euclidean_modular_gcd_inverse import euclidean_mod_gcd_inv


def modular_inverse_extgcd(mod: int, n: int) -> int:
    gcd, x = euclidean_mod_gcd_inv(mod, n)
    if gcd != 1:
        raise ArithmeticError("mod and n are not coprime")
    return x


class Tests(unittest.TestCase):
    def test(self) -> None:
        mod = 1_000_000_007
        assert modular_inverse_extgcd(mod, 2) == 500_000_004
        assert modular_inverse_extgcd(8, 3) == 3


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
