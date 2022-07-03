M0 = 0x5555555555555555
M1 = 0x3333333333333333
M2 = 0x0F0F0F0F0F0F0F0F


def popcount(n: int) -> int:
    n -= (n >> 1) & M0
    n = (n & M1) + ((n >> 2) & M1)
    n = (n + (n >> 4)) & M2
    n = n + (n >> 8)
    n = n + (n >> 16)
    n = n + (n >> 32)
    return n & 0x7F
