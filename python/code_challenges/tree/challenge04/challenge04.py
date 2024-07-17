# Write here the code challenge solution
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

# Example usage:
tree_elements = [8, 3, 10,45, 1, 6, 14]
root_node = build_tree_level_order(tree_elements, None, 0, len(tree_elements))
print(f"Tree elements: {tree_elements}")
largest_value = find_largest_value(root_node)
print(f"The largest value in the tree is: {largest_value}")
