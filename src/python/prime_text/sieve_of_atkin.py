import math
from typing import List


def sieve_of_atkin(n: int) -> List[bool]:
    """ Atkinの篩によって、nまでの素数リストを生成する

    Args:
        n (int): 生成する素数の最大値。n >= 5

    Returns:
        sieve_list (list[bool]): nが素数   <=> sieve_list[n] == True
                                 nが合成数 <=> sieve_list[n] == False

    Examples:
        >>> sieve_list = sieve_of_atkin(100)
        >>> sieve_list[5]
        True
        >>> sieve_list[12]
        False
    """
    sieve_list = [False] * (n + 1)
    sq_n = math.sqrt(n)

    for x in range(1, int(sq_n/2) + 1):
        z = 4*x**2 + 1  # 4x^2+y^2, y=1
        y_delta = 8
        while z <= n:
            if z % 12 != 9:  # z % 12 in [1, 5]
                sieve_list[z] ^= True
            z += y_delta
            y_delta += 8

    for x in range(1, int(sq_n/math.sqrt(3)) + 1, 2):
        z = 3*x**2 + 4  # 3x^2+y^2, y=2
        y_delta = 12
        while z <= n:
            if z % 12 == 7:
                sieve_list[z] ^= True
            z += y_delta
            y_delta += 8

    for x in range(2, int(sq_n/math.sqrt(2)) + 1):
        z = 2*x*(x+1) - 1  # 3x^2-y^2, y=x-1
        y_delta = 4*x - 8
        while 0 <= y_delta and z <= n:
            if z % 12 == 11:
                sieve_list[z] ^= True
            z += y_delta
            y_delta -= 8

    for r in range(5, int(sq_n) + 1, 2):
        if sieve_list[r]:
            for idx in range(r**2, n+1, r**2):
                sieve_list[idx] = False
    sieve_list[2] = sieve_list[3] = True
    return sieve_list
