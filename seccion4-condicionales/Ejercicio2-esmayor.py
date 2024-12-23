# Condicionales if
# Crear un programa que pida 3 números y obtenga como resultado cual de ellos es mayor

dato1 = int (input("Ingrese número: "))
dato2 = int (input("Ingrese otro número: "))
dato3 = int (input("Ingrese número: "))

if dato1 >=dato2 and dato1>=dato3:
    print(f"Dato 1 es mayor {dato1}")
elif dato2>=dato1 and dato2>=dato3:
    print(f"Dato 2 es mayor {dato2}")
elif dato3>=dato1 and dato3>=dato2:
    print(f"Dato 3 es mayor {dato3}")

print ("Fin del programa")