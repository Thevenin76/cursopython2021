# Ejercicio 2
# Obtener el radio y longitud de un circulo en Python

# a = PI * r2
# longitud = 2 * PI * r

import math

radio=float(input("radio: "))

area = math.pi * radio**2
longitud = 2 * math.pi * radio 

print(f"El área es: {area:.1f}")
print(f"La longitud es: {longitud:.1f}")