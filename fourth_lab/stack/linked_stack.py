from abstract_stack import AbstractStack, EmptyStackException


class Node:
    """Helper class that represents a node in a linked list."""
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedStack(AbstractStack):
    """Implements a stack data structure using a singly linked list."""

    def __init__(self):
        """Initializes an empty stack."""
        self.head = None
        self.size = 0

    def push(self, element):
        """
        Adds an element to the top of the stack.
        
        Args:
            element: The element to be added to the stack.
        """
        new_node = Node(element, self.head)
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
        
        value = self.head.value
        self.head = self.head.next_node
        self.size -= 1
        return value

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
        
        return self.head.value

    def is_empty(self):
        """
        Checks if the stack is empty.
        
        Returns:
            True if the stack is empty, False otherwise.
        """
        return self.size == 0

    def get_size(self):
        """
        Returns the number of elements in the stack.
        
        Returns:
            The number of elements in the stack.
        """
        return self.size
