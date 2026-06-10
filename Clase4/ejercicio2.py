print("... llega un alumno con su maestro de mate")
print("...alumno: hola profesor, cómo está?")
print("...profe: bien gracias, en qué te puedo ayudar ?")
print("...alumno: necesito saber que tipo de triángulo es el que tengo ")

lado_1 = int(input("ingresa el valor del lado 1: "))
lado_2 = int(input("ingresa el valor del lado 2: "))
lado_3 = int(input("ingresa el valor del lado 3: "))

if lado_1 == lado_2 and lado_2 == lado_3: print("hola el triángulo es equilátero")
elif lado_1 == lado_2 or lado_2 == lado_3 or lado_1 == lado_3: print("hola el triángulo es isósceles")
else: print("hola el triángulo es escaleno")
