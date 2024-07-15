# Write your test here
import pytest
from challenge03 import TreeNode, Solution  # assuming your solution is in solution.py

def tree_equals(t1, t2):
    if not t1 and not t2:
        return True
    if t1 and t2:
        return (t1.val == t2.val and
                tree_equals(t1.left, t2.left) and
                tree_equals(t1.right, t2.right))
    return False

@pytest.mark.parametrize("nums, expected_tree", [
    ([-10, -3, 0, 5, 9], TreeNode(0, TreeNode(-3, TreeNode(-10), None), TreeNode(9, TreeNode(5), None))),
    ([1, 3], TreeNode(3, TreeNode(1), None))
])
def test_sortedArrayToBST(nums, expected_tree):
    sol = Solution()
    result_tree = sol.sortedArrayToBST(nums)
    assert tree_equals(result_tree, expected_tree)
