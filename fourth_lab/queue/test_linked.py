from linked_queue import LinkedListQueue
from abstract_queue import EmptyQueueException

import unittest

class TestLinkedListQueue(unittest.TestCase):
    """
    A class that contains unit tests for the LinkedListQueue class.

    Methods:
    - test_enqueue: Test the enqueue method of LinkedListQueue.
    - test_dequeue: Test the dequeue method of LinkedListQueue.
    - test_peek: Test the peek method of LinkedListQueue.
    - test_is_empty: Test the is_empty method of LinkedListQueue.
    - test_get_size: Test the get_size method of LinkedListQueue.
    - test_empty_dequeue: Test the behavior of dequeue when the queue is empty.
    - test_empty_peek: Test the behavior of peek when the queue is empty.
    """
    
    def test_enqueue(self):
        """Test the enqueue method of LinkedListQueue."""
        queue = LinkedListQueue()
        queue.enqueue(1)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.get_size(), 1)

    def test_dequeue(self):
        """Test the dequeue method of LinkedListQueue."""
        queue = LinkedListQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        value = queue.dequeue()
        self.assertEqual(value, 1)
        self.assertEqual(queue.get_size(), 1)
        self.assertEqual(queue.peek(), 2)

    def test_peek(self):
        """Test the peek method of LinkedListQueue."""
        queue = LinkedListQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.peek(), 1)

    def test_is_empty(self):
        """Test the is_empty method of LinkedListQueue."""
        queue = LinkedListQueue()
        self.assertTrue(queue.is_empty())
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())
        queue.dequeue()
        self.assertTrue(queue.is_empty())

    def test_get_size(self):
        """Test the get_size method of LinkedListQueue."""
        queue = LinkedListQueue()
        self.assertEqual(queue.get_size(), 0)
        queue.enqueue(1)
        self.assertEqual(queue.get_size(), 1)
        queue.enqueue(2)
        self.assertEqual(queue.get_size(), 2)
        queue.dequeue()
        self.assertEqual(queue.get_size(), 1)

    def test_empty_dequeue(self):
        """Test the behavior of dequeue when the queue is empty."""
        queue = LinkedListQueue()
        with self.assertRaises(EmptyQueueException):
            queue.dequeue()

    def test_empty_peek(self):
        """Test the behavior of peek when the queue is empty."""
        queue = LinkedListQueue()
        with self.assertRaises(EmptyQueueException):
            queue.peek()

if __name__ == '__main__':
    unittest.main()