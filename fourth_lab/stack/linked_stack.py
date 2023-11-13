class EmptyStackException(Exception):
    """Exception raised when performing an operation on an empty stack."""
    pass

class LinkedStack:
    """Implements a stack data structure using a linked list."""

    class Node:
        """A node in the linked list used for the stack."""

        def __init__(self, data):
            """
            Initializes a Node with the given data.

            Args:
                data: The data to be stored in the node.
            """
            self.data = data
            self.next = None

    def __init__(self):
        """Initializes an empty LinkedStack."""
        self.head = None
        self.size = 0

    def push(self, element):
        """
        Adds an element to the top of the stack.

        Args:
            element: The element to be added to the stack.
        """
        new_node = self.Node(element)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
