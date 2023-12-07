from abstract_queue import AbstractQueue, EmptyQueueException


class ArrayQueue(AbstractQueue):
    """
    A queue implementation using array up method.

    Attributes:
        __items (list): The list of elements in the queue.
        __size (int): The number of elements in the queue.
    """
    def __init__(self):
        """Initialize an empty ArrayQueue."""
        self.__items = []
        self.__size = 0

    def enqueue(self, element):
        """Add an element to the end of the queue.

        Args:
            element: The element to be added to the queue.
        """
        self.__items.append(element)
        self.__size += 1

    def dequeue(self):
        """Remove and return the first element from the queue.

        Returns:
            The first element of the queue.

        Raises:
            EmptyQueueException: If the queue is empty.
        """
        if self.is_empty():
            raise EmptyQueueException("Queue is empty")
        value = self.__items.pop(0)
        self.__size -= 1
        return value

    def peek(self):
        """Return the first element of the queue without removing it.

        Returns:
            The first element of the queue.

        Raises:
            EmptyQueueException: If the queue is empty.
        """
        if self.is_empty():
            raise EmptyQueueException("Queue is empty")
        return self.__items[0]

    def is_empty(self):
        """Check if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return self.__size == 0

    def get__size(self):
        """Return the number of elements in the queue.

        Returns:
            The number of elements in the queue.
        """
        return self.__size
