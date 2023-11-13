class EmptyStackException(Exception):
    pass

class ArrayStack:
    INITIAL_SIZE = 10

    def __init__(self):
        self.array = [None] * ArrayStack.INITIAL_SIZE
        self.size = 0

