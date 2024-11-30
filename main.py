from binary_tree import BinaryTree

if __name__ == "__main__":
    tree = BinaryTree()
    tree2 = BinaryTree()
    complete = BinaryTree()

    tree.insert(50)
    tree.insert(30)
    tree.insert(70)
    tree.insert(20)
    tree.insert(40)
    tree.insert(60)
    tree.insert(80)

    tree2.insert(1)
    tree2.insert(2)
    tree2.insert(3)


    tree.InOrden() 
    tree.PostOrden()
    tree.PreOrden()
    tree.Merge(tree2)
    tree.InOrden()
    tree.PostOrden() 