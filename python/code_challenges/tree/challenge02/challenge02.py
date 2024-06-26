from Tree import Tree

def main():
    t = Tree()
    t.insert(1)
    t.insert(2)
    t.insert(3)
    
    t2 = Tree()
    t2.insert(1)
    t2.insert(3)
    t2.insert(3)
    
    print(t.same_tree(t.root, t2.root))

if __name__ == "__main__":
    main()
