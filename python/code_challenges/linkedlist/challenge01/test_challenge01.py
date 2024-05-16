# Write your test here
from challenge01 import ListNode, delete_node

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

def test_delete_middle_node():
    """
    Test deleting a middle node (node with value 3) from the linked list.

    Verifies that the node with value 3 is correctly deleted,
    and the linked list remains in the expected state (1 -> 2 -> 4).
    """
    head = create_linked_list()

    # Delete node with value 3 (middle node)
    delete_node(head.next.next)

    # After deletion, linked list should be: 1 -> 2 -> 4
    assert head.val == 1
    assert head.next.val == 2
    assert head.next.next.val == 4
    assert head.next.next.next is None  # Ensure the end of the list is None

def test_delete_first_node():
    """
    Test deleting the first node (node with value 1) from the linked list.

    Verifies that the node with value 1 is correctly deleted,
    and the linked list remains in the expected state (2 -> 3 -> 4).
    """
    head = create_linked_list()

    # Delete the first node (node with value 1)
    delete_node(head)

    # After deletion, linked list should be: 2 -> 3 -> 4
    assert head.val == 2
    assert head.next.val == 3
    assert head.next.next.val == 4
    assert head.next.next.next is None  # Ensure the end of the list is None

def test_delete_second_node():
    """
    Test deleting the second node (node with value 2) from the linked list.

    Verifies that the node with value 2 is correctly deleted,
    and the linked list remains in the expected state (1 -> 3 -> 4).
    """
    head = create_linked_list()

    # Delete the second node (node with value 2)
    delete_node(head.next)

    # After deletion, linked list should be: 1 -> 3 -> 4
    assert head.val == 1
    assert head.next.val == 3
    assert head.next.next.val == 4
    assert head.next.next.next is None  # Ensure the end of the list is None
