from Node import Node

class BinaryTree:
    def __init__(self):

        self.root = None

    def insert(self, value):

        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_rec(self.root, value)

    def insert_rec(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert_rec(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert_rec(node.right, value)

    def InOrden_rec(self, node):
        if node is not None:
            self.InOrden_rec(node.left)
            print(node.value, end=" ")
            self.InOrden_rec(node.right)
    def InOrden(self):
        self.InOrden_rec(self.root)
        print("")

    def PostOrden_rec(self, node):
        if node is not None:
            self.PostOrden_rec(node.left) 
            self.PostOrden_rec(node.right)  
            print(node.value, end=" ")  

    def PostOrden(self):
        self.PostOrden_rec(self.root)
        print("")

    def PreOrden_rec(self,node):
        if node is not None:
            print(node.value, end=" ")
            self.PreOrden_rec(node.left)
            self.PreOrden_rec(node.right)
    
    def PreOrden(self):
        self.PreOrden_rec(self.root)
        print("")
    #
    #SE ESCOGIO EL PREORDEN PARA HACER EL PUNTO
    def Merge(self, other):
        if isinstance(other, BinaryTree):
            self._merge_trees(self.root, other.root)
        else:
            print("Cannot merge")

    def _merge_trees(self, node1, node2):
        if node2 is None:
            return
        self.insert(node2.value)

        self._merge_trees(node1, node2.left)
        self._merge_trees(node1, node2.right)


   
