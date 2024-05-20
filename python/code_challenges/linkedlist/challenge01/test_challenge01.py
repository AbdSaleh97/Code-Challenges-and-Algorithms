<<<<<<< HEAD
=======
import pytest

>>>>>>> 0f0f40ca48acee7bd089227cc9f549585fafb8cf
class ListNode:
    """A node in a singly-linked list."""
    def __init__(self, val):
        """Initialize a ListNode with the given value."""
        self.val = val
        self.next = None

    def __str__(self):
        """Generate a string representation of the linked list starting from this node."""
        current = self
        values = []
        while current is not None:
            values.append(str(current.val))
            current = current.next
        return "->".join(values)

def delete_node(node):
    """Delete the specified node from the linked list."""
    node.val = node.next.val
    node.next = node.next.next

<<<<<<< HEAD
=======
@pytest.fixture
>>>>>>> 0f0f40ca48acee7bd089227cc9f549585fafb8cf
def create_linked_list():
    """
    Helper function to create a sample linked list: 1 -> 2 -> 3 -> 4

    Returns:
        ListNode: The head node of the created linked list.
    """
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    return node1  # Return the head node

<<<<<<< HEAD
def print_linked_list(head):
    """Prints the linked list starting from the head node."""
    current = head
    values = []
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values))

def test_delete_middle_node():
=======
def test_delete_middle_node(create_linked_list):
>>>>>>> 0f0f40ca48acee7bd089227cc9f549585fafb8cf
    """
    Test deleting a middle node (node with value 3) from the linked list.

    Verifies that the node with value 3 is correctly deleted,
    and the linked list remains in the expected state (1 -> 2 -> 4).
    """
<<<<<<< HEAD
    head = create_linked_list()
    print("Original list:")
    print_linked_list(head)
=======
    head = create_linked_list
>>>>>>> 0f0f40ca48acee7bd089227cc9f549585fafb8cf

    # Delete node with value 3 (middle node)
    delete_node(head.next.next)

    print("List after deleting middle node (value 3):")
    print_linked_list(head)

    # After deletion, linked list should be: 1 -> 2 -> 4
    assert str(head) == "1->2->4"

def test_delete_first_node(create_linked_list):
    """
    Test deleting the first node (node with value 1) from the linked list.

    Verifies that the node with value 1 is correctly deleted,
    and the linked list remains in the expected state (2 -> 3 -> 4).
    """
<<<<<<< HEAD
    head = create_linked_list()
    print("Original list:")
    print_linked_list(head)
=======
    head = create_linked_list
>>>>>>> 0f0f40ca48acee7bd089227cc9f549585fafb8cf

    # Try to delete the first node (node with value 1)
    delete_node(head)

<<<<<<< HEAD
    print("List after attempting to delete the first node (value 1):")
    print_linked_list(head)

    # After deletion, linked list should be: 2 -> 3 -> 4
=======
    # This test won't work as intended since the head cannot be deleted this way
    # The delete_node function isn't designed to delete the head node in this manner.
    # After deletion, linked list should not have the original head's value
>>>>>>> 0f0f40ca48acee7bd089227cc9f549585fafb8cf
    assert head.val == 2
    assert head.next.val == 3
    assert head.next.next.val == 4
    assert head.next.next.next is None

def test_delete_second_node(create_linked_list):
    """
    Test deleting the second node (node with value 2) from the linked list.

    Verifies that the node with value 2 is correctly deleted,
    and the linked list remains in the expected state (1 -> 3 -> 4).
    """
<<<<<<< HEAD
    head = create_linked_list()
    print("Original list:")
    print_linked_list(head)
=======
    head = create_linked_list
>>>>>>> 0f0f40ca48acee7bd089227cc9f549585fafb8cf

    # Delete the second node (node with value 2)
    delete_node(head.next)

    print("List after deleting second node (value 2):")
    print_linked_list(head)

    # After deletion, linked list should be: 1 -> 3 -> 4
<<<<<<< HEAD
    assert head.val == 1
    assert head.next.val == 3
    assert head.next.next.val == 4
    assert head.next.next.next is None  # Ensure the end of the list is None

# Run the test functions to print and verify the linked lists
test_delete_middle_node()
test_delete_first_node()
test_delete_second_node()
=======
    assert str(head) == "1->3->4"

# To run the tests, execute the following command in your terminal:
# pytest <name_of_this_script>.py
>>>>>>> 0f0f40ca48acee7bd089227cc9f549585fafb8cf
