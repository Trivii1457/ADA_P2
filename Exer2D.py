from Queue import Queue
class queueCafe:
    def __init__(self):
        self.Workers = Queue();
        self.Students = Queue();


    def proces_event(self,event):
        try:
            part = event.split()
            event_type = part[0]
             # a es el evento para agregar estudiantes
            if event_type == 'a':
                self.Students.enqueue(part[1])
            # w es el evento para agregar trabajadores
            elif event_type == 'w':
                self.Workers.enqueue(part[1])
            elif event_type == 'aw':
                while not self.Workers.is_empty() or not self.Students.is_empty():
                    if  self.Workers.is_empty( ):
                        if self.Students.is_empty():
                            print("The queue is empty")
                        else:
                            next_persn = self.Students.dequeue()
                            print(f"Atendiendo a {next_persn}")
                    else:
                        next_persn = self.Workers.dequeue()
                        print(f"Atendiendo a {next_persn}")
        except Exception as e:
            print(f"Oh, an error has happened: {e}")
        






