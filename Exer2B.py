from LinkedList import LinkedList as LList
from DoubleLinkedList import DoubleLinkedList as DLList
import os


def main():
    
    DoubleLL = DLList()
    SingleLL = LList()

    SingleLL.InsertList(1)
    SingleLL.InsertList(2)
    SingleLL.InsertList(3)
    SingleLL.InsertList(4)
    SingleLL.InsertList(5)
    SingleLL.InsertList(6)
    SingleLL.InsertList(7)
    SingleLL.InsertList(8)


    DoubleLL.InsertList(10)
    DoubleLL.InsertList(20)
    DoubleLL.InsertList(30)
    DoubleLL.InsertList(40)
    DoubleLL.InsertList(50)
    DoubleLL.InsertList(60)
    DoubleLL.InsertList(70)
    DoubleLL.InsertList(80)
    
    
    
    print("Single Linked List")
    SingleLL.print_list()
    print("\nDouble Linked List")
    DoubleLL.PrintList()

    #Insertando al inicio y al final de ambas listas
    SingleLL.InsertAtStart(0)
    SingleLL.InsertAtEnd(9)
    DoubleLL.InsertAtStart(0)
    DoubleLL.InsertAtEnd(90)
    print("\nInsertando al inicio y al final de ambas listas")
    print("Single Linked List")
    SingleLL.print_list()
    print("\nDouble Linked List")
    DoubleLL.PrintList()

    #Eliminando al inicio y al final de ambas listas
    SingleLL.DeleteFromStart()
    SingleLL.DeleteFromEnd()
    DoubleLL.DeleteFromStart()
    DoubleLL.DeleteFromEnd()
    print("\nEliminando al inicio y al final de ambas listas")
    print("Single Linked List")
    SingleLL.print_list()
    print("\nDouble Linked List")
    DoubleLL.PrintList()

    #Reemplazando antes y después de un nodo en ambas listas
    SingleLL.Replace_After(4, 100)
    SingleLL.Replace_Before(5, 200)
    DoubleLL.Replace_After(60, 100)
    DoubleLL.Replace_Before(40, 200)
    print("\nReemplazando antes y despues de un nodo en ambas listas")
    print("Single Linked List")
    SingleLL.print_list()
    print("\nDouble Linked List")
    DoubleLL.PrintList()

    #Moviendo un nodo en ambas listas
    SingleLL.Move(100, 300)
    DoubleLL.Move(100, 300)
    print("\nMoviendo un nodo en ambas listas")
    print("Single Linked List")
    SingleLL.print_list()
    print("\nDouble Linked List")
    DoubleLL.PrintList()
    

if __name__ == "__main__":
    main()