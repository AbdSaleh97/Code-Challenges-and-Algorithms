class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root,k: int):
        table = set()
        def sum(node):
            if node is None: return False
            y = k - node.val
            if y in table:
                return True
            table.add(node.val)
            return sum(node.left) or sum(node.right)
        return sum(root)


def create_sample_tree():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    return root

if __name__ == "__main__":
    sol = Solution()
    root = create_sample_tree()
    k = 5
    print(f"Find target {k}: {sol.findTarget(root, k)}")