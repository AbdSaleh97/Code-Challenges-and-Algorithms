class ListNode:
    """Node class for the linked list used in separate chaining."""
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class HashTable:
    """Hash table implementation using separate chaining for collision resolution."""
    def __init__(self, size=10):
        # Initialize the hash table with a fixed size
        self.size = size
        self.buckets = [None] * self.size

    def _hash(self, key):
        # Hash function to map keys to bucket indices
        return hash(key) % self.size

    def insert(self, key, value):
        # Insert a key-value pair into the hash table
        index = self._hash(key)
        if self.buckets[index] is None:
            # Create a new linked list node if the bucket is empty
            self.buckets[index] = ListNode(key, value)
        else:
            # Traverse the linked list and update the value if the key exists
            current = self.buckets[index]
            while current is not None:
                if current.key == key:
                    current.value = value  # Update the value if the key is found
                    return
                if current.next is None:
                    break
                current = current.next
            # Append a new node at the end of the list if the key does not exist
            current.next = ListNode(key, value)

    def get(self, key):
        # Retrieve a value by its key from the hash table
        index = self._hash(key)
        current = self.buckets[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None  # Return None if the key is not found

    def remove(self, key):
        # Remove a key-value pair from the hash table
        index = self._hash(key)
        current = self.buckets[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.buckets[index] = current.next  # Remove the node if it's the head
                else:
                    prev.next = current.next  # Bypass the node to remove it
                return
            prev = current
            current = current.next

    def __str__(self):
        # String representation of the hash table
        result = []
        for i, node in enumerate(self.buckets):
            if node is not None:
                chain = []
                current = node
                while current:
                    chain.append(f"{current.key}: {current.value}")
                    current = current.next
                result.append(f"Bucket {i}: " + " -> ".join(chain))
            else:
                result.append(f"Bucket {i}: None")
        return "\n".join(result)

def sort_people(names, heights):
    """
    Sorts a list of names based on their corresponding heights in descending order.

    Parameters:
        names (List[str]): A list of names.
        heights (List[int]): A list of heights corresponding to the names.

    Returns:
        List[str]: A list of names sorted in descending order of their heights.

    Example:
        >>> names = ["Alice", "Bob", "Dave"]
        >>> heights = [155, 185, 150]
        >>> sort_people(names, heights)
        ['Bob', 'Alice', 'Dave']
    """
    # Initialize hash table
    hash_table = HashTable()

    # Insert names with corresponding heights into the hash table
    for name, height in zip(names, heights):
        hash_table.insert(height, name)

    # Sort the heights in descending order
    sorted_heights = sorted(heights, reverse=True)

    # Retrieve names in descending order of heights using the hash table
    sorted_names = [hash_table.get(height) for height in sorted_heights]

    return sorted_names

# Example usage
if __name__ == "__main__":
    names = ["Alice", "Bob", "Dave"]
    heights = [155, 185, 150]
    sorted_names = sort_people(names, heights)
    print(sorted_names)  # Output: ["Bob", "Alice", "Bob"]
    
    # Print the hash table
    # print("\nHash Table:")
    # print(hash_table)
