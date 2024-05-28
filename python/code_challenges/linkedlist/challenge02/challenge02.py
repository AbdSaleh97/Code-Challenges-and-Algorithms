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


if __name__ == "__main__":
    # Create the linked list and append nodes
    head = ListNode(1)
    head.append(2)
    head.append(3)
    head.append(4)
    head.append(5)
    head.append(6)

    # Print the linked list
    print("Linked List:")
    head.print_linked_list()

    # Find and print the middle to end nodes
    middle_to_end = head.find_middle()
    print("Middle to End Nodes:", middle_to_end)