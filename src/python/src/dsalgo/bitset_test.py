import time
import unittest

import dsalgo.bitset


class Test(unittest.TestCase):
    def test_benchmark(self) -> None:
        n = 1 << 20
        start = time.time()
        length = dsalgo.bitset.bit_length_table(n)
        for i in range(n):
            length[i]
        time_table = time.time() - start

        start = time.time()
        for i in range(n):
            i.bit_length()
        time_std = time.time() - start
        print(time_table, time_std)

    def test_next_power_of_two(self) -> None:
        table = [dsalgo.bitset.next_power_of_two(i) for i in range(6)]
        self.assertEqual(table, [1, 1, 2, 4, 4, 8])


if __name__ == "__main__":
    unittest.main()
