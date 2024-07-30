# Write here the code challenge solution

class ListNode:
    """
    A node in a singly linked list used for handling collisions in the hash table.

    Attributes:
        key: The key of the node.
        value: The value associated with the key.
        next: The reference to the next node in the linked list.
    """
    def __init__(self, key, value):
        """
        Initialize a new ListNode.

        Args:
            key: The key of the node.
            value: The value associated with the key.
        """
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    """
    A simple hash table implementation with collision handling using chaining (linked lists).

    Attributes:
        size: The size of the hash table.
        table: The list to store the hash table elements.
    """
    def __init__(self, size=100):
        """
        Initialize a new HashTable.

        Args:
            size: The size of the hash table. Default is 100.
        """
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        """
        Compute the hash value of a key.

        Args:
            key: The key to hash.

        Returns:
            The hash value of the key.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.

        Args:
            key: The key to insert.
            value: The value associated with the key.
        """
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [key, value]
        else:
            # Collision detected, use chaining
            if isinstance(self.table[index], list):
                # Convert the array to a linked list
                existing_key, existing_value = self.table[index]
                self.table[index] = ListNode(existing_key, existing_value)
                self.table[index].next = ListNode(key, value)
            else:
                current = self.table[index]
                while current.next:
                    current = current.next
                current.next = ListNode(key, value)

    def search(self, key):
        """
        Search for a value by key in the hash table.

        Args:
            key: The key to search for.

        Returns:
            The value associated with the key if found, else None.
        """
        index = self._hash(key)
        if self.table[index] is None:
            return None
        elif isinstance(self.table[index], list):
            if self.table[index][0] == key:
                return self.table[index][1]
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    return current.value
                current = current.next
        return None

    def delete(self, key):
        """
        Delete a key-value pair from the hash table.

        Args:
            key: The key to delete.

        Returns:
            True if the key was found and deleted, else False.
        """
        index = self._hash(key)
        if self.table[index] is None:
            return False
        elif isinstance(self.table[index], list):
            if self.table[index][0] == key:
                self.table[index] = None
                return True
        else:
            current = self.table[index]
            prev = None
            while current:
                if current.key == key:
                    if prev:
                        prev.next = current.next
                    else:
                        self.table[index] = current.next
                    return True
                prev = current
                current = current.next
        return False

def array_intersection(arr1, arr2):
    """
    Find the intersection of two arrays using a hash table.

    Args:
        arr1: The first array.
        arr2: The second array.

    Returns:
        A list of unique elements that are present in both arrays.
    """
    # Create a hash table
    hash_table = HashTable()

    # Insert elements of the first array into the hash table
    for num in arr1:
        if hash_table.search(num) is None:
            hash_table.insert(num, True)

    # Find intersection by checking elements of the second array in the hash table
    result = []
    for num in arr2:
        if hash_table.search(num) is not None:
            result.append(num)
            hash_table.delete(num)  # Ensure each element in the result is unique

    return result

arr1 = [1, 2, 2, 1]
arr2 = [2,1]
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Intersection:", array_intersection(arr1, arr2))
