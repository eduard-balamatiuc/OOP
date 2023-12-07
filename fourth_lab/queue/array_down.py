from abstract_queue import AbstractQueue, EmptyQueueException


class ArrayQueue(AbstractQueue):
    """A queue implementation using an array-based data structure.
    
    Attributes:
        __items (list): The list of elements in the queue.
        __size (int): The number of elements in the queue.
    """

    def __init__(self):
        """Initialize an empty ArrayQueue."""
        self.__items = []
        self.__size = 0

    def enqueue(self, element):
        """Add an element to the back of the queue.

        Args:
            element: The element to be added to the queue.
        """
        self.__items.append(element)
        self.__size += 1

    def dequeue(self):
        """Remove and return the element at the front of the queue.

        Returns:
            The element at the front of the queue.

        Raises:
            EmptyQueueException: If the queue is empty.
        """
        if self.is_empty():
            raise EmptyQueueException("Queue is empty")

        # Shift all elements to the left by one position
        value = self.__items[0]
        for i in range(1, self.__size):
            self.__items[i - 1] = self.__items[i]
        self.__items.pop()  # Remove the last element which is now duplicated
        self.__size -= 1

        return value

    def peek(self):
        """Return the element at the front of the queue without removing it.

        Returns:
            The element at the front of the queue.

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

    def get_size(self):
        """Return the number of elements in the queue.

        Returns:
            The number of elements in the queue.
        """
        return self.__size
