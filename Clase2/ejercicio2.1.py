nombre = input("nombre?") #pedimos al usuario que ingrese su nombre y lo guardamos en la variable nombre
edad = int(input("edad?")) #pedimos al usuario que ingrese su edad, la convertimos a entero y la guardamos en la variable edad

print("responda la siguiente pregunta con 1 para si y 0 para no") #instrucciones para el usuario

boleto = int(input("tiene boleto?"))  #preguntamos al usuario si tiene boleto, convertimos su respuesta a entero y la guardamos en la variable boleto
puede_entrar = edad>= 18 and boleto ==1  #evaluamos si el usuario tiene 18 años o más y si tiene boleto, el resultado se guarda en la variable puede_entrar

print("hola", nombre, ",puede entrar?", puede_entrar) #comprobamos si el usuario puede entrar o no, mostrando su nombre y el resultado de la evaluación en la variable puede_entrar