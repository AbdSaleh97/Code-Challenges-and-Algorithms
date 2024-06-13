from Node import Node

class Queue:
    """
    A class used to represent a Queue.

    Attributes
    ----------
    front : Node
        The front node of the queue.
    rear : Node
        The rear node of the queue.
    size : int
        The size of the queue.

    Methods
    -------
    push(value):
        Adds a value to the rear of the queue.
    pop():
        Removes and returns the value from the front of the queue.
    peek():
        Returns the value from the front of the queue without removing it.
    empty():
        Checks if the queue is empty.
    get_size():
        Returns the size of the queue.
    reverse_queue():
        Reverses the elements in the queue.
    print_linked_list():
        Prints the values of nodes in the queue from rear to front.
    """
    
    def __init__(self):
        """Initializes the queue with no elements."""
        self.front = None
        self.rear = None
        self.size = 0

    def push(self, value):
        """
        Adds a value to the rear of the queue.

        Parameters
        ----------
        value : any
            The value to be added to the queue.
        """
        node = Node(value)
        if self.size == 0:
            self.front = node
            self.rear = node
        else:
            node.next = self.rear
            self.rear = node
        self.size += 1

    def pop(self):
        """
        Removes and returns the value from the front of the queue.

        Returns
        -------
        any
            The value that was at the front of the queue.
        False
            If the queue is empty.
        """
        if self.size <= 0:
            return False
        elif self.size == 1:
            temp = self.front
            self.front = None
            self.rear = None
            self.size -= 1
            return temp.value
        else:
            temp = self.front
            node = self.rear
            while node.next:
                if node.next == temp:
                    self.front = node
                    self.size -= 1
                    node.next = None
                    return temp.value
                node = node.next

    def peek(self):
        """
        Returns the value from the front of the queue without removing it.

        Returns
        -------
        any
            The value at the front of the queue.
        """
        return self.front.value

    def empty(self):
        """
        Checks if the queue is empty.

        Returns
        -------
        bool
            True if the queue is empty, False otherwise.
        """
        return self.size == 0
    
    def get_size(self):
        """
        Returns the size of the queue.

        Returns
        -------
        int
            The size of the queue.
        """
        return self.size
    
    def reverse_queue(self):
        """
        Reverses the elements in the queue.

        This function reverses the order of elements in the queue. It does this by iterating through the queue from the rear to the front, updating the next pointers of each node to point to the previous node. The front of the queue becomes the rear of the reversed queue, and the rear of the queue becomes the front of the reversed queue.

        Returns
        -------
        None
            If the queue is empty or has only one element, the function returns None.
        """
        if self.empty():
            return
        
        if self.get_size() == 1:
            return

        prev = self.rear
        current = self.rear.next
        prev.next = None

        while current != self.front:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        if current == self.front:
            current.next = prev
            self.front = self.rear
            self.rear = current

    def print_linked_list(self):
        """
        Prints the values of nodes in the LinkedList starting from the rear node.

        The values are printed in the format: value -> value -> ... -> Rear -> Front.
        """
        arr = ["Rear"]
        current = self.rear
        while current:
            arr.append(str(current.value))  # Append the value as a string
            current = current.next
        arr.append("Front")  # Append "Front" at the end
        return " -> ".join(arr)  # Join elements with " -> "

# Example usage
q = Queue()

q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)

print(q.print_linked_list())
q.reverse_queue()
print(q.print_linked_list())
