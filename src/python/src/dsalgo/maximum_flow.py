from __future__ import annotations

from dsalgo.constant import INT_INF


# O(EV^2)
def dinic(
    capacity_graph: list[list[tuple[int, int]]],
    src: int,
    sink: int,
) -> int:
    n = len(capacity_graph)
    residual_flow = [[0] * n for _ in range(n)]
    for u in range(n):
        for v, capacity in capacity_graph[u]:
            residual_flow[u][v] += capacity

    graph: list[list[int]] = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if residual_flow[u][v] > 0:
                graph[u].append(v)
    level = [-1] * n

    def update_level() -> None:
        nonlocal graph, level
        for i in range(n):
            level[i] = -1
        level[src] = 0
        que = [src]
        for u in que:
            for v in graph[u]:
                if level[v] != -1:
                    continue
                level[v] = level[u] + 1
                que.append(v)

    def flow_to_sink(u: int, flow_in: int) -> int:
        nonlocal residual_flow, graph, level
        if u == sink:
            return flow_in
        flow_out = 0
        edges = graph[u].copy()
        graph[u].clear()
        for v in edges:
            if level[v] == -1 or level[v] <= level[u]:
                graph[u].append(v)
                continue
            flow = flow_to_sink(v, min(flow_in, residual_flow[u][v]))
            residual_flow[u][v] -= flow
            if residual_flow[u][v] > 0:
                graph[u].append(v)
            if residual_flow[v][u] == 0 and flow > 0:
                graph[v].append(u)
            residual_flow[v][u] += flow
            flow_in -= flow
            flow_out += flow
        return flow_out

    flow = 0
    while True:
        update_level()
        if level[sink] == -1:
            break
        flow += flow_to_sink(src, INT_INF)
    return flow


# O(V^2 + Ef)
def ford_fulkerson(
    capacity_graph: list[list[tuple[int, int]]],
    src: int,
    sink: int,
) -> int:
    n = len(capacity_graph)
    residual_flow = [[0] * n for _ in range(n)]
    for u in range(n):
        for v, capacity in capacity_graph[u]:
            residual_flow[u][v] += capacity

    graph: list[list[int]] = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if residual_flow[u][v] > 0:
                graph[u].append(v)
    visited = [False] * n

    def augment_flow(u: int, flow_in: int) -> int:
        visited[u] = True
        if u == sink:
            return flow_in
        edges = graph[u].copy()
        graph[u].clear()
        flow = 0
        for v in edges:
            if visited[v] or flow > 0:
                graph[u].append(v)
                continue
            flow = augment_flow(v, min(flow_in, residual_flow[u][v]))
            residual_flow[u][v] -= flow
            if residual_flow[u][v] > 0:
                graph[u].append(v)
            if flow == 0:
                continue
            if residual_flow[v][u] == 0:
                graph[v].append(u)
            residual_flow[v][u] += flow
        return flow

    flow = 0
    while True:
        for i in range(n):
            visited[i] = False
        f = augment_flow(src, INT_INF)
        if f == 0:
            break
        flow += f
    return flow


# O(V^2 + VE^2)
def edmonds_karp(
    capacity_graph: list[list[tuple[int, int]]],
    src: int,
    sink: int,
) -> int:
    n = len(capacity_graph)
    residual_flow = [[0] * n for _ in range(n)]
    for u in range(n):
        for v, capacity in capacity_graph[u]:
            residual_flow[u][v] += capacity

    graph: list[list[int]] = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if residual_flow[u][v] > 0:
                graph[u].append(v)

    def find_path() -> list[int]:
        parent = [-1] * n
        parent[src] = src
        que = [src]
        for u in que:
            graph[u] = [v for v in graph[u] if residual_flow[u][v] != 0]
            for v in graph[u]:
                if parent[v] != -1:
                    continue
                parent[v] = u
                que.append(v)
        v = sink
        path = [v]
        while parent[v] != -1 and v != src:
            v = parent[v]
            path.append(v)
        return path

    def augment_flow(path: list[int]) -> int:
        flow = INT_INF
        for i in range(len(path) - 1):
            flow = min(flow, residual_flow[path[i + 1]][path[i]])
        assert flow != INT_INF
        for i in range(len(path) - 1):
            u, v = path[i + 1], path[i]
            residual_flow[u][v] -= flow
            if residual_flow[v][u] == 0:
                graph[v].append(u)
            residual_flow[v][u] += flow
        return flow

    flow = 0
    while True:
        path = find_path()
        if len(path) == 1:
            break
        flow += augment_flow(path)
    return flow


def mpm() -> None:
    ...


def push_relabel_fifo_verted() -> None:
    ...


def push_relabel_dist_verted() -> None:
    ...


def push_relabel_dynamic_tree() -> None:
    ...


def krt() -> None:
    ...


def binary_blocking_flow() -> None:
    ...


def orlin() -> None:
    ...
