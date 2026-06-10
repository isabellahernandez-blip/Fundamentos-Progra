#sistema de acceso para una persona que si tiene + de 18 puede ingresar, si tiene entre 15 y 17 puede entrar con un adulto y si es - a 15 no puede entrar
# si es mayor de 18 años, puede inbresae 
nombre = input("cómo te llamas? ") #esto es una variable con un input para que el usuario ingrese su nombre
edad = int(input("Ingresa porfa tu edad: ")) #esto es una variable con un int input para que el usuario ingrese su edad

if edad >= 18: #esto es una condicional if para verificar si la edad es mayor o igual a 18
    print("Hola :)", nombre +",", "puedes ingresar, al establecimiento") #si la condición es verdadera, se imprime este mensaje
elif edad >= 15 and edad < 18: #esto es una condicional elif para verificar si la persona puede ingresar con un adulto 
    print("Hola :)", nombre + ",", "podes entrar al establecimiento pero acompañado de un adulto") #si la condición es verdadera, se imprime este mensaje
else: #esto es una condicional else para verificar si la persona no puede ingresar
    print("Hola :)", nombre + ",", "lo lamento mucho :(), no puedes ingresar al establecimiento") #si la condición es falsa, se imprime este mensaje

