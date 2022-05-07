from __future__ import annotations


def base_convert_to_ten(base: int, digits: list[int]) -> int:
    """
    Examples:
        >>> digits = [0, 1, 1]
        >>> base_convert_to_ten(2, digits)
        6
    """
    assert abs(base) >= 2
    p = 1
    n = 0
    for d in digits:
        n += d * p
        p *= base
    return n


def base_convert_from_ten(base: int, n: int) -> list[int]:
    """
    Examples:
        >>> base_convert_from_ten(-2, 10)
        [0, 1, 1, 1, 1]
    """
    assert abs(base) >= 2
    if n == 0:
        return [0]
    digits = []
    while n:
        n, r = divmod(n, base)
        if r < 0:
            r -= base
            n += 1
        digits.append(r)
    return digits


def base_convert(base_from: int, base_to: int, digits: list[int]) -> list[int]:
    return base_convert_from_ten(
        base_to,
        base_convert_to_ten(base_from, digits),
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
