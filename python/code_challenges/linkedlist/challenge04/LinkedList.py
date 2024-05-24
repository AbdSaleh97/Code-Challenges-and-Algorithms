from Node import Node
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """
        Method to add a node at the end of the LinkedList.
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
        Print the values of nodes in the linked list starting from the current node.
        """
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def __str__(self):
        """
        Returns the content of the linked list as a string.
        """
        current = self.head
        output = ""
        while current:
            output += str(current.value) + " -> "
            current = current.next
        output += "None"
        return output

    def reverse_linked_list(self):
        """
        Reverses the linked list.
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev