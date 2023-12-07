from abc import ABC, abstractmethod


class EmptyStackException(Exception):
    """Exception raised when performing an operation on an empty stack."""
    pass

class AbstractStack(ABC):
    """
    An abstract base class for a stack.
    """

    @abstractmethod
    def push(self, element):
        """Adds an element to the stack."""
        pass

    @abstractmethod
    def pop(self):
        """Removes and returns the top element of the stack."""
        pass

    @abstractmethod
    def peek(self):
        """Returns the top element without removing it."""
        pass

    @abstractmethod
    def is_empty(self):
        """Checks if the stack is empty."""
        pass

    @abstractmethod
    def get_size(self):
        """Returns the number of elements in the stack."""
        pass
