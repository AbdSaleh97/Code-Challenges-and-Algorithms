# Write your test here
from Queue import MyQueue  

def test_queue_operations():
    queue = MyQueue()

    # Test push operation
    queue.push(1)
    queue.push(2)
    queue.push(3)

    # Test peek operation
    assert queue.peek() == 1

    # Test pop operation
    assert queue.pop() == 1
    assert queue.pop() == 2

    # Test empty operation
    assert not queue.empty()

    # Test pop and peek after further operations
    queue.push(4)
    queue.push(5)
    assert queue.pop() == 3
    assert queue.peek() == 4
    assert queue.pop() == 4
    assert queue.pop() == 5
    assert queue.empty()

def test_empty_queue():
    # Initialize an empty queue
    queue = MyQueue()
    
    # Test empty operation on an empty queue
    assert queue.empty()

def test_queue_with_single_element():
    # Initialize a queue with a single element
    queue = MyQueue()
    queue.push(10)

    # Test peek and pop operations
    assert queue.peek() == 10
    assert queue.pop() == 10

    # Test empty operation
    assert queue.empty()