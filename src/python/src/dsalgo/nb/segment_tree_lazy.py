
# segment tree lazy
S = typing.TypeVar("S")
F = typing.TypeVar("F")


@nb.njit
def seg_build(
    op_s: typing.Callable[[S, S], S],
    e_s: typing.Callable[[], S],
    e_f: typing.Callable[[], F],
    a: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    r"""Build new segment tree lazy from an array."""
    n = 1 << bit_length(len(a) - 1)
    seg = np.empty((n << 1,) + a.shape[1:], np.int64)
    for i in range(n << 1):
        seg[i] = e_s()
    seg[n : n + len(a)] = a.copy()
    for i in range(n - 1, 0, -1):
        seg[i] = op_s(seg[i << 1], seg[i << 1 | 1])
    lazy = np.empty(n, np.int64)
    for i in range(n):
        lazy[i] = e_f()
    return seg, lazy


@nb.njit
def __seg_apply(
    op_f: typing.Callable[[F, F], F],
    map_: typing.Callable[[F, S], S],
    seg: np.ndarray,
    lazy: np.ndarray,
    i: int,
    f: F,
) -> None:
    seg[i] = map_(f, seg[i])
    if i < len(lazy):
        lazy[i] = op_f(f, lazy[i])


@nb.njit
def __seg_propagate(
    op_f: typing.Callable[[F, F], F],
    e_f: typing.Callable[[], F],
    map_: typing.Callable[[F, S], S],
    seg: np.ndarray,
    lazy: np.ndarray,
    i: int,
) -> None:
    __seg_apply(op_f, map_, seg, lazy, i << 1, lazy[i])
    __seg_apply(op_f, map_, seg, lazy, i << 1 | 1, lazy[i])
    lazy[i] = e_f()


@nb.njit
def __seg_merge(
    op_s: typing.Callable[[S, S], S],
    seg: np.ndarray,
    i: int,
) -> None:
    seg[i] = op_s(seg[i << 1], seg[i << 1 | 1])


@nb.njit
def seg_set(
    op_s: typing.Callable[[S, S], S],
    op_f: typing.Callable[[F, F], F],
    e_f: typing.Callable[[], F],
    map_: typing.Callable[[F, S], S],
    seg: np.ndarray,
    lazy: np.ndarray,
    l: int,
    r: int,
    f: F,
) -> None:
    r"""Set x on [l, r).

    \forall{l \le i \lt r}\ a_i := map_(f, a_i).
        - operate f on a_i from right.
    """
    n = len(seg) >> 1
    assert 0 <= l <= r <= n  # 0 <= l <= r <= size actually
    l, r = l + n, r + n
    h = bit_length(n)

    for i in range(h, 0, -1):
        if (l >> i) << i != l:
            __seg_propagate(op_f, e_f, map_, seg, lazy, l >> i)
        if (r >> i) << i != r:
            __seg_propagate(op_f, e_f, map_, seg, lazy, (r - 1) >> i)

    l0, r0 = l, r
    while l < r:
        if l & 1:
            __seg_apply(op_f, map_, seg, lazy, l, f)
            l += 1
        if r & 1:
            r -= 1
            __seg_apply(op_f, map_, seg, lazy, r, f)
        l, r = l >> 1, r >> 1
    l, r = l0, r0
    for i in range(1, h + 1):
        if (l >> i) << i != l:
            __seg_merge(op_s, seg, l >> i)
        if (r >> i) << i != r:
            __seg_merge(op_s, seg, (r - 1) >> i)


@nb.njit
def seg_get(
    op_s: typing.Callable[[S, S], S],
    e_s: typing.Callable[[], S],
    op_f: typing.Callable[[F, F], F],
    e_f: typing.Callable[[], F],
    map_: typing.Callable[[F, S], S],
    seg: np.ndarray,
    lazy: np.ndarray,
    l: int,
    r: int,
) -> S:
    r"""Get \prod_{j=l}^{r-1}{a_j}."""
    n = len(seg) >> 1
    assert 0 <= l <= r <= n  # 0 <= l <= r <= size actually
    l, r = l + n, r + n
    h = bit_length(n)

    for i in range(h, 0, -1):
        if (l >> i) << i != l:
            __seg_propagate(op_f, e_f, map_, seg, lazy, l >> i)
        if (r >> i) << i != r:
            __seg_propagate(op_f, e_f, map_, seg, lazy, (r - 1) >> i)

    vl, vr = e_s(), e_s()
    while l < r:
        if l & 1:
            vl = op_s(vl, seg[l])
            l += 1
        if r & 1:
            r -= 1
            vr = op_s(seg[r], vr)
        l, r = l >> 1, r >> 1
    return op_s(vl, vr)


@nb.njit
def seg_update(
    op_s: typing.Callable[[S, S], S],
    op_f: typing.Callable[[F, F], F],
    e_f: typing.Callable[[], F],
    map_: typing.Callable[[F, S], S],
    seg: np.ndarray,
    lazy: np.ndarray,
    i: int,
    x: S,
) -> None:
    r"""Replace a_i with x."""
    n = len(seg) >> 1
    assert 0 <= i < n  # 0 <= i < size actually
    i += n
    h = bit_length(n)
    for j in range(h, 0, -1):
        __seg_propagate(op_f, e_f, map_, seg, lazy, i >> j)
    seg[i] = x
    for j in range(1, h + 1):
        __seg_merge(op_s, seg, i >> j)


# segment tree lazy interface.
@nb.njit
def build_seg(a: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    r"""Build interface."""
    return seg_build(seg_op_s, seg_e_s, seg_e_f, a)


@nb.njit
def set_seg(seg: np.ndarray, lazy: np.ndarray, l: int, r: int, f: F) -> None:
    r"""Set interface."""
    seg_set(seg_op_s, seg_op_f, seg_e_f, seg_map, seg, lazy, l, r, f)


@nb.njit
def get_seg(seg: np.ndarray, lazy: np.ndarray, l: int, r: int) -> S:
    r"""Get interface."""
    return seg_get(
        seg_op_s, seg_e_s, seg_op_f, seg_e_f, seg_map, seg, lazy, l, r
    )


@nb.njit
def update_point_seg(seg: np.ndarray, lazy: np.ndarray, i: int, x: S) -> None:
    r"""Update interface."""
    seg_update(seg_op_s, seg_op_f, seg_e_f, seg_map, seg, lazy, i, x)


@nb.njit
def seg_op_s(a: S, b: S) -> S:
    ...


@nb.njit
def seg_e_s() -> S:
    ...


@nb.njit
def seg_op_f(f: F, g: F) -> F:
    ...


@nb.njit
def seg_e_f() -> F:
    ...


@nb.njit
def seg_map(f: F, x: S) -> S:
    ...
