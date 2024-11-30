from Stack import Stack 

def main():
    print("Ejercicio 2A" + "\n"+ "Caso prueba con pila 4,7,21,12,2,1")

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(12)
    stack.push(21)
    stack.push(7)
    stack.push(4)
    print(f"{stack.items} valores sin funcion const, se lee de derecha a izquierda")
    print(f"{stack.const()} valores con funcion const, se lee de derecha a izquierda")
    print(f"{stack.mov(2)} funcion mov, se lee de izquierda a derecha con n = 2")
    print(stack.items)
    stack.imp()
    



if __name__ == "__main__":
    main()



