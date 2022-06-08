from sieve_of_eratosthenes import sieve_of_eratosthenes


def divisor_transform(n: int, g):
    """ f(n) = \sum_{d \mid n} g(d) を計算する

    Args:
        n (int): 求める最大値
        g (func): intからTへの関数

    Returns:
        f_list (List[Optional[T]]): [None, f(1), f(2), ..., f(n)]というリスト
                                    f_list[0]はインデックスを揃えるためのダミー

    Examples:
        >>> from totient_function import totient_function
        >>> divisor_transform(11, totient_function)
        [None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    """
    sieve_list = sieve_of_eratosthenes(n)
    f_list = [None] + [g(k) for k in range(1, n+1)]
    for p in range(2, n+1):
        if sieve_list[p]:
            for k in range(1, n//p + 1):
                f_list[k * p] += f_list[k]
    return f_list
