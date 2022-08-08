from __future__ import annotations


def union_find(n: int, edges: list[tuple[int, int]]) -> list[int]:
    import dsalgo.union_find

    uf = dsalgo.union_find.UnionFind(n)
    for u, v in edges:
        uf.unite(u, v)
    return dsalgo.union_find.get_labels(uf)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
