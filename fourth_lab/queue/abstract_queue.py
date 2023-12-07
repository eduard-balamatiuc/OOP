from abc import ABC, abstractmethod

class EmptyQueueException(Exception):
    """Exception raised when performing an operation on an empty queue."""
    pass

class AbstractQueue(ABC):
    """
    An abstract base class for a queue.
    """

    @abstractmethod
    def enqueue(self, element):
        """
        Adds an element to the back of the queue.
        Args:
            element: The element to be added to the queue.
        """
        pass

    @abstractmethod
    def dequeue(self):
        """
        Removes and returns the front element of the queue.
        Returns:
            The element at the front of the queue.
        Raises:
            EmptyQueueException: If the queue is empty.
        """
        pass

    @abstractmethod
    def peek(self):
        """
        Returns the front element of the queue without removing it.
        Returns:
            The element at the front of the queue.
        Raises:
            EmptyQueueException: If the queue is empty.
        """
        pass

    @abstractmethod
    def is_empty(self):
        """
        Checks if the queue is empty.
        Returns:
            True if the queue is empty, False otherwise.
        """
        pass

    @abstractmethod
    def get_size(self):
        """
        Returns the number of elements in the queue.
        Returns:
            The number of elements in the queue.
        """
        pass