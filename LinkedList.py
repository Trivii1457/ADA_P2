class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #Inserta al final de la lista
    def InsertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    #Inserta al inicio de la lista
    def InsertAtStart(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    #Enseña la lista de arriba hacía abajo
    def print_list(self):
        Current_node = self.head
        while Current_node:
            print(Current_node.data)
            Current_node = Current_node.next


    def DeleteFromStart(self):
        if self.head is None:
            return "La lista está vacía"
        self.head = self.head.next

    def DeleteFromEnd(self):
        if self.head is None:
            return "La lista está vacía"
        last_node = self.head
        #Mientras el penúltimo nodo no sea None
        #El último nodo será el penúltimo nodo
        while last_node.next.next:
            last_node = last_node.next
        last_node.next = None   

    def DeleteNode(self, data):
        if self.head is None:
            return "La lista está vacía"
        if self.head.data == data:
            self.head = self.head.next
            return
        Current_node = self.head
        while Current_node.next:
            if Current_node.next.data == data:
                Current_node.next = Current_node.next.next
                return
            Current_node = Current_node.next


    def Search(self, data):
        if self.head is None:
            return "La lista está vacía"
        Current_node = self.head
        while Current_node:
            if Current_node.data == data:
                return "El dato se encuentra en la lista"
            Current_node = Current_node.next
        return "El dato no se encuentra en la lista"