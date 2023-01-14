import typing

E = typing.Tuple[int, int]
L = typing.List


# TODO: rename as bfs
# (undirected edges, root) -> parent, depth
# unlike in Rust, we don't generalize in Python to avoid overhead
def tree_bfs(e: typing.List[E], r: int) -> typing.Tuple[L[int], L[int]]:
    n = len(e) + 1
    g = [[] for _ in range(n)]
    for u, v in e:
        g[u].append(v)
        g[v].append(u)
    p = [-1] * n
    d = [0] * n
    q = [r]
    for u in q:
        for v in g[u]:
            if v == p[u]:
                continue
            p[v] = u
            d[v] = d[u] + 1
            q.append(v)
    return p, d


# TODO: merge into graphops or treeops


class HLD:
    def heavy_light_decompose(
        tree_edges: list[tuple[int, int]],
        root: int,
    ) -> list[int]:
        # range query: O(\log^2{N})
        n = len(tree_edges) + 1
        graph: list[list[int]] = [[] for _ in range(n)]
        for u, v in tree_edges:
            graph[u].append(v)
            graph[v].append(u)
        labels = [-1] * n
        label = 0

        def dfs(u: int, parent: int) -> int:
            nonlocal label
            size_u = 1
            heavy_node, max_size = None, 0
            for v in graph[u]:
                if v == parent:
                    continue
                size_v = dfs(v, u)
                size_u += size_v
                if size_v > max_size:
                    heavy_node, max_size = v, size_v
            if heavy_node is None:
                labels[u] = label
                label += 1
            else:
                labels[u] = labels[heavy_node]
            return size_u

        dfs(root, -1)
        return labels

    def compute_roots(
        tree_edges: list[tuple[int, int]],
        root: int,
        labels: list[int],
    ) -> list[int]:
        n = len(tree_edges) + 1
        k = max(labels) + 1
        roots = [-1] * k
        min_depth = [n] * k
        _, depth = dsalgo.tree_bfs.tree_bfs(tree_edges, root)
        for i, label in enumerate(labels):
            if depth[i] < min_depth[label]:
                min_depth[label] = depth[i]
                roots[label] = i
        return roots

    # edges = [
    #     (0, 1),
    #     (0, 6),
    #     (0, 10),
    #     (1, 2),
    #     (1, 5),
    #     (2, 3),
    #     (2, 4),
    #     (6, 7),
    #     (7, 8),
    #     (7, 9),
    #     (10, 11),
    # ]
    # root = 0
    # labels = hl_decompose(edges, root)
    # print(labels)
    # roots = compute_roots(edges, root, labels)
    # print(roots)
