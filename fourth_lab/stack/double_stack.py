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

    def pop_stack1(self):
        """
        Pops an element from stack 1.

        Returns:
            The popped element from stack 1.

        Raises:
            IllegalStateException: If stack 1 is empty.
        """
        if self.is_empty_stack1():
            raise Exception("Stack 1 is empty.")
        else:
            element = self.array[self.top1]
            self.top1 -= 1
            return element

    def pop_stack2(self):
        """
        Pops an element from stack 2.

        Returns:
            The popped element from stack 2.

        Raises:
            IllegalStateException: If stack 2 is empty.
        """
        if self.is_empty_stack2():
            raise Exception("Stack 2 is empty.")
        else:
            element = self.array[self.top2]
            self.top2 += 1
            return element

    def peek_stack1(self):
        """
        Peeks at the top element of stack 1.

        Returns:
            The top element of stack 1.

        Raises:
            IllegalStateException: If stack 1 is empty.
        """
        if self.is_empty_stack1():
            raise Exception("Stack 1 is empty.")
        else:
            return self.array[self.top1]

    def peek_stack2(self):
        """
        Peeks at the top element of stack 2.

        Returns:
            The top element of stack 2.

        Raises:
            IllegalStateException: If stack 2 is empty.
        """
        if self.is_empty_stack2():
            raise Exception("Stack 2 is empty.")
        else:
            return self.array[self.top2]

    def size_stack1(self):
        """
        Returns the size of stack 1.

        Returns:
            The number of elements in stack 1.
        """
        return self.top1 + 1

