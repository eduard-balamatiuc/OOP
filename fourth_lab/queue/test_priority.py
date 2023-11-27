from priority_queue import PriorityQueue

# Initialize a PriorityQueue
pq = PriorityQueue()

print("Enqueueing elements 20, 10, 30")
pq.enqueue(20)
pq.enqueue(10)
pq.enqueue(30)

# Display highest priority element
print("Highest priority element:", pq.peek())

# Dequeue the highest priority element
print("Dequeued highest priority:", pq.dequeue())

# Display current highest priority element
print("Current highest priority element:", pq.peek())

# Enqueue another element
print("Enqueueing element 5")
pq.enqueue(5)

# Display the size of the priority queue
print("Priority Queue size:", pq.get_size())

# Check if priority queue is empty
print("Is priority queue empty?:", pq.is_empty())

# Clear the priority queue
print("Clearing the priority queue")
pq.clear()

# Check if priority queue is empty after clearing
print("Is priority queue empty after clearing?:", pq.is_empty())
