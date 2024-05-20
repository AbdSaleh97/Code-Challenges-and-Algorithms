# Write your test here
import pytest

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

# Test cases
def test_remove_nth_node_from_multi_node_list():
    """Test removing a node from a multi-node linked list."""
    head = ListNode(1)
    head.append(2)
    head.append(3)
    head.append(4)
    
    # Remove the node at index 2 (value 3)
    head.remove_nth_node(2)
    
    assert str(head) == "1->2->4"

def test_remove_head_node():
    """Test removing the head node from a linked list."""
    head = ListNode(1)
    head.append(2)
    head.append(3)
    head.append(4)
    
    # Remove the head node (index 0, value 1)
    head.remove_nth_node(0)
    
    assert str(head) == "2->3->4"

def test_remove_last_node():
    """Test removing the last node from a linked list."""
    head = ListNode(1)
    head.append(2)
    head.append(3)
    head.append(4)
    
    # Remove the last node (index 3, value 4)
    head.remove_nth_node(3)
    
    assert str(head) == "1->2->3"

def test_remove_single_node():
    """Test removing the only node from a single-node linked list."""
    head = ListNode(1)
    
    # Attempt to remove the only node
    try:
        head.remove_nth_node(0)
    except IndexError as e:
        assert str(head) == "1"

def test_remove_node_from_empty_list():
    """Test removing a node from an empty linked list."""
    head = ListNode(None)
    
    # Attempt to remove a node from an empty list
    try:
        head.remove_nth_node(0)
    except IndexError as e:
        assert str(head) == "None"

def test_remove_node_out_of_bounds():
    """Test removing a node with an index out of bounds."""
    head = ListNode(1)
    head.append(2)
    head.append(3)
    head.append(4)
    
    # Attempt to remove a node with an out-of-bounds index
    try:
        head.remove_nth_node(4)
    except IndexError as e:
        assert str(head) == "1->2->3->4"

def test_remove_middle_node():
    """Test removing a middle node from the linked list."""
    head = ListNode(1)
    head.append(2)
    head.append(3)
    head.append(4)
    head.append(5)
    
    # Remove the node at index 2 (value 3)
    head.remove_nth_node(2)
    
    assert str(head) == "1->2->4->5"

if __name__ == "__main__":
    pytest.main()
