from typing import List


def b_smooth_sieve(n: int, B: int) -> List[int]:
    """ B-smoothな数を篩う

    Args:
        n (int): nまでのリストを作成する
        B (int): B-smooth

    Returns:
        sieve_list (list[int]): nが素数     <=> sieve_list[n] == 1
                                nはB-smooth <=> sieve_list[n] == n
    Examples:
        >>> sieve_list = b_smooth_sieve(100, 5)
        >>> sieve_list[20] # 20 = 2**2 * 5 は、5-smoothなので出力は20と一致する
        20
        >>> sieve_list[14] # 14 = 2 * 7 は5-smoothではないから出力は14と一致しない
        2
        """
    sieve_list = [1] * (n + 1)
    for p in range(2, B + 1):
        if sieve_list[p] == 1:
            q = p
            while q < n + 1:
                for idx in range(q, n + 1, q):
                    sieve_list[idx] *= p
                q *= p
    return sieve_list
