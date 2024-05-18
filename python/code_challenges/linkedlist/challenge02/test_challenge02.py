from challenge02 import ListNode
# Write your test here
# Write your test here

def test_odd_linkedList():
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None
    head = ListNode(1)
    head.append(2)
    head.append(3)
    head.append(4)
    head.append(5)
    head.append(6)
    head.append(7)

    middle_nodes = head.find_middle()
    actual = middle_nodes
    expected = [4,5,6,7]
    assert actual == expected

def test_edge_case_linkedList():
     # Creating a linked list: 1 -> 2 -> 3 -> None
    head = ListNode(1)
    head.append(2)
    head.append(3)

    middle_nodes = head.find_middle()
    actual = middle_nodes
    expected = [2,3]
    assert actual == expected

def test_small_linkedList():
    # Creating a linked list: 1 -> 2 -> None
    head = ListNode(1)
    head.append(2)
    middle_nodes = head.find_middle()
    actual = middle_nodes
    expected = [2]
    assert actual == expected


def test_empty_linked_list():
    # Test an empty linked list
    head = ListNode(None)
    middle_nodes = head.find_middle()
    assert middle_nodes == [None]
    
def test_single_node_linked_list():
    # Test a linked list with a single node
    head = ListNode(1)
    middle_nodes = head.find_middle()
    assert middle_nodes == [1]

def test_large_linked_list():
    # Test a large linked list
    head = ListNode(1)
    for i in range(2, 101): 
        head.append(i)
    middle_nodes = head.find_middle()
    assert middle_nodes == list(range(51, 101)) 
