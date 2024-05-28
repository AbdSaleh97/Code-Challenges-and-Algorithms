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

    def find_middle(self):
        """
        Find and return the middle nodes of the linked list.
        If the linked list has an even number of nodes, return the latter half.
        """
        slow = fast = self
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle_nodes = []
        while slow:
            middle_nodes.append(slow.val)
            slow = slow.next
        
        return middle_nodes

    def __str__(self):
        """Generate a string representation of the linked list starting from this node."""
        current = self
        values = []
        while current is not None:
            values.append(str(current.val))
            current = current.next
        return "->".join(values)

def test_odd_linkedList():
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None
    head = ListNode(1)
    head.append(2)
    head.append(3)
    head.append(4)
    head.append(5)
    head.append(6)
    head.append(7)

    print("Original list (odd):")
    print(head)

    middle_nodes = head.find_middle()
    print("Middle nodes (odd):", middle_nodes)

    actual = middle_nodes
    expected = [4, 5, 6, 7]
    assert actual == expected

def test_edge_case_linkedList():
    # Creating a linked list: 1 -> 2 -> 3 -> None
    head = ListNode(1)
    head.append(2)
    head.append(3)

    print("Original list (edge case):")
    print(head)

    middle_nodes = head.find_middle()
    print("Middle nodes (edge case):", middle_nodes)

    actual = middle_nodes
    expected = [2, 3]
    assert actual == expected

def test_small_linkedList():
    # Creating a linked list: 1 -> 2 -> None
    head = ListNode(1)
    head.append(2)

    print("Original list (small):")
    print(head)

    middle_nodes = head.find_middle()
    print("Middle nodes (small):", middle_nodes)

    actual = middle_nodes
    expected = [2]
    assert actual == expected

def test_empty_linked_list():
    # Test an empty linked list
    head = ListNode(None)

    print("Original list (empty):")
    print(head)

    middle_nodes = head.find_middle()
    print("Middle nodes (empty):", middle_nodes)

    assert middle_nodes == [None]

def test_single_node_linked_list():
    # Test a linked list with a single node
    head = ListNode(1)

    print("Original list (single node):")
    print(head)

    middle_nodes = head.find_middle()
    print("Middle nodes (single node):", middle_nodes)

    assert middle_nodes == [1]

def test_large_linked_list():
    # Test a large linked list
    head = ListNode(1)
    for i in range(2, 101):
        head.append(i)

    print("Original list (large):")
    print(head)

    middle_nodes = head.find_middle()
    print("Middle nodes (large):", middle_nodes)

    assert middle_nodes == list(range(51, 101))

# Run the test functions to print and verify the linked lists
test_odd_linkedList()
test_edge_case_linkedList()
test_small_linkedList()
test_empty_linked_list()
test_single_node_linked_list()
test_large_linked_list()
