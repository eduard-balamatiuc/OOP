class EmptyStackException(Exception):
    pass

class ArrayStack:
    INITIAL_SIZE = 10

    def __init__(self):
        self.array = [None] * ArrayStack.INITIAL_SIZE
        self.size = 0

    def push(self, element):
        if self.size == len(self.array):
            self._resize_array(2 * len(self.array))
        self.array[self.size] = element
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise EmptyStackException("Stack is empty")
        self.size -= 1
        element = self.array[self.size]
        self.array[self.size] = None
        return element

    def peek(self):
        if self.is_empty():
            raise EmptyStackException("Stack is empty")
        return self.array[self.size - 1]

    def clear(self):
        for i in range(self.size):
            self.array[i] = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def _resize_array(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

