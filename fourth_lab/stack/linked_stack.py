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

    def pop(self):
        """
        Removes and returns the top element of the stack.

        Returns:
            The element at the top of the stack.

        Raises:
            EmptyStackException: If the stack is empty.
        """
        if self.is_empty():
            raise EmptyStackException("Stack is empty")
        popped = self.head.data
        self.head = self.head.next
        self.size -= 1
        return popped

    def peek(self):
        """
        Returns the top element of the stack without removing it.

        Returns:
            The element at the top of the stack.

        Raises:
            EmptyStackException: If the stack is empty.
        """
        if self.is_empty():
            raise EmptyStackException("Stack is empty")
        return self.head.data

    def clear(self):
        """Removes all elements from the stack."""
        self.head = None
        self.size = 0
