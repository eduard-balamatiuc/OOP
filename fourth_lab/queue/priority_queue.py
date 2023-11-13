class EmptyPriorityQueueException(Exception):
    """Exception raised when performing an operation on an empty priority queue."""
    pass

class PriorityQueue:
    """Implements a priority queue using a heap."""

    def __init__(self):
        """Initializes an empty PriorityQueue."""
        self.heap = []

    def enqueue(self, element):
        """
        Adds an element to the priority queue.

        Args:
            element: The element to be added to the priority queue.
        """
        self.heap.append(element)
        self._heapify_up(len(self.heap) - 1)

    def dequeue(self):
        """
        Removes and returns the element with the highest priority.

        Returns:
            The element with the highest priority.

        Raises:
            EmptyPriorityQueueException: If the priority queue is empty.
        """
        if self.is_empty():
            raise EmptyPriorityQueueException("PriorityQueue is empty")
        highest_priority = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return highest_priority
