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
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, element):
        """
        Adds an element to the rear of the queue.

        Args:
            element: The element to be added to the queue.
        """
        new_node = self.Node(element)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

