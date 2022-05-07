from __future__ import annotations


def label_bipartite(graph: list[list[int]]) -> list[int] | None:
    n = len(graph)
    assert n >= 1
    labels = [-1] * n
    labels[0] = 0
    que = [0]
    for u in que:
        for v in graph[u]:
            if labels[v] == labels[u]:
                return None
            if labels[v] != -1:
                continue
            labels[v] = labels[u] ^ 1
            que.append(v)
    assert all(label != -1 for label in labels)
    return labels


def is_bipartite(graph: list[list[int]]) -> bool:
    return label_bipartite(graph) is not None
