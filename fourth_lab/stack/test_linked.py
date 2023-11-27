from linked_stack import LinkedStack

# Initialize a LinkedStack
stack = LinkedStack()

print("Pushing elements 10, 20, and 30 onto the stack")
stack.push(10)
stack.push(20)
stack.push(30)

# Display the top element of the stack
print("Top element:", stack.peek())

# Pop the top element from the stack
print("Popped element:", stack.pop())

# Display the current top element
print("Current top element:", stack.peek())

# Push another element onto the stack
print("Pushing element 40")
stack.push(40)

# Display the size of the stack
print("Stack size:", stack.get_size())

# Check if stack is empty
print("Is stack empty?:", stack.is_empty())

# Clear the stack
print("Clearing the stack")
stack.clear()

# Check if stack is empty after clearing
print("Is stack empty after clearing?:", stack.is_empty())
