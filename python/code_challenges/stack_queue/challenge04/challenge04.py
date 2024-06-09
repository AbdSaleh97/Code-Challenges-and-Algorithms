# Write here the code challenge solution


# Write here the code challenge solution
from Queue import Queue


queue = Queue();

queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)

print(queue.print_linked_list())

queue.reverse_queue()

print(queue.print_linked_list())


queue2 = Queue()

queue2.push(0)
queue2.push(1)
queue2.push(2)
queue2.push(3)
queue2.push(4)
queue2.push(5)
queue2.push(6)


print(queue2.print_linked_list())


queue2.reverse_queue()
print(queue2.print_linked_list())

