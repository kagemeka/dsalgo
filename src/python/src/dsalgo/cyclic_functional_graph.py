from __future__ import annotations

import dataclasses


@dataclasses.dataclass
class CyclicFunctionalGraph:
    graph: list[int]
    sequence: list[int]
    order: list[int | None]
    src: int
    start_of_cycle: int
    cycle_size: int


def make_cyclic_functional_graph(
    graph: list[int],
    src: int,
) -> CyclicFunctionalGraph:
    n = len(graph)
    sequence: list[int] = []
    order: list[int | None] = [None] * n
    x = src
    for i in range(n):
        order[x] = i
        sequence.append(x)
        x = graph[x]
        if order[x] is None:
            continue
        cycle_size = i + 1 - order[x]
        start_of_cycle = x
        break
    return CyclicFunctionalGraph(
        graph=graph,
        sequence=sequence,
        order=order,
        src=src,
        start_of_cycle=start_of_cycle,
        cycle_size=cycle_size,
    )
