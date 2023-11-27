from double_stack import DoubleStack

# Initialize a DoubleStack with a total capacity of 6
double_stack = DoubleStack(6)

print("Pushing elements 10, 20 onto stack 1")
double_stack.push_stack1(10)
double_stack.push_stack1(20)

print("Pushing elements 30, 40 onto stack 2")
double_stack.push_stack2(30)
double_stack.push_stack2(40)

# Display the top elements of each stack
print("Top element of stack 1:", double_stack.peek_stack1())
print("Top element of stack 2:", double_stack.peek_stack2())

# Pop the top elements from each stack
print("Popped from stack 1:", double_stack.pop_stack1())
print("Popped from stack 2:", double_stack.pop_stack2())

# Display the current top elements of each stack
print("Current top of stack 1:", double_stack.peek_stack1())
print("Current top of stack 2:", double_stack.peek_stack2())

# Push another element onto each stack
print("Pushing element 50 onto stack 1")
double_stack.push_stack1(50)
print("Pushing element 60 onto stack 2")
double_stack.push_stack2(60)

# Display the sizes of each stack
print("Size of stack 1:", double_stack.size_stack1())
print("Size of stack 2:", double_stack.size_stack2())

# Check if each stack is empty
print("Is stack 1 empty?:", double_stack.is_empty_stack1())
print("Is stack 2 empty?:", double_stack.is_empty_stack2())
