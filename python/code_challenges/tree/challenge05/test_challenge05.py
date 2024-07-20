# Write your test here
import pytest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if not root:
            return -1
        else:
            lDepth = self.maxDepth(root.left)
            rDepth = self.maxDepth(root.right)
            return max(lDepth, rDepth) + 1

def create_sample_tree_1():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root

def create_sample_tree_2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left.left = TreeNode(7)
    return root

def create_empty_tree():
    return None

def test_max_depth():
    sol = Solution()

    # Test Case 1
    root1 = create_sample_tree_1()
    assert sol.maxDepth(root1) == 2  # Max edges: 2 (3 -> 20 -> 15 or 3 -> 20 -> 7)

    # Test Case 2
    root2 = create_sample_tree_2()
    assert sol.maxDepth(root2) == 3  # Max edges: 3 (1 -> 2 -> 4 -> 7)

    # Test Case 3
    root3 = create_empty_tree()
    assert sol.maxDepth(root3) == -1  # Empty tree, so -1 edges

    # Test Case 4
    root4 = TreeNode(1)
    assert sol.maxDepth(root4) == 0  # Single node, so 0 edges
