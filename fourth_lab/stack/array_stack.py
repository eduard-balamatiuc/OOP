class EmptyStackException(Exception):
    """Exception raised when performing an operation on an empty stack."""
    pass

class ArrayStack:
    """Implements a stack data structure using a dynamically resizing array."""

    INITIAL_SIZE = 10

    def __init__(self):
        """Initializes an empty stack."""
        self.array = [None] * ArrayStack.INITIAL_SIZE
        self.size = 0

    def push(self, element):
        """
        Adds an element to the top of the stack.

        Args:
            element: The element to be added to the stack.
        """
        if self.size == len(self.array):
            self._resize_array(2 * len(self.array))
        self.array[self.size] = element
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
        self.size -= 1
        element = self.array[self.size]
        self.array[self.size] = None
        return element

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
        return self.array[self.size - 1]

    def clear(self):
        """Removes all elements from the stack."""
        for i in range(self.size):
            self.array[i] = None
        self.size = 0

    def size(self):
        """
        Returns the number of elements in the stack.

        Returns:
            The number of elements in the stack.
        """
        return self.size

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return self.size == 0

    def _resize_array(self, new_capacity):
        """
        Resizes the internal array to the new capacity.

        Args:
            new_capacity: The new capacity of the array.
        """
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
