def count_circle_lattice_points(cx: int, cy: int, r: int, k: int) -> int:
    """
    count up integer point (x, y) in the circle or on it.
    centered at (cx, cy) with radius r.
    and both x and y are multiple of k.

    """
    assert r >= 0 and k >= 0
    cx %= k
    cy %= k

    def is_ok(dx: int, dy: int) -> bool:
        return dx * dx + dy * dy <= r * r

    def count_right(cx: int, cy: int, x0: int) -> int:
        assert x0 == 0 or x0 == k
        y0, y1 = 0, 1
        count = 0
        for x in range((cx + r) // k * k, x0 - 1, -k):
            while is_ok(x - cx, y0 * k - cy):
                y0 -= 1
            while is_ok(x - cx, y1 * k - cy):
                y1 += 1
            count += y1 - y0 - 1
        return count

    return count_right(cx, cy, k) + count_right(-cx, cy, 0)


def count_circle_lattice_points_binary_search(
    cx: int,
    cy: int,
    r: int,
    k: int,
) -> int:
    assert r >= 0 and k >= 0

    def count_up_y(x: int) -> int:
        assert x % k == 0
        rhs = r * r - (x - cx) ** 2

        if rhs < 0:
            return 0

        def is_ok(y: int) -> bool:
            return (y - cy) ** 2 <= rhs

        def search_max() -> int:
            lo, hi = cy, cy + r + 1
            while hi - lo > 1:
                y = (lo + hi) >> 1
                if is_ok(y):
                    lo = y
                else:
                    hi = y
            return lo // k * k

        def search_min() -> int:
            lo, hi = cy - r - 1, cy
            while hi - lo > 1:
                y = (lo + hi) >> 1
                if is_ok(y):
                    hi = y
                else:
                    lo = y
            return (hi + k - 1) // k * k

        return (search_max() - search_min()) // k + 1

    x0 = (cx - r + k - 1) // k * k
    x1 = (cx + r) // k * k
    return sum(count_up_y(x) for x in range(x0, x1 + 1, k))
