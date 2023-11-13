class DoubleStack:
    """Implements two stacks within a single array."""

    def __init__(self, capacity):
        """
        Initializes the DoubleStack with a given capacity.

        Args:
            capacity: The total capacity for both stacks combined.
        """
        self.array = [None] * capacity
        self.top1 = -1
        self.top2 = capacity

    def push_stack1(self, element):
        """
        Pushes an element onto stack 1.

        Args:
            element: The element to be pushed onto stack 1.

        Raises:
            IllegalStateException: If stack 1 is full.
        """
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.array[self.top1] = element
        else:
            raise Exception("Stack 1 is full.")

    def push_stack2(self, element):
        """
        Pushes an element onto stack 2.

        Args:
            element: The element to be pushed onto stack 2.

        Raises:
            IllegalStateException: If stack 2 is full.
        """
        if self.top2 > self.top1 + 1:
            self.top2 -= 1
            self.array[self.top2] = element
        else:
            raise Exception("Stack 2 is full.")
