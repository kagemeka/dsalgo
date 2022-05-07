"""
Tag
- numbe theory
"""


def floor_sqrt(n: int) -> int:
    r"""Floor Sqrt."""
    assert n >= 0
    x = 0
    while x * x <= n:
        x += 1
    return x - 1
