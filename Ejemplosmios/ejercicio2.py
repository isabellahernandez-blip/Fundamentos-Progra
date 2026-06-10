# ejercicio en parejas con Giron
# usar condicionales y operadores logicos

nombre = input("¿nombre?: ")
edad = int(input("¿edad?: "))

print("Responda la siguiente pregunta con 1 para sí y 0 para no")
boleto = int(input("¿tiene boleto?: "))

if edad >= 18 and boleto == 1:
    print("Hola", nombre, "puede entrar")
else:
    print("Hola", nombre, "NO puede entrar")


