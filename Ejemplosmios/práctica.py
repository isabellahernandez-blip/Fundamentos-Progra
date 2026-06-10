nombre = input("cuál es tu nombre? ")
cantidad1 = int(input("escoge el primer número que quieras sumar: "))
cantidad2 = int(input("escoge el segundo número que quieras sumar: "))
suma = cantidad1 + cantidad2
print("Hola", nombre, "La suma de", cantidad1, "y", cantidad2, "es", suma)

cantidad3 = int(input("escoge el primer número que quieras multiplicar: "))
cantidad4 = int(input("escoge el segundo número que quieras multiplicar: "))
multiplicacion = cantidad3 * cantidad4
print("Hola,", nombre, "! La multiplicación de", cantidad3, "y", cantidad4, "es", multiplicacion, ".")

cantidad5 = int(input("escoge el primer número que quieras dividir con enteros: "))
cantidad6 = int(input("escoge el segundo número que quieras dividir con enteros: "))
division = cantidad5 // cantidad6
print("Hola,", nombre, "! La división entera de", cantidad5, "entre", cantidad6, "es", division, ".")

print (type(cantidad1), type(cantidad2), type(suma)
       )