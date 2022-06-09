import math
import random
from typing import Optional

from inverse_mod import inverse_mod
from sympy.ntheory import primerange


def elliptic_curve_method_fast(
    n: int,
    *,
    B1: int,
    D: int,
    B2: Optional[int] = None,
    sigma: Optional[int] = None,
) -> int:
    """各種の高速化手法を取り入れた楕円曲線法を用いた素因数分解。

    Args:
        n (int): 素因数分解する整数。ただし、gcd(n,6)=1。
        B1 (int), B2(int): 第1段階、第2段階の上限で偶数。B2が設定されない場合はB2=100*B1とする。
        D (int): キャッシュサイズ。大きい程メモリを使う
        sigma (int): 楕円曲線のパラメータ。6以上の整数。指定しない場合はランダム

    Returns:
        int: nの非自明な約数
             失敗した場合は、1

    Examples:
        >>> elliptic_curve_method_fast(1000037 * 1000253, B1=20, B2=200, D=100, sigma=40)
        1000253
    """
    B2 = B2 or 100 * B1

    def _add(P, Q, diff):
        """Montgomery座標における加法 P+Q を計算する。ただし、diff=P-Q, A=1, B=0"""
        P_x, P_z = P
        Q_x, Q_z = Q
        d_x, d_z = diff
        u = (P_x - P_z) * (Q_x + Q_z)
        v = (P_x + P_z) * (Q_x - Q_z)
        add, sub = u + v, u - v
        x = (d_z * add**2) % n
        z = (d_x * sub**2) % n
        return x, z

    def _double(P):
        """Montgomery座標におけるPの2倍を計算する。ただし、A=1, B=0"""
        P_x, P_z = P
        add, sub = (P_x + P_z) ** 2, (P_x - P_z) ** 2
        diff = add - sub
        x = (add * sub) % n
        z = (diff * (sub + a24 * diff)) % n
        return x, z

    def _times(P, k):
        """Montgomery座標におけるPのk倍を計算する。ただし、A=1, B=0"""
        Q = P
        R = _double(P)
        for bit in bin(k)[3:]:
            if bit == "1":
                Q, R = _add(R, Q, P), _double(R)
            else:
                Q, R = _double(Q), _add(Q, R, P)
        return Q

    def _sequence(*, s_1, delta, k=None, s_0=None, s_2=None):
        """s_1, s_2, ..., s_k を返す
        ただし、s_0 = s_1 - delta, s_1 = s_1, s_2 = s_1 + delta, s_3 = s_1 + 2delta
        """

        def _next(pre, current):
            return current, _add(current, delta, pre)

        yield s_1
        pre, current = _next(s_0, s_1) if s_0 is not None else (s_1, s_2)
        yield current
        k = k or B2  # k is None の場合は十分大きな値を設定する
        for _ in range(2, k):
            pre, current = _next(pre, current)
            yield current

    sigma = sigma or random.randint(6, n - 1)
    u = (sigma**2 - 5) % n
    v = (4 * sigma) % n
    diff = v - u
    Q = u_3, _ = pow(u, 3, n), pow(v, 3, n)
    C = (pow(diff, 3, n) * (3 * u + v) * inverse_mod(4 * u_3 * v, n) - 2) % n
    a24 = (C + 2) * inverse_mod(4, n) % n
    # 楕円曲線 y**2 = x**3 + C * x**2 + x を用いる

    # stage 1
    for prime in primerange(2, B1 + 1):
        l = math.floor(math.log(B1) / math.log(prime))
        Q = _times(Q, prime**l)
    assert Q[1] != 0  # Q[1] == 0 は実用上滅多に発生しないが、この場合はB1が大きすぎた
    g = math.gcd(Q[1], n)
    if 1 < g < n:
        return g

    # stage 2
    s_1 = _double(Q)
    # S_i = [2(i+1)]Q
    S = list(_sequence(s_1=s_1, s_2=_double(s_1), delta=s_1, k=D))
    beta = [(x * z) % n for x, z in S]
    g = 1
    B = B1 - 1
    seq = _sequence(s_0=_times(Q, B - 2 * D), s_1=_times(Q, B), delta=S[D - 1])
    for r in range(B, B2, 2 * D):
        R_x, R_z = next(seq)
        alpha = (R_x * R_z) % n
        for q in primerange(r + 2, r + 2 * D + 1):
            delta = (q - r) // 2 - 1
            d_x, d_z = S[delta]
            f = (R_x - d_x) * (R_z + d_z) - alpha + beta[delta]
            g = (g * f) % n
    g = math.gcd(g, n)
    if 1 < g < n:
        return g
    else:
        return 1  # 失敗
