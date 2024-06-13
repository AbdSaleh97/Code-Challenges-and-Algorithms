from Node import Node

class Stack:
    """
    A class used to represent a Stack.

    Attributes
    ----------
    top : Node
        The top node of the stack.
    size : int
        The size of the stack.

    Methods
    -------
    push(value):
        Pushes a value onto the stack.
    pop():
        Pops the top value off the stack.
    peek():
        Returns the top value of the stack without removing it.
    get_size():
        Returns the size of the stack.
    isEmpty():
        Checks if the stack is empty.
    delete_middle():
        Deletes the middle element from the stack.
    to_list():
        Returns a list of all values in the stack.
    """
    
    def __init__(self):
        """Initializes the stack with no elements."""
        self.top = None
        self.size = 0

    def push(self, value):
        """
        Pushes a value onto the stack.

        Parameters
        ----------
        value : any
            The value to be pushed onto the stack.
        """
        node = Node(value)
        self.size += 1

        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
        """
        Pops the top value off the stack.

        Returns
        -------
        any
            The value that was on top of the stack.
        False
            If the stack is empty.
        """
        if self.isEmpty():
            return False
        else:
            self.size -= 1
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
    
    def peek(self):
        """
        Returns the top value of the stack without removing it.

        Returns
        -------
        any
            The value on top of the stack.
        False
            If the stack is empty.
        """
        if self.isEmpty():
            return False
        else:
            return self.top.value
        
    def get_size(self):
        """
        Returns the size of the stack.

        Returns
        -------
        int
            The size of the stack.
        """
        return self.size
    
    def isEmpty(self):
        """
        Checks if the stack is empty.

        Returns
        -------
        bool
            True if the stack is empty, False otherwise.
        """
        return self.top is None
    
    def delete_middle(self):
        """
        Deletes the middle element from the stack.

        If the stack is empty or has only one element, it performs a pop operation.
        """
        if self.isEmpty():
            return None
        
        if self.get_size() == 1:
            return self.pop()
        
        target = self.top
        prev = None
        for i in range(self.size // 2):
            prev = target
            target = target.next
        prev.next = target.next
        target.next = None
        self.size -= 1

    def to_list(self):
        """
        Returns a list of all values in the stack.

        Returns
        -------
        list
            A list containing all values in the stack.
        """
        result = []
        current = self.top
        while current:
            result.append(current.value)
            current = current.next
        return result
