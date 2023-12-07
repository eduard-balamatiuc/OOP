from array_down import ArrayQueue
from abstract_queue import EmptyQueueException

import unittest

class TestArrayQueue(unittest.TestCase):
    """
    A test case class for testing the ArrayQueue class.

    This class contains test methods to verify the functionality of the ArrayQueue class.
    """

    def test_enqueue(self):
        # Test method for enqueue operation
        queue = ArrayQueue()
        queue.enqueue(1)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.get_size(), 1)

    def test_dequeue(self):
        # Test method for dequeue operation
        queue = ArrayQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        value = queue.dequeue()
        self.assertEqual(value, 1)
        self.assertEqual(queue.get_size(), 1)

    def test_peek(self):
        # Test method for peek operation
        queue = ArrayQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.peek(), 1)
        value = queue.dequeue()
        self.assertEqual(queue.peek(), 2)

    def test_is_empty(self):
        # Test method for is_empty operation
        queue = ArrayQueue()
        self.assertTrue(queue.is_empty())
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())

    def test_get_size(self):
        # Test method for get_size operation
        queue = ArrayQueue()
        self.assertEqual(queue.get_size(), 0)
        for i in range(3):
            queue.enqueue(i)
        self.assertEqual(queue.get_size(), 3)

    def test_empty_dequeue(self):
        # Test method for empty dequeue operation
        queue = ArrayQueue()
        with self.assertRaises(EmptyQueueException):
            queue.dequeue()

    def test_empty_peek(self):
        # Test method for empty peek operation
        queue = ArrayQueue()
        with self.assertRaises(EmptyQueueException):
            queue.peek()

if __name__ == '__main__':
    unittest.main()
