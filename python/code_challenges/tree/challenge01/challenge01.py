# Write here the code challenge solution
from Tree import buildTree,printLevelOrder
from Node import Node

examples = [
    {
        "preorder": [3, 9, 20, 15, 7],
        "inorder": [9, 3, 15, 20, 7]
    },
    {
        "preorder": [-1],
        "inorder": [-1]
    },
    {
        "preorder": [],
        "inorder": []
    },
    {
        "preorder": [1, 2, 3],
        "inorder": [2, 1, 3]
    },
    {
        "preorder": [1, 2, 4, 5, 3, 6, 7],
        "inorder": [4, 2, 5, 1, 6, 3, 7]
    }
]

for i, example in enumerate(examples, 1):
    preorder = example["preorder"]
    inorder = example["inorder"]
    tree = buildTree(preorder[:], inorder[:])  # Use slices to pass a copy
    result = printLevelOrder(tree)
    print(f"Example {i}:")
    print(f"Preorder: {example['preorder']}")
    print(f"Inorder: {example['inorder']}")
    print(f"Output: {result}")
    print()
