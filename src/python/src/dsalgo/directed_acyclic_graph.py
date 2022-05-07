def count_topological_sort(
    graph: list[list[int]],
    mod: int | None = None,
) -> int:
    """Count of Topological Sorting.

    Args:
        graph (list[list[int]]): DAG.
        mod (typing.Optional[int], optional): Modulo. Defaults to None.

    Returns:
        int: count.

    Complexity:
        time: O(NN^2)
        space: O(N^2)
    """
    n = len(graph)
    before = [0] * n
    for u in range(n):
        for v in graph[u]:
            before[v] |= 1 << u
    cnt = [0] * (1 << n)
    cnt[0] = 1
    for s in range(1 << n):
        for i in range(n):
            if ~s >> i & 1:
                continue
            t = s & ~(1 << i)
            if before[i] & ~t != 0:
                continue
            cnt[s] += cnt[t]
            if mod is not None:
                cnt[s] %= mod
    return cnt[-1]
