from fibonacci_sequence import fibonacci_sequence
from legendre_symbol import legendre_symbol


def fibonacci_pseudoprime_test(n: int) -> str:
    """Fibonacci数列を用いた素数判定を行う。

    Args:
        n (int): 素数判定を行う対象の整数

    Returns:
        string: 'composite number' = nは合成数
                'probable prime'   = nはおそらく素数

    Examples:
        >>> fibonacci_pseudoprime_test(101)
        'probable prime'
        >>> fibonacci_pseudoprime_test(323)
        'probable prime'
    """
    if fibonacci_sequence(n - legendre_symbol(n, 5)) % n != 0:
        return "composite number"
    return "probable prime"
