from abstract_queue import AbstractQueue, EmptyQueueException


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListQueue(AbstractQueue):
    """A queue implementation using a linked list.

    Attributes:
        __head (Node): The head of the linked list.
        __tail (Node): The tail of the linked list.
        __size (int): The number of elements in the queue.
    """

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def enqueue(self, element):
        """Adds an element to the end of the queue.

        Args:
            element: The element to be added to the queue.
        """
        new_node = Node(element)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node
        self.__size += 1

    def dequeue(self):
        """Removes and returns the element at the front of the queue.

        Returns:
            The element at the front of the queue.

        Raises:
            EmptyQueueException: If the queue is empty.
        """
        if self.is_empty():
            raise EmptyQueueException("Queue is empty")
        value = self.__head.value
        self.__head = self.__head.next
        self.__size -= 1
        if self.is_empty():
            self.__tail = None
        return value

    def peek(self):
        """Returns the element at the front of the queue without removing it.

        Returns:
            The element at the front of the queue.

        Raises:
            EmptyQueueException: If the queue is empty.
        """
        if self.is_empty():
            raise EmptyQueueException("Queue is empty")
        return self.__head.value

    def is_empty(self):
        """Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return self.__size == 0

    def get_size(self):
        """Returns the number of elements in the queue.

        Returns:
            The number of elements in the queue.
        """
        return self.__size