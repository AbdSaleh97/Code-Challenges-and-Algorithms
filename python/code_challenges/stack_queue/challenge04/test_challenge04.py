# Write your test here
from Queue import Queue

def test_reverse_queue_empty():
    q = Queue()
    q.reverse_queue()
    assert q.empty() == True



def test_reverse_queue_correctness():
    q = Queue()
    elements = [10, 20, 30, 40, 50]
    for elem in elements:
        q.push(elem)

    q.reverse_queue()

    # Checking the printed representation
    expected_output = "Rear -> 10 -> 20 -> 30 -> 40 -> 50 -> Front"
    assert q.print_linked_list() == expected_output

def test_reverse_queue_multiple_elements():
    q = Queue()
    elements = [1, 2, 3, 4, 5]
    for elem in elements:
        q.push(elem)
    
    q.reverse_queue()

    reversed_elements = elements[::-1]
    for elem in reversed_elements:
        assert q.pop() == elem


def test_reverse_queue_mixed_elements():
    q = Queue()
    elements = [1, "two", 3.0, "four", 5]
    for elem in elements:
        q.push(elem)
    
    q.reverse_queue()

    reversed_elements = elements[::-1]
    for elem in reversed_elements:
        assert q.pop() == elem