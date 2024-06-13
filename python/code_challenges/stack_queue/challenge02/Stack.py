class Node:
    """
    Represents a node in a linked list.

    Attributes:
        value: The value stored in the node.
        next: A reference to the next node in the linked list.
    """
    def __init__(self, value):
        """
        Initializes a new node with the given value and sets the next reference to None.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.next = None

class Stack:
    """
    Represents a stack data structure using a linked list for storage.

    Attributes:
        top: The top node of the stack.
    """
    def __init__(self):
        """
        Initializes an empty stack by setting the top reference to None.
        """
        self.top = None

    def push(self, value):
        """
        Pushes a new value onto the top of the stack.

        Args:
            value: The value to be pushed onto the stack.
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Removes and returns the value at the top of the stack. If the stack is empty, returns None.

        Returns:
            The value at the top of the stack, or None if the stack is empty.
        """
        if self.top is None:
            return None
        removed_value = self.top.value
        self.top = self.top.next
        return removed_value

    def peek(self):
        """
        Returns the value at the top of the stack without removing it. If the stack is empty, returns None.

        Returns:
            The value at the top of the stack, or None if the stack is empty.
        """
        if self.top is None:
            return None
        return self.top.value

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return self.top is None
