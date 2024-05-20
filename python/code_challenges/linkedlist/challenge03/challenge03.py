class ListNode:
    """A node in a singly-linked list."""
    def __init__(self, val):
        """Initialize a ListNode with the given value."""
        self.val = val
        self.next = None

    def append(self, val):
        """Append a node with the given value to the end of the linked list."""
        current = self
        while current.next is not None:
            current = current.next
        current.next = ListNode(val)

    def remove_nth_node(self, index):
        """
        Remove the node at the specified index from the linked list.
        """
        # If the index is 0, handle the special case of removing the head
        if index == 0:
            if self.next is not None:
                self.val = self.next.val
                self.next = self.next.next
            else:
                raise IndexError("Cannot remove the only node in the list")
            return

        current = self
        prev = None
        count = 0

        # Traverse the list to find the node just before the index
        while current is not None and count < index:
            prev = current
            current = current.next
            count += 1

        # If the node to be removed is found, adjust the pointers
        if current is not None:
            prev.next = current.next
        else:
            raise IndexError("Index out of bounds")

    def __str__(self):
        """Generate a string representation of the linked list starting from this node."""
        current = self
        values = []
        while current is not None:
            values.append(str(current.val))
            current = current.next
        return "->".join(values)

# # Example usage and test
# head = ListNode(1)
# head.append(2)
# head.append(3)
# head.append(4)
# head.append(5)

# print("Original list:")
# print(head)

# # Remove the node at index 2 (0-based index, value 3)
# head.remove_nth_node(2)

# print("List after removing node at index 2 (value 3):")
# print(head)

# # Remove the node at index 0 (head of the list, value 1)
# head.remove_nth_node(0)

# print("List after removing node at index 0 (value 1):")
# print(head)
