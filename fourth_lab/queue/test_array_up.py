from array_up import ArrayQueue
from abstract_queue import EmptyQueueException

import unittest

class TestArrayQueue(unittest.TestCase):
    """
    A class that contains unit tests for the ArrayQueue class.
    """

    def test_enqueue(self):
        """
        Test case for the enqueue method of ArrayQueue.
        """
        queue = ArrayQueue()
        queue.enqueue(1)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.get_size(), 1)

    def test_dequeue(self):
        """
        Test case for the dequeue method of ArrayQueue.
        """
        queue = ArrayQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        value = queue.dequeue()
        self.assertEqual(value, 1)
        self.assertEqual(queue.get_size(), 1)
        self.assertEqual(queue.peek(), 2)

    def test_peek(self):
        """
        Test case for the peek method of ArrayQueue.
        """
        queue = ArrayQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.peek(), 1)

    def test_is_empty(self):
        """
        Test case for the is_empty method of ArrayQueue.
        """
        queue = ArrayQueue()
        self.assertTrue(queue.is_empty())
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())
        queue.dequeue()
        self.assertTrue(queue.is_empty())

    def test_get_size(self):
        """
        Test case for the get_size method of ArrayQueue.
        """
        queue = ArrayQueue()
        self.assertEqual(queue.get_size(), 0)
        queue.enqueue(1)
        self.assertEqual(queue.get_size(), 1)
        queue.enqueue(2)
        self.assertEqual(queue.get_size(), 2)
        queue.dequeue()
        self.assertEqual(queue.get_size(), 1)

    def test_empty_dequeue(self):
        """
        Test case for dequeuing from an empty queue.
        """
        queue = ArrayQueue()
        with self.assertRaises(EmptyQueueException):
            queue.dequeue()

    def test_empty_peek(self):
        """
        Test case for peeking into an empty queue.
        """
        queue = ArrayQueue()
        with self.assertRaises(EmptyQueueException):
            queue.peek()

if __name__ == '__main__':
    unittest.main()