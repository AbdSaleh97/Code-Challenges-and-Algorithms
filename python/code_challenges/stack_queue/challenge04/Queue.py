from Node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0


    def push(self,value):
        node = Node(value)
        if self.size == 0:
            self.front = node
            self.rear = node
        else:
            node.next = self.rear
            self.rear = node

        self.size += 1
        

    def pop(self):
        if self.size <= 0:
            return False
        elif self.size == 1:
            temp = self.front
            self.front = None
            self.rear = None
            self.size -= 1
            return temp.value
        else:
            temp = self.front
            node = self.rear
            while node.next:
                if node.next == temp:
                    self.front = node
                    self.size -= 1
                    node.next = None
                    return temp.value
                node = node.next

    def peek(self):
        return self.front.value

    def empty(self):
        # if size == 0 return true else return false
        return self.size == 0
    
    def get_size(self):
        return self.size
    
    def reverse_queue(self):
        if self.empty():
            return 
        if self.get_size() == 1:
            return
        prev = self.rear
        current = self.rear.next
        prev.next = None

        while current != self.front:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        if current == self.front:
            current.next = prev
            self.front = self.rear
            self.rear = current
            
    def print_linked_list(self):
            """
            Print the values of nodes in the LinkedList starting from the head node.
            The values are printed in the format: value -> value -> ... -> Rear -> Front.
            """
            arr = ["Rear"]
            current = self.rear
            while current:
                arr.append(str(current.value))  # Append the value as a string
                current = current.next
            arr.append("Front")  # Append "Front" at the end
            return " -> ".join(arr)  # Join elements with " -> "
