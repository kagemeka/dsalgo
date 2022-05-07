import unittest

import dsalgo.longest_common_prefix_array
import dsalgo.suffix_array

# from dsalgo.string.longest_common_prefix.kasai import lcp_array_kasai
# from dsalgo.string.suffix_array.sa_is_recurse import sa_is_recurse


class TestKasai(unittest.TestCase):
    def test(self) -> None:
        arr = [1, 0, 3, 3, 0, 3, 3, 0, 2, 2, 0]  # mississippi
        sa = dsalgo.suffix_array.sais_recurse(arr)
        """
        sa|lcp |suffix
        -------------------
        10|None|i
        7 |1   |ippi
        4 |1   |issippi
        1 |4   |ississippi
        0 |0   |mississippi
        9 |0   |pi
        8 |1   |ppi
        6 |0   |sippi
        3 |2   |sissippi
        5 |1   |ssippi
        2 |3   |ssissippi
        """
        lcp = [1, 1, 4, 0, 0, 1, 0, 2, 1, 3]
        self.assertEqual(
            dsalgo.longest_common_prefix_array.kasai(arr, sa),
            lcp,
        )


if __name__ == "__main__":
    unittest.main()
