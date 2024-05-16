# Write here the code challenge solution
class ListNode:
    """A node in a singly-linked list."""
    def __init__(self, val):
        """Initialize a ListNode with the given value."""
        self.val = val
        self.next = None

def delete_node(node):
    """Delete the specified node from the linked list."""
    node.val = node.next.val
    node.next = node.next.next