import unittest

import dsalgo.euclidean_algorithm


class TestLCM(unittest.TestCase):
    def test_lcm(self) -> None:
        self.assertEqual(dsalgo.euclidean_algorithm.least_common_multiple(0, 0), 0)
        self.assertEqual(dsalgo.euclidean_algorithm.least_common_multiple(0, 10), 0)
        self.assertEqual(dsalgo.euclidean_algorithm.least_common_multiple(10, 0), 0)
        self.assertEqual(dsalgo.euclidean_algorithm.least_common_multiple(9, 6), 18)




if __name__ == "__main__":
    unittest.main()
