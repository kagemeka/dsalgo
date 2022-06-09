import math

from sqrt_int import sqrt_int


def lehman_method(n: int) -> int:
    """Lehman法による素因数分解を行う。
    確定的アルゴリズムで、素数ならば確実に素数と判定し、
    合成数ならば、nの非自明な約数を返す。

    Args:
        n (int): 素因数分解する整数。n > 21 でn^(1/3)以下に非自明な約数は存在しないとする

    Returns:
        int: nが合成数の場合は、nの非自明な約数。
             nが素数の場合は、1

    Examples:
        >>> lehman_method(2021) # 2021 = 43 * 47
        47
        >>> lehman_method(2027) # 2027 is prime
        1
    """
    for k in range(1, math.ceil(math.pow(n, 1 / 3)) + 1):
        head = 2 * math.sqrt(k * n)
        for x in range(
            math.ceil(head),
            math.floor(head + pow(n, 1 / 6) / (4 * math.sqrt(k))) + 1,
        ):
            y2 = x**2 - 4 * k * n
            y = sqrt_int(y2)
            if y**2 == y2:
                return math.gcd(x + y, n)
    return 1
