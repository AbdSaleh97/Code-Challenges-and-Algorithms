from Node import Node

class LinkedList:
    def __init__(self):
        """
        Initialize the LinkedList with a head attribute set to None.
        """
        self.head = None

    def append(self, value):
        """
        Append a new node with the given value to the end of the LinkedList.

        Parameters:
        value (any): The value to be added to the LinkedList.
        """
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def print_linked_list(self):
        """
        Print the values of nodes in the LinkedList starting from the head node.
        The values are printed in the format: value -> value -> ... -> None.
        """
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def insert_node(self, insert_after, node):
        """
        Insert a new node after the node with the specified value in the LinkedList.

        Parameters:
        insert_after (any): The value of the node after which the new node will be inserted.
        node (Node): The new node to be inserted into the LinkedList.

        Raises:
        ValueError: If the node with the value `insert_after` is not found in the LinkedList.
        """
        current = self.head
        while current:
            if current.value == insert_after:
                break
            current = current.next
        else:
            raise ValueError(f"Node with value {insert_after} not found in the LinkedList.")
        
        next_node = current.next
        current.next = node
        node.next = next_node
