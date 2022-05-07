from __future__ import annotations

import dataclasses
import typing

from dsalgo.type import T, U


@dataclasses.dataclass
class Edge(typing.Generic[T]):
    u: int
    v: int
    data: T | None = None


@dataclasses.dataclass
class Graph(typing.Generic[T, U]):
    edges: list[list[Edge[U]]]
    node_datas: list[T] | None = None


def add_edge(graph: Graph[T, U], edge: Edge[U]) -> None:
    graph.edges[edge.u].append(edge)


@dataclasses.dataclass
class UndirectedGraph(typing.Generic[T, U]):
    edges: list[Edge[U]]
    node_datas: list[T] | None = None


@dataclasses.dataclass
class DenseGraph(typing.Generic[T, U]):
    edge_datas: list[list[U | None]]
    node_datas: list[T] | None = None


def edges_with_data_to_graph(
    size: int,
    edges: list[tuple[int, ...]],
) -> list[list[tuple[int, ...]]]:
    graph: list[list[tuple[int, ...]]] = [[] for _ in range(size)]
    for u, v, *datas in edges:
        graph[u].append((v, *datas))
        graph[v].append((u, *datas))
    return graph


def edges_to_graph(
    size: int,
    edges: list[tuple[int, int]],
) -> list[list[int]]:
    graph: list[list[int]] = [[] for _ in range(size)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph
