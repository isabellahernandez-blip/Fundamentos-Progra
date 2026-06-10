temperatura = float(input("Pofa, ingresa la Temperatura en grados Celsius: "))
if temperatura > 30 and temperatura <= 45:
    print("Hace calor, tomá agua")
elif temperatura >= 15 and temperatura <= 30:
    print("Clima es agradable")
elif temperatura < 15:
    print("Hace frío, abrigate")
else:
    print("Temperatura no válida")

print("temperatura registrada")
