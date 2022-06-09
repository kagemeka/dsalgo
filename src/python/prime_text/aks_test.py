import math

from is_perfect_power import is_perfect_power
from n_times import n_times
from sqrt_int import sqrt_int
from sympy.ntheory import n_order
from totient_function import totient_function


def aks_test(n: int) -> str:
    """AKS法によってn>=2の素数判定を行う。

    確定的アルゴリズム。

    Args:
        n (int): 素数かを判定する対象の自然数

    Returns:
        string: 'composite number' = nは合成数
                'prime number'     = nは素数

    Examples:
        >>> aks_test(31)
        'prime number'
        >>> aks_test(111)
        'composite number'
    """

    def _mul(poly_1, poly_2):
        result = [0] * r
        for i in range(r):
            for j in range(r):
                coef = (i + j) % r
                result[coef] += poly_1[i] * poly_2[j]
                result[coef] %= n
        return result

    if is_perfect_power(n):
        return "composite number"

    r = n
    minimum_order = int(math.log2(n) ** 2)
    for r_ in range(minimum_order, n):
        if math.gcd(n, r_) != 1:
            return "composite number"
        if n_order(n, r_) > minimum_order:
            r = r_

    threshold = int(math.sqrt(totient_function(r)) * math.log2(n)) + 1
    if any(n % p == 0 for p in range(2, threshold)):  # thresholdまで試し割を行う
        return "composite number"
    if sqrt_int(n) < threshold:
        return "prime number"

    for a in range(threshold):
        # (x + a)^n
        poly_1 = [0] * r
        poly_1[0] = a % n
        poly_1[1] = 1
        poly_1 = n_times(poly_1, n, _mul)

        # x^n + a
        poly_2 = [0] * r
        poly_2[0] = a % n
        poly_2[n % r] += 1

        # (x + a)^n と x^n + a が mod x^r - 1, n で合同でないならば合成数と判定する
        if poly_1 != poly_2:
            return "composite number"
    return "prime number"
