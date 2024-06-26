# Write your test here
import pytest
from Tree import Tree

@pytest.fixture
def setup_trees():
    tree1 = Tree()
    tree2 = Tree()
    return tree1, tree2

def test_same_tree_empty(setup_trees):
    tree1, tree2 = setup_trees
    assert tree1.same_tree(None, None) == True

def test_same_tree_different_structure(setup_trees):
    tree1, tree2 = setup_trees
    tree1.insert(1)
    tree1.insert(2)
    
    tree2.insert(1)
    tree2.insert(3)
    
    assert tree1.same_tree(tree1.root, tree2.root) == False

def test_same_tree_identical_trees(setup_trees):
    tree1, tree2 = setup_trees
    tree1.insert(1)
    tree1.insert(2)
    tree1.insert(3)
    
    tree2.insert(1)
    tree2.insert(2)
    tree2.insert(3)
    
    assert tree1.same_tree(tree1.root, tree2.root) == True

def test_same_tree_empty(setup_trees):
    tree1, tree2 = setup_trees
    assert tree1.same_tree(None, None) == True

def test_same_tree_single_node(setup_trees):
    tree1, tree2 = setup_trees
    tree1.insert(1)
    assert tree1.same_tree(tree1.root, tree1.root) == True

def test_same_tree_different_structure(setup_trees):
    tree1, tree2 = setup_trees
    tree1.insert(1)
    tree1.insert(2)
    
    tree2.insert(1)
    tree2.insert(3)
    
    assert tree1.same_tree(tree1.root, tree2.root) == False

def test_same_tree_identical_trees(setup_trees):
    tree1, tree2 = setup_trees
    tree1.insert(1)
    tree1.insert(2)
    tree1.insert(3)
    
    tree2.insert(1)
    tree2.insert(2)
    tree2.insert(3)
    
    assert tree1.same_tree(tree1.root, tree2.root) == True

def test_same_tree_complex_trees(setup_trees):
    tree1, tree2 = setup_trees
    # Tree 1:      1
    #            /   \
    #           2     3
    #          / \   / \
    #         4   5 6   7
    tree1.insert(1)
    tree1.insert(2)
    tree1.insert(3)
    tree1.insert(4)
    tree1.insert(5)
    tree1.insert(6)
    tree1.insert(7)
    
    # Tree 2:      1
    #            /   \
    #           2     3
    #          / \   /
    #         4   5 6
    tree2.insert(1)
    tree2.insert(2)
    tree2.insert(3)
    tree2.insert(4)
    tree2.insert(5)
    tree2.insert(6)
    
    assert tree1.same_tree(tree1.root, tree2.root) == False