# Write here the code challenge solution
from Queue import Queue


queue = Queue();

queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)


queue.print_linked_list()

# print(queue.peek())
print(queue.pop())
queue.print_linked_list()

print(queue.empty())

queue.pop()
queue.pop()
queue.pop()
queue.pop()

queue.print_linked_list()

print(queue.empty())


print(queue.pop()) # does not allow me to pop any further cause the queue is empty



