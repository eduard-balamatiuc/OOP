from abstract_stack import AbstractStack, EmptyStackException


class ArrayDownStack(AbstractStack):
    """Implements an "array down" stack using a dynamically resizing array."""

    INITIAL_SIZE = 10

    def __init__(self):
        """Initializes an empty stack."""
        self.__array = [None] * ArrayDownStack.INITIAL_SIZE
        self.__top_index = len(self.__array) - 1

    def push(self, element):
        """
        Adds an element to the top of the stack.
        Args:
            element: The element to be added to the stack.
        """
        if self.__top_index < 0:
            self._resize_array(2 * len(self.__array))
        self.__array[self.__top_index] = element
        self.__top_index -= 1

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
        self.__top_index += 1
        element = self.__array[self.__top_index]
        self.__array[self.__top_index] = None
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
        return self.__array[self.__top_index + 1]

    def is_empty(self):
        """
        Checks if the stack is empty.
        Returns:
            True if the stack is empty, False otherwise.
        """
        return self.__top_index == len(self.__array) - 1

    def get_size(self):
        """
        Returns the number of elements in the stack.
        Returns:
            The number of elements in the stack.
        """
        return len(self.__array) - 1 - self.__top_index

    def _resize_array(self, new_capacity):
        """
        Resizes the array to the specified capacity.
        Args:
            new_capacity: The new capacity of the array.
        """
        new_array = [None] * new_capacity
        old_capacity = len(self.__array)
        for i in range(old_capacity):
            new_array[i + new_capacity - old_capacity] = self.__array[i]
        self.__array = new_array
        self.__top_index += new_capacity - old_capacity
