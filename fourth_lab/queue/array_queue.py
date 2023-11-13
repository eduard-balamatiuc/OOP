class EmptyQueueException(Exception):
    """Exception raised when performing an operation on an empty queue."""
    pass

class ArrayQueue:
    """Implements a queue data structure using a dynamically resizing array."""

    def __init__(self, capacity):
        """
        Initializes the ArrayQueue with a given capacity.

        Args:
            capacity: The initial capacity of the queue.
        """
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

