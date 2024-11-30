from Exer2D import queueCafe
def main():
    cafeto = queueCafe()

    eventos = [
        "w Maria","a Juan", "w elias","aw"   #aw es el evento para empezar a atendender  
    ]
    
    for evento in eventos:
        cafeto.proces_event(evento)

if __name__ == "__main__":
    main()