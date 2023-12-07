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
        self.__capacity = capacity
        self.__array = [None] * capacity
        self.__front = 0
        self.__rear = -1
        self.__size = 0

    def enqueue(self, element):
        """
        Adds an element to the rear of the queue.

        Args:
            element: The element to be added to the queue.
        """
        if self.__size == self.__capacity:
            self._resize_array()
        self.__rear = (self.__rear + 1) % self.__capacity
        self.__array[self.__rear] = element
        self.__size += 1

    def dequeue(self):
        """
        Removes and returns the front element of the queue.

        Returns:
            The element at the front of the queue.

        Raises:
            EmptyQueueException: If the queue is empty.
        """
        if self.is_empty():
            raise EmptyQueueException("Queue is empty")
        removed_element = self.__array[self.__front]
        self.__front = (self.__front + 1) % self.__capacity
        self.__size -= 1
        return removed_element

    def peek(self):
        """
        Returns the front element of the queue without removing it.

        Returns:
            The element at the front of the queue.

        Raises:
            EmptyQueueException: If the queue is empty.
        """
        if self.is_empty():
            raise EmptyQueueException("Queue is empty")
        return self.__array[self.__front]

    def get_size(self):
        """
        Returns the number of elements in the queue.

        Returns:
            The number of elements in the queue.
        """
        return self.__size

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return self.__size == 0

    def clear(self):
        """Removes all elements from the queue."""
        self.__front = 0
        self.__rear = -1
        self.__size = 0
        self.__array = [None] * self.__capacity

    def _resize_array(self):
        """Resizes the internal array to double its current capacity."""
        new_capacity = 2 * self.__capacity
        new_array = [None] * new_capacity
        for i in range(self.__size):
            new_array[i] = self.__array[(self.__front + i) % self.__capacity]
        self.__front = 0
        self.__rear = self.__size - 1
        self.__array = new_array
        self.__capacity = new_capacity
