from challenge01 import TreeNode, Solution

import pytest
# Write your test here
def create_sample_tree_1():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    return root

def create_sample_tree_2():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(3)
    root.left.left = TreeNode(-2)
    root.left.right = TreeNode(-1)
    root.right.left = TreeNode(2)
    return root

def create_sample_tree_3():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)
    return root

def create_sample_tree_4():
    root = TreeNode(1)
    root.left = TreeNode(1)
    return root

def create_empty_tree():
    return None

@pytest.mark.parametrize("tree_func, k, expected", [
    (create_sample_tree_1, 9, True),  # Nodes 2 and 7 sum up to 9
    (create_sample_tree_1, 28, False),  # No such pair exists
    (create_empty_tree, 1, False),  # Empty tree, no pairs
    (create_sample_tree_4, 2, True),  # Nodes 1 and 1 sum up to 2
    (create_sample_tree_2, -1, True),  # Nodes 0 and -1 sum up to -1
    (create_sample_tree_3, 25, True),  # Nodes 10 and 15 sum up to 25
    (create_sample_tree_3, 35, False),  # No such pair exists
    (create_sample_tree_2, 2, True),  # Nodes -1 and 3 sum up to 2
    (create_sample_tree_2, 4, True),  # Nodes 1 and 3 sum up to 4
    (create_sample_tree_3, 3, False),  # No such pair exists
    (create_sample_tree_1, 11, True),  # Nodes 5 and 6 sum up to 11
])
def test_find_target(tree_func, k, expected):
    sol = Solution()
    root = tree_func()
    assert sol.findTarget(root, k) == expected