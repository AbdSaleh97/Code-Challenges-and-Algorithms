from collections import deque
from Node import Node

def buildTree(preorder, inorder):
    """
    Construct a binary tree from preorder and inorder traversal lists.

    Args:
    preorder (list): The preorder traversal of the binary tree.
    inorder (list): The inorder traversal of the binary tree.

    Returns:
    Node: The root node of the constructed binary tree.
    """
    if not inorder or not preorder:
        return None
    
    root = Node(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = buildTree(preorder[1: mid+1], inorder[:mid])
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:])
    
    return root

def printLevelOrder(root):
    """
    Perform a level-order traversal (breadth-first traversal) of the binary tree.

    Args:
    root (Node): The root node of the binary tree.

    Returns:
    list: A list representing the level-order traversal of the tree, with `None` for missing nodes.
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result
