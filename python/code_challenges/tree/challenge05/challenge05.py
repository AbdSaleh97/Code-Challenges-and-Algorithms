
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Initializes a new instance of the TreeNode class.

        Parameters:
            val (int): The value of the current node (default is 0).
            left (TreeNode): The left child node (default is None).
            right (TreeNode): The right child node (default is None).
        """
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        """
        Calculates the maximum depth of a binary tree starting from the root node.

        Parameters:
            root (TreeNode): The root node of the binary tree.

        Returns:
            int: The maximum depth of the binary tree.
        """
        if not root:
            return -1
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1
    

def create_sample_tree():
    # Example Tree:
    #       3
    #      / \
    #     9  20
    #        / \
    #       15  7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root

if __name__ == "__main__":
    sol = Solution()
    root = create_sample_tree()
    print(f"Maximum number of edges: {sol.maxDepth(root)}")