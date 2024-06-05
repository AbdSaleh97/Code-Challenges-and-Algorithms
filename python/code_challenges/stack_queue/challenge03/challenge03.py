# Write here the code challenge solution
from Stack import Stack
def print_stack(stack):
    current = stack.top
    elements = []
    while current:
        elements.append(current.value)
        current = current.next
    print(elements[::-1])  # Print elements in stack order

stack = Stack()
s2 = Stack()
elements = [1, 2, 3, 4, 5]  # Example elements to push onto the stack

e = [1,2,3,4,5,6,7]

for e in e:
    s2.push(e)

for element in elements:
    stack.push(element)

print("Original Stack:")
print_stack(stack)

stack.delete_middle()

print("Stack after deleting the middle element:")
print_stack(stack)




print("Original Stack:")
print_stack(s2)

s2.delete_middle()

print("Stack after deleting the middle element:")
print_stack(s2)