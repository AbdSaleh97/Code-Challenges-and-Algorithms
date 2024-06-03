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

    def print_linked_list(self):
        """
        Print the values of nodes in the LinkedList starting from the head node.
        The values are printed in the format: value -> value -> ... -> None.
        """
        current = self.rear
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")