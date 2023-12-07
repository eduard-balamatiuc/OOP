from abstract_queue import AbstractQueue, EmptyQueueException


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListQueue(AbstractQueue):
    """A queue implementation using a linked list.

    Attributes:
        head (Node): The head of the linked list.
        tail (Node): The tail of the linked list.
        size (int): The number of elements in the queue.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, element):
        """Adds an element to the end of the queue.

        Args:
            element: The element to be added to the queue.
        """
        new_node = Node(element)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        """Removes and returns the element at the front of the queue.

        Returns:
            The element at the front of the queue.

        Raises:
            EmptyQueueException: If the queue is empty.
        """
        if self.is_empty():
            raise EmptyQueueException("Queue is empty")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
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
        return self.head.value

    def is_empty(self):
        """Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return self.size == 0

    def get_size(self):
        """Returns the number of elements in the queue.

        Returns:
            The number of elements in the queue.
        """
        return self.size