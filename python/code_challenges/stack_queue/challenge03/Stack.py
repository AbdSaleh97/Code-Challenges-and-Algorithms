from Node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,value):
        node = Node(value)
        self.size = self.size +1

        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
        if self.isEmpty():
            return False
        else:
            self.size = self.size -1
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
    
    def peek(self):
        if self.isEmpty():
            return False
        else:
            return self.top.value
        
    def get_size(self):
        return self.size
    
    def isEmpty(self):
       return self.top is None
    
    def delete_middle(self):
    
        if self.isEmpty():
            return None
        
        if self.get_size() == 1:
            return self.pop()
        
        target = self.top
        prev = None
        for i in range(self.size//2):
            prev = target
            target = target.next
        prev.next = target.next
        target.next = None
        self.size += 1

    def to_list(self):
        result = []
        current = self.top
        while current:
            result.append(current.value)
            current = current.next
        return result