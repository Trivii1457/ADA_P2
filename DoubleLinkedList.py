class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
   
    def __init__(self):
        self.head = None

    def InsertList(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    

    def InsertAtStart(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    

    def InsertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def InsertAfter(self, prev_node, data):
        if prev_node is None:
            return "El nodo anterior no está en la lista"
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node
    
    def InsertBefore(self, next_node, data):
        if next_node is None:
            return "El nodo siguiente no está en la lista"
        new_node = Node(data)
        new_node.prev = next_node.prev
        next_node.prev = new_node
        new_node.next = next_node
        if new_node.prev is not None:
            new_node.prev.next = new_node

    def Search(self, data):
        Current_node = self.head
        while Current_node:
            if Current_node.data == data:
                return True
            Current_node = Current_node.next
        return False
    
    def ListaVacia(self):
        if self.head is None:
            return True
        else:
            return False
        
    def DeleteFromStart(self):
        if self.head is None:
            return "La lista está vacía"
        self.head = self.head.next
        self.head.prev = None

    def DeleteFromEnd(self):
        if self.head is None:
            return "La lista está vacía"
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.prev.next = None

    def CountNodes(self):
        count = 0
        Current_node = self.head
        while Current_node:
            count += 1
            Current_node = Current_node.next
        return count
    
    def DeleteNode(self, data):
        if self.head is None:
            return "La lista está vacía"
        if self.head.data == data:       
            self.head = self.head.next
            self.head.prev = None
            return
        Current_node = self.head
        while Current_node.next:
            if Current_node.next.data == data:
                Current_node.next = Current_node.next.next
                if Current_node.next is not None:
                    Current_node.next.prev = Current_node
                return
            Current_node = Current_node.next

    def InvertList(self):
        prev = None
        Current_node = self.head
        while Current_node:
            next_node = Current_node.next
            Current_node.next = prev
            Current_node.prev = next_node
            prev = Current_node
            Current_node = next_node
        self.head = prev

    def Succesor(self, data):
        Current = self.head
        while Current:
            if Current.data == data:
                if Current.next is not None:
                    return Current.next.data
                else:
                    return "No hay sucesor para el nodo dado"
            Current = Current.next
        return "El nodo con el dato proporcionado no se encuentra en la lista"
    
    def Predeccesor(self, data):
        Current = self.head
        while Current:
            if Current.data == data:
                if Current.prev is not None:
                    return Current.prev.data
                else:
                    return "No hay predecesor para el nodo dado"
            Current = Current.next
        return "El nodo con el dato proporcionado no se encuentra en la lista"
    
    def PrintList(self):
        Current_node = self.head
        while Current_node:
            print(Current_node.data, end=' <-> ')
            Current_node = Current_node.next
        print(None)
    

#Pueba
llist = DoubleLinkedList()
llist.InsertList(1)
llist.InsertList(2)
llist.InsertList(3)
llist.InsertList(4)
llist.InsertList(5)
llist.InsertList(6)
print(llist.CountNodes())
llist.InsertAtStart(0)
llist.InsertAtEnd(7)
print(llist.Predeccesor(2))
print(llist.Succesor(2))
llist.DeleteFromStart()
print(llist.CountNodes())
print(llist.PrintList())