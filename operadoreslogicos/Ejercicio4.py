# Ejercicio 2
# Obtener el precio final que se tiene que pagar si se aplica el 36% del total de la compra.

import math

precio=float(input("Total compra en €: "))

dto = float(36 / 100)

precio_final = precio - ( precio * (dto) ) 

print(f"El precio con un 36% de descuento es: {precio_final:.2f} €")