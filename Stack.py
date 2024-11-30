class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    #Devuelve el último elemento de la lista
    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
    
    def const(self):
        if self.items != []:
            a = self.items.pop()
            b = self.items.pop()
            c = a+b
            self.items.append(c)
            return self.items
    
    """
    def mov(self,n):
        a = 0
        selff = []
        for i in range(1,n):
            a += self.items.pop()

        for i in range(len(self.items)-1, -1, -1):
            selff.append(self.items.pop())

        self.items = selff
        return self.items
    """
    def mov(self, n):
        if n > len(self.items):
            print("n es mayor que el número de elementos en la pila")
        
        elemento = []
        a = 0
        for i in range(n):
            a += self.items.pop()
        elemento.append(a)

        
        Restantes = self.items[::-1]
        self.items = Restantes

        return [elemento,self.items[::-1]]
    
    def imp(self):
        return print(self.items)
    
            
    
        