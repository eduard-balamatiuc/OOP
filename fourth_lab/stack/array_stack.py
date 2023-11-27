class EmptyStackException(Exception):
    """Exception raised when performing an operation on an empty stack."""
    pass

class ArrayStack:
    """Implements a stack data structure using a dynamically resizing array."""

    INITIAL_SIZE = 10

    def __init__(self):
        """Initializes an empty stack."""
        self.__array = [None] * ArrayStack.INITIAL_SIZE
        self.__size = 0

    def push(self, element):
        """
        Adds an element to the top of the stack.

        Args:
            element: The element to be added to the stack.
        """
        if self.__size == len(self.__array):
            self._resize_array(2 * len(self.__array))
        self.__array[self.__size] = element
        self.__size += 1

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
        self.__size -= 1
        element = self.__array[self.__size]
        self.__array[self.__size] = None
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
        return self.__array[self.__size - 1]

    def clear(self):
        """Removes all elements from the stack."""
        for i in range(self.__size):
            self.__array[i] = None
        self.__size = 0

    def get_size(self):
        """
        Returns the number of elements in the stack.

        Returns:
            The number of elements in the stack.
        """
        return self.__size

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return self.__size == 0

    def _resize_array(self, new_capacity):
        """
        Resizes the internal array to the new capacity.

        Args:
            new_capacity: The new capacity of the array.
        """
        new_array = [None] * new_capacity
        for i in range(self.__size):
            new_array[i] = self.__array[i]
        self.__array = new_array
