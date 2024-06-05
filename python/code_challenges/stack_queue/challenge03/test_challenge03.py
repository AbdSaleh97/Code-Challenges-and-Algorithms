# Write your test here
from Stack import Stack
import pytest

@pytest.fixture
def stack():
    # Create a stack for testing
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    return stack

def test_delete_middle_with_even_size(stack):
    # Test deleting middle element from stack with even number of elements
    stack.delete_middle()
    assert stack.to_list()[::-1] == [1, 2, 4, 5]

def test_delete_middle_with_odd_size(stack):
    # Test deleting middle element from stack with odd number of elements
    stack.push(6)
    stack.delete_middle()
    assert stack.to_list()[::-1] == [1, 2, 4, 5, 6]

def test_delete_middle_with_one_element():
    # Test deleting middle element from stack with one element
    stack = Stack()
    stack.push(1)
    stack.delete_middle()
    assert stack.to_list() == []

def test_delete_middle_with_empty_stack():
    # Test deleting middle element from empty stack
    stack = Stack()
    assert stack.delete_middle() == None
    assert stack.to_list() == []

