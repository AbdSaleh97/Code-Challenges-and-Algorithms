import pytest
from LinkedList import LinkedList

def test_reverse_linked_list_multiple_elements():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.reverse_linked_list()
    assert str(ll) == "3 -> 2 -> 1 -> None"

def test_reverse_linked_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    ll.reverse_linked_list()
    assert str(ll) == "5 -> 4 -> 3 -> 2 -> 1 -> None"

def test_reverse_linked_list_empty():
    ll = LinkedList()
    ll.reverse_linked_list()
    assert str(ll) == "None"

def test_reverse_linked_list_single_element():
    ll = LinkedList()
    ll.append(1)
    ll.reverse_linked_list()
    assert str(ll) == "1 -> None"

def test_reverse_linked_list_two_elements():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.reverse_linked_list()
    assert str(ll) == "2 -> 1 -> None"

# Add additional tests if needed

# Running the tests with pytest
if __name__ == "__main__":
    pytest.main()
