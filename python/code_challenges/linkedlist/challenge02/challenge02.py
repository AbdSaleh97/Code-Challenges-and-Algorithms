import math
class ListNode:
    def __init__(self, val):
        """
        Initialize a ListNode with the given value.
        """
        self.val = val
        self.next = None
    def append(self, value):
        """
        Append a new node with the given value to the end of the linked list.
        """
        node = ListNode(value)  # Creating a new node with the given value
        # If the LinkedList is empty
        if self.next is None:
            self.next = node
        else:  # LinkedList is not empty
            current = self
            while current.next is not None:
                current = current.next
            current.next = node

    def print_linked_list(self):
        """
        Print the values of nodes in the linked list starting from the current node.
        """
        current = self
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    def find_middle(self):
        """
        Find the nodes from the middle to the end of the linked list.
        """
        arr = []
        current = self
        while current:
            arr.append(current.val)
            current = current.next
        
        middle_nodes = arr[len(arr) // 2:]  # Start from the middle to the end
        
        return middle_nodes
