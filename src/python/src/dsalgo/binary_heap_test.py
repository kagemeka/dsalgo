import heapq
import unittest

import dsalgo.binary_heap


class Test(unittest.TestCase):
    def test(self) -> None:
        hq = dsalgo.binary_heap.BinaryMinHeap[int]()
        hq_std: list[int] = []
        for i in range(10, -1, -1):
            hq.push(i)
            heapq.heappush(hq_std, i)
            assert list(hq) == hq_std
            print(hq)
        while hq:
            x, y = hq.pop(), heapq.heappop(hq_std)
            assert x == y and list(hq) == hq_std
            print(x, hq)


if __name__ == "__main__":
    unittest.main()
