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

 