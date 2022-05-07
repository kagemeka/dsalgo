import unittest

import dsalgo.queue


class Test(unittest.TestCase):
    def test_singly_linked_list(self) -> None:
        que = dsalgo.queue.SinglyLinkedList[int]()
        que.append(1)
        self.assertEqual(len(que), 1)
        self.assertEqual(que.pop(), 1)
        self.assertEqual(len(que), 0)
        with self.assertRaises(Exception):
            que.pop()


if __name__ == "__main__":
    unittest.main()
