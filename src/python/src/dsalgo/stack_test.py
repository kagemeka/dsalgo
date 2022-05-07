import unittest

import dsalgo.stack


class Test(unittest.TestCase):
    def test(self) -> None:
        st = dsalgo.stack.Stack[int]()
        st.push(3)
        st.push(2)
        self.assertEqual(len(st), 2)
        self.assertEqual(st.top(), 2)
        self.assertEqual(len(st), 2)
        self.assertEqual(st.pop(), 2)
        self.assertEqual(len(st), 1)


if __name__ == "__main__":
    unittest.main()
