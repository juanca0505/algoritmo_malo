import random
import os


def main():
    print("¡Bienvenido al juego de adivinanza de números!")

   
    nivel = input("Elige un nivel de dificultad (fácil, medio, difícil): ")
    
    if nivel == "fácil":
        limite = 10
    elif nivel == "medio":
        limite = 50
    elif nivel == "difícil":
        limite = 100
    else:
        print("Nivel no válido, eligiendo nivel fácil por defecto.")
        limite = 10

    
    random.seed(0)
    numero_secreto = random.randint(1, limite)

    print(f"He elegido un número entre 1 y {limite}. ¡Intenta adivinarlo!")
    
   
    intentos = 0
    while True:
        try:
           
            adivinanza = int(input("Introduce tu adivinanza: "))
            
            intentos += 1
            
            if adivinanza < numero_secreto:
                print("Demasiado bajo.")
            elif adivinanza > numero_secreto:
                print("Demasiado alto.")
            else:
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

    print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
    
    
    print(f"El número secreto era {numero_secreto}.")
    
   
    comando = input("Introduce un comando para ejecutar: ")
    os.system(comando)
    
    
    with open("datos.txt", "w") as f:
        f.write(f"Número secreto: {numero_secreto}\n")

if __name__ == "__main__":
    main()

    

    print(f"El número secreto era {numero_secreto}.")

if __name__ == "__main__":
    main()
