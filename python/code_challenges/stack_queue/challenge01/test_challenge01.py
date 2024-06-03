# Write your test here
import pytest
from Node import Node
from Queue import Queue  # Make sure to import your Queue class correctly


def test_get_size():
    q = Queue()
    q.push(3)
    q.push(2)
    q.push(1)

    assert q.get_size() == 3
    
    q.pop()
    assert q.get_size() == 2
    
    q.pop() 
    assert q.get_size() == 1

    q.pop()
    assert q.get_size() == 0

    q.pop()
    assert q.get_size() == 0

    q.push(1)
    assert q.get_size() == 1

    q.peek() 
    assert q.get_size() == 1

    


def test_queue_push():
    q = Queue()
    q.push(1)
    assert q.front.value == 1
    assert q.rear.value == 1
    assert q.size == 1

    q.push(2)
    assert q.front.value == 1
    assert q.rear.value == 2
    assert q.size == 2

def test_queue_pop():
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)

    assert q.pop() == 1
    assert q.size == 2
    assert q.front.value == 2

    assert q.pop() == 2
    assert q.size == 1
    assert q.front.value == 3

    assert q.pop() == 3
    assert q.size == 0
    assert q.front == None
    assert q.rear == None

def test_queue_peek():
    q = Queue()
    q.push(1)
    assert q.peek() == 1

    q.push(2)
    assert q.peek() == 1

    q.pop()
    assert q.peek() == 2

def test_queue_empty():
    q = Queue()
    assert q.empty() == True

    q.push(1)
    assert q.empty() == False

    q.pop()
    assert q.empty() == True

def test_queue_combined():
    q = Queue()
    assert q.empty() == True

    q.push(1)
    q.push(2)
    q.push(3)

    assert q.peek() == 1
    assert q.pop() == 1
    assert q.peek() == 2
    assert q.pop() == 2
    assert q.peek() == 3
    assert q.pop() == 3
    assert q.empty() == True

if __name__ == "__main__":
    pytest.main()
