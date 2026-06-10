import random

usuario = input("Ingrese piedra, papel o tijera: ")
maquina = random.choice(["piedra", "papel", "tijera"])
print("La máquina eligió:", maquina)

if usuario == maquina:
    print("Empate! Ambos eligieron", usuario)
elif (usuario == "piedra" and maquina == "tijera") or(usuario == "papel" and maquina == "piedra") or (usuario == "tijera" and maquina == "papel"):
    print("Ganaste! Elegiste", usuario, "y la máquina eligió", maquina)
else:
    print("Perdiste! Elegiste", usuario, "y la máquina eligió", maquina)
