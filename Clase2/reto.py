print("bienvenido al reto de los números, adivina el número secreto...")

numero_secreto = 89
numero_usuario = int(input("ingresa el número que crees que es el secreto:"))
if numero_usuario == numero_secreto:
    print("EXELENTE!, adivinaste")
elif numero_usuario > numero_secreto: print("Probá otra vez, el número secreto es mayor que el que ingresaste")
else: print("Probá otra vez, el número secreto es menor que el que ingresaste")
    