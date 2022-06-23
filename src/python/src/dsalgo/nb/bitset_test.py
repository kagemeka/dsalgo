import unittest

import numpy as np

import nb.bitset


class Test(unittest.TestCase):
    def test(self) -> None:
        self.assertTrue(
            np.all(
                nb.bitset.bit_length_table(10)
                == np.array([0, 1, 2, 2, 3, 3, 3, 3, 4, 4])
            ),
        )


if __name__ == "__main__":
    unittest.main()
