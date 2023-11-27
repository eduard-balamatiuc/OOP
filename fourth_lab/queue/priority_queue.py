class EmptyPriorityQueueException(Exception):
    """Exception raised when performing an operation on an empty priority queue."""
    pass

class PriorityQueue:
    """Implements a priority queue using a heap."""

    def __init__(self):
        """Initializes an empty PriorityQueue."""
        self.__heap = []

    def enqueue(self, element):
        """
        Adds an element to the priority queue.

        Args:
            element: The element to be added to the priority queue.
        """
        self.__heap.append(element)
        self._heapify_up(len(self.__heap) - 1)

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
        highest_priority = self.__heap[0]
        self.__heap[0] = self.__heap[-1]
        self.__heap.pop()
        self._heapify_down(0)
        return highest_priority

    def peek(self):
        """
        Returns the element with the highest priority without removing it.

        Returns:
            The element with the highest priority.

        Raises:
            EmptyPriorityQueueException: If the priority queue is empty.
        """
        if self.is_empty():
            raise EmptyPriorityQueueException("PriorityQueue is empty")
        return self.__heap[0]

    def is_empty(self):
        """
        Checks if the priority queue is empty.

        Returns:
            True if the priority queue is empty, False otherwise.
        """
        return len(self.__heap) == 0

    def get_size(self):
        """
        Returns the number of elements in the priority queue.

        Returns:
            The number of elements in the priority queue.
        """
        return len(self.__heap)

    def clear(self):
        """Removes all elements from the priority queue."""
        self.__heap.clear()

    def _heapify_up(self, index):
        """Ensures the heap property is maintained while adding a new element."""
        while index > 0:
            parent_index = (index - 1) // 2
            if self.__heap[index] < self.__heap[parent_index]:
                self.__heap[index], self.__heap[parent_index] = self.__heap[parent_index], self.__heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        """Ensures the heap property is maintained while removing an element."""
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if left_child_index < len(self.__heap) and self.__heap[left_child_index] < self.__heap[smallest]:
                smallest = left_child_index

            if right_child_index < len(self.__heap) and self.__heap[right_child_index] < self.__heap[smallest]:
                smallest = right_child_index

            if smallest != index:
                self.__heap[index], self.__heap[smallest] = self.__heap[smallest], self.__heap[index]
                index = smallest
            else:
                break
