from linked_queue import LinkedQueue

queue = LinkedQueue()

print("Enqueueing elements 10, 20, and 30")
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# Display front element
print("Front element:", queue.peek())

# Dequeue two elements
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())

# Display current front element
print("Current front element:", queue.peek())

# Enqueue another element
print("Enqueueing element 40")
queue.enqueue(40)

# Display the size of the queue
print("Queue size:", queue.get_size())

# Check if queue is empty
print("Is queue empty?:", queue.is_empty())

# Clear the queue
print("Clearing the queue")
queue.clear()

# Check if queue is empty after clearing
print("Is queue empty after clearing?:", queue.is_empty())
