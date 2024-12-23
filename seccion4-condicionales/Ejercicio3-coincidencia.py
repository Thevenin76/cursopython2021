# Condicionales if
# Crear un programa que pida 2  nombressi comienzan con la misma letra o son iguales

nombre1 = (input("Ingrese nombre: "))
nombre2 = (input("Ingrese otro nombre: "))

if nombre1[0] == nombre2[0] or nombre1[-1]==nombre2[-1]:
    print("Hay coincidencia")
else: 
    print("No Hay coincidencia")
