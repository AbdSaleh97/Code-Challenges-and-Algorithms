# Write here the code challenge solution
from Queue import MyQueue


# Initialize a queue
queue = MyQueue()

# Push elements into the queue
queue.push(1)
queue.push(2)
queue.push(3)

# Print the queue elements
print("Queue after pushing elements: ", end="")
while not queue.empty():
    print(queue.pop(), end=" ")
print()

# Test empty operation
print("Is the queue empty?:", queue.empty())

# Test pushing and peeking on an empty queue
queue.push(10)
print("Element at the front of the queue:", queue.peek())

# Pop the element
print("Popped element from the queue:", queue.pop())

# Test empty operation after popping an element
print("Is the queue empty now?:", queue.empty())
