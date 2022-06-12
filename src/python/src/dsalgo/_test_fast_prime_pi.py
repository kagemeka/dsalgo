import typing

from dsalgo.prime_pi_power_of_10 import PRIME_PI_POWER_OF_10
from dsalgo.prime_pi_table import prime_pi_table


def test_fast_prime_counting(pi: typing.Callable[[int], int]) -> None:
    N = 1 << 10
    ans = prime_pi_table(N)
    for i in range(N):
        assert pi(i) == ans[i]

    for i in range(11):
        assert pi(10**i) == PRIME_PI_POWER_OF_10[i]
