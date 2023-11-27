class EmptyQueueException(Exception):
    """Exception raised when performing an operation on an empty queue."""
    pass

class LinkedQueue:
    """Implements a queue data structure using a linked list."""

    class Node:
        """A node in the linked list used for the queue."""

        def __init__(self, data):
            """
            Initializes a Node with the given data.

            Args:
                data: The data to be stored in the node.
            """
            self.data = data
            self.next = None

    def __init__(self):
        """Initializes an empty queue."""
        self.__front = None
        self.__rear = None
        self.__annotations__size = 0

    def enqueue(self, element):
        """
        Adds an element to the rear of the queue.

        Args:
            element: The element to be added to the queue.
        """
        new_node = self.Node(element)
        if self.is_empty():
            self.__front = new_node
            self.__rear = new_node
        else:
            self.__rear.next = new_node
            self.__rear = new_node
        self.__annotations__size += 1

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
        removed_data = self.__front.data
        self.__front = self.__front.next
        self.__annotations__size -= 1
        if self.is_empty():
            self.__rear = None
        return removed_data

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
        return self.__front.data

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return self.__annotations__size == 0

    def get_size(self):
        """
        Returns the number of elements in the queue.

        Returns:
            The number of elements in the queue.
        """
        return self.__annotations__size

    def clear(self):
        """Removes all elements from the queue."""
        self.__front = None
        self.__rear = None
        self.__annotations__size = 0