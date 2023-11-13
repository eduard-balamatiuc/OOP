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

