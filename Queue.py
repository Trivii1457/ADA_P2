class Queue:

    def __init__(self):
        self.items = []
        
    def is_empty(self):
            if self.items == []:
                return True
            else:
                return "Tiene Elementos" 

    def enqueue(self, item):
        self.items.append(item) 

    def dequeue(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[0]
    
    def LastElement(self):
        return self.items[-1]
    