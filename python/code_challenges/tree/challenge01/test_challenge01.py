# Write your test here
from Tree import buildTree,printLevelOrder
def test_buildTree():
    # Test case 1
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    tree = buildTree(preorder[:], inorder[:])
    assert printLevelOrder(tree) == [3, 9, 20, None, None, 15, 7]

    # Test case 2
    preorder = [-1]
    inorder = [-1]
    tree = buildTree(preorder[:], inorder[:])
    assert printLevelOrder(tree) == [-1]

    # Test case 3
    preorder = []
    inorder = []
    tree = buildTree(preorder[:], inorder[:])
    assert printLevelOrder(tree) == []

    # Test case 4
    preorder = [1, 2, 3]
    inorder = [2, 1, 3]
    tree = buildTree(preorder[:], inorder[:])
    assert printLevelOrder(tree) == [1, 2, 3]

    # Test case 5
    preorder = [1, 2, 4, 5, 3, 6, 7]
    inorder = [4, 2, 5, 1, 6, 3, 7]
    tree = buildTree(preorder[:], inorder[:])
    assert printLevelOrder(tree) == [1, 2, 3, 4, 5, 6, 7]