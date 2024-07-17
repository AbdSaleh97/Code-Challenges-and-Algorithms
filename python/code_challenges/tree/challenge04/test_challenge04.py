import pytest

class BinaryTreeNode:
    def __init__(self, data=0, left_node=None, right_node=None):
        """Initialize a node in a binary tree with data and optional left and right children."""
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def find_largest_value(root_node):
    """Find the largest value in the binary tree using inorder traversal."""
    def inorder(node):
        """Perform inorder traversal to update the largest value found."""
        if node is None:
            return
        inorder(node.left_node)
        nonlocal largest_value
        if node.data > largest_value:
            largest_value = node.data
        inorder(node.right_node)
    
    if root_node is None:
        return None
    
    largest_value = float('-inf')
    inorder(root_node)
    return largest_value

def build_tree_level_order(elements, root_node, index, size):
    """Insert nodes into the binary tree in level order."""
    if index < size:
        temp_node = BinaryTreeNode(elements[index])
        root_node = temp_node

        # Insert left child
        root_node.left_node = build_tree_level_order(elements, root_node.left_node, 2 * index + 1, size)

        # Insert right child
        root_node.right_node = build_tree_level_order(elements, root_node.right_node, 2 * index + 2, size)
    
    return root_node

# Pytest test cases
def test_find_largest_value():
    elements = [8, 3, 10, 1, 6, 14]
    root_node = build_tree_level_order(elements, None, 0, len(elements))
    assert find_largest_value(root_node) == 14

def test_find_largest_value_single_node():
    elements = [42]
    root_node = build_tree_level_order(elements, None, 0, len(elements))
    assert find_largest_value(root_node) == 42

def test_find_largest_value_empty_tree():
    assert find_largest_value(None) is None

def test_find_largest_value_negative_numbers():
    elements = [-10, -20, -5, -30, -15, -7]
    root_node = build_tree_level_order(elements, None, 0, len(elements))
    assert find_largest_value(root_node) == -5

def test_find_largest_value_mixed_numbers():
    elements = [10, -20, 15, -30, 25, -7, 100]
    root_node = build_tree_level_order(elements, None, 0, len(elements))
    assert find_largest_value(root_node) == 100

if __name__ == "__main__":
    pytest.main()
