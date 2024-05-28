from LinkedList import LinkedList, Node

def test_insert():
    """
    Test the insert_node method of the LinkedList class.
    
    This function performs the following tests:
    1. Creates a linked list and appends nodes with values 1, 2, and 3.
    2. Inserts a new node with value 4 after the node with value 2.
       - Asserts that the linked list is now [1, 2, 4, 3].
    3. Inserts a new node with value 5 after the node with value 1.
       - Asserts that the linked list is now [1, 5, 2, 4, 3].
    4. Inserts a new node with value 6 after the node with value 3.
       - Asserts that the linked list is now [1, 5, 2, 4, 3, 6].
    """
    # Create a linked list
    linked_list = LinkedList()

    # Append nodes to the linked list
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    # Create a new node
    new_node = Node(4)

    # Insert the new node after value 2
    linked_list.insert_node(2, new_node)

    # Check if the new node is inserted correctly
    assert linked_list.head.value == 1
    assert linked_list.head.next.value == 2
    assert linked_list.head.next.next.value == 4
    assert linked_list.head.next.next.next.value == 3

    # Insert node at the beginning
    new_node_2 = Node(5)
    linked_list.insert_node(1, new_node_2)

    # Check if the new node is inserted correctly at the beginning
    assert linked_list.head.value == 1
    assert linked_list.head.next.value == 5
    assert linked_list.head.next.next.value == 2
    assert linked_list.head.next.next.next.value == 4
    assert linked_list.head.next.next.next.next.value == 3

    # Test inserting at the end
    new_node_3 = Node(6)
    linked_list.insert_node(3, new_node_3)

    # Check if the new node is inserted correctly at the end
    assert linked_list.head.value == 1
    assert linked_list.head.next.value == 5
    assert linked_list.head.next.next.value == 2
    assert linked_list.head.next.next.next.value == 4
    assert linked_list.head.next.next.next.next.value == 3
    assert linked_list.head.next.next.next.next.next.value == 6
