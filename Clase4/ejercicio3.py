print("... comprador: hola, me gustaría saber que tipo de descuento tengo en esta tienda")
print("...  vnededor: claro, para eso necesito saber que tipo de cliente eres, por favor ingresa tu tipo de cliente")

tipo_cliente = input("ingresa tu tipo de cliente (regular, estudiante, VIP u otro): ")
monto_compra = float(input("ingresa el monto de tu compra: "))

if tipo_cliente == "regular": print(" Tu descento es de 5%, y el monto total a pagar es:", monto_compra*0.95) 
elif tipo_cliente == "estudiante": print(" Tu descento es de 15%, y el monto total a pagar es:", monto_compra*0.85)
elif tipo_cliente == "VIP": print(" Tu descento es de 20%, y el monto total a pagar es:", monto_compra*0.80)
else: print("el monto total a pagar es:", monto_compra)
