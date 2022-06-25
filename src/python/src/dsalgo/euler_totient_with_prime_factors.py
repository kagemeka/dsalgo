import typing
import unittest


def euler_totient_with_prime_factors(
    prime_factors: typing.Callable[[int], typing.List[int]],
    n: int,
) -> int:
    for p in prime_factors(n):
        n -= n // p
    return n


# TODO:
class Test(unittest.TestCase):
    def test(self) -> None:

        # self.assertEqual(
        #     dsalgo.euler_totient_with_prime_factors.naive(100), 40
        # )
        ...


if __name__ == "__main__":
    unittest.main()
