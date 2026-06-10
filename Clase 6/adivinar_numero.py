import random 
print("¡Bienvenido al juego de adivinar el número!")

maquina = random.randint(1,5)
usuario = int(input("Adivina el número del 1 al 5, ingresa el que crees que es el correcto: "))

if usuario == maquina: 
    print("Que pilas, adivinaste el número secreto")
elif usuario > maquina:
    print("proba otra vez, el número es menor al que ingresaste")
else:
    print("proba otra vez, el número es mayor al que ingresaste")

print("El número secreto era:", maquina)
