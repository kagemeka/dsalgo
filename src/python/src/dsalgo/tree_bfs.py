def tree_bfs(
    tree_edges: list[tuple[int, int]],
    root: int,
) -> tuple[list[int], list[int]]:
    n = len(tree_edges) + 1
    graph: list[list[int]] = [[] for _ in range(n)]
    for u, v in tree_edges:
        graph[u].append(v)
        graph[v].append(u)
    parent = [-1] * n
    depth = [0] * n
    que = [root]
    for u in que:
        for v in graph[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            depth[v] = depth[u] + 1
            que.append(v)
    return parent, depth
