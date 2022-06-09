import math
import random

from sqrt_int import sqrt_int


def pocklington_test(n: int, k: int = 10) -> str:
    """Pocklingtonの定理を用いて、n>2が素数かを判定する。

    Args:
        n (int): 素数判定する対象の整数
        k (int): 試行回数。既定値を10としたが、特に意味はない。

    Returns:
        string: 'prime number'       = nは素数
                'composite number'   = nは合成数
                'possibly composite' = nはおそらく合成数

    Examples:
        >>> pocklington_test(97)
        'prime number'
        >>> pocklington_test(100)
        'composite number'
    """
    # n - 1を試し割する
    N = n - 1
    F = 1
    qs = []
    upper = sqrt_int(N) + 1
    for divisor in range(2, upper):
        count = 0
        while N % divisor == 0:
            N //= divisor
            count += 1
        if count != 0:
            qs.append(divisor)
            F *= divisor**count
            if n <= F**2:
                break
    for _ in range(k):
        a = random.randrange(2, n)
        if pow(a, n - 1, n) != 1:
            return "composite number"
        if all(math.gcd(pow(a, (n - 1) // q, n) - 1, n) == 1 for q in qs):
            return "prime number"
    return "possibly composite"
