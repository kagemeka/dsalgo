import typing


def solve() -> None:

    # TODO cut below

    ffq = [0] * 0
    fifo_idx = 0

    def fifo_append(x):
        nonlocal ffq
        ffq.append(x)

    def fifo_pop():
        nonlocal ffq, fifo_idx
        v = ffq[fifo_idx]
        fifo_idx += 1
        return v

    def fifo_empty():
        nonlocal ffq, fifo_idx
        return fifo_idx == len(ffq)
