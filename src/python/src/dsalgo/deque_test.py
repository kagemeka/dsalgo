import unittest

import dsalgo.deque


class TestCircularBuffer(unittest.TestCase):
    def test(self) -> None:
        que = dsalgo.deque.CircularBuffer[int](2)
        que.append_right(1)
        self.assertEqual(len(que), 1)
        que.append_left(2)
        self.assertEqual(len(que), 2)
        with self.assertRaises(Exception):
            que.append_right(3)
        self.assertEqual(que.pop_right(), 1)
        self.assertEqual(len(que), 1)
        self.assertEqual(que.pop_right(), 2)
        self.assertEqual(len(que), 0)
        with self.assertRaises(Exception):
            que.pop_left()


class TestDoublyLinkedList(unittest.TestCase):
    def test(self) -> None:
        que = dsalgo.deque.DoublyLinkedList[int]()
        que.append_right(1)
        self.assertEqual(len(que), 1)
        que.append_left(2)
        self.assertEqual(len(que), 2)
        self.assertEqual(que.pop_right(), 1)
        self.assertEqual(len(que), 1)
        self.assertEqual(que.pop_right(), 2)
        self.assertEqual(len(que), 0)
        with self.assertRaises(Exception):
            que.pop_left()


if __name__ == "__main__":
    unittest.main()
