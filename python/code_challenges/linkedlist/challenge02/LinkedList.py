
from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    # method to add node at the end of the LinkedList

    def append(self,value):
        
        node = Node(value) # creating new node with value

        # if the LinkedList is empty
        if self.head is None:
            self.head = node
        else: # LinkedList is not empty
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def delete_node(self,key):
        temp = self.head

        #1. Empty linkedlist
        if(temp is None):
            return False
        
        #2. If the target is the first node
        if(temp is not None):
            if(temp.value == key):
                self.head = temp.next
                temp = None
                return True

        # serch for the key and delete the target node

        while(temp is not None):
            if temp.value == key:
                break
            prev = temp
            temp = temp.next

            #3. The key does not exists
            if(temp is None):
                return False

            prev.next = temp.next
            temp=None
            return True
        
    def __str__(self):
        '''this function return the content of liked list as string'''
        pass
