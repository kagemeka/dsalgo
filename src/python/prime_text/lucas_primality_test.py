import random

from sympy import factorint


def lucas_primality_test(n: int, k: int = 10) -> str:
    """Lucasの定理を用いて、n > 2が素数かを判定する。

    Args:
        n (int): 素数判定する対象の自然数
        k (int): 試行回数。nが素数で十分大きい場合、
                 1回の試行で素数と判定できる確率は、少なくとも 1 / (2 ln ln n)

    Returns:
        string: 'prime number'       = nは素数
                'composite number'   = nは合成数
                'possibly composite' = nはおそらく合成数

    Examples:
        >>> lucas_primality_test(93)
        'composite number'
        >>> lucas_primality_test(101)
        'prime number'
    """
    qs = [*factorint(n - 1)]
    for _ in range(k):
        a = random.randrange(2, n)
        if pow(a, n - 1, n) != 1:
            return "composite number"
        if all(pow(a, (n - 1) // q, n) != 1 for q in qs):
            return "prime number"
    return "possibly composite"
