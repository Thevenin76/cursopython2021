# Condicionales if
# Crear un programa que pida 2 números y obtenga como resultado cual de ellos es Par o si ambos lo son

dato = int (input("Ingrese número: "))
dato2 = int (input("Ingrese otro número: "))

if dato %2 ==0 and dato2%2 == 0:
    print("Ambos son Pares")
elif dato %2 !=0 or dato2%2 != 0:
    if dato%2 == 0:
        print(f"{dato} es par")
    elif dato2%2 == 0:
        print(f"{dato2} es par")
    else: 
        print("Ambos son Impares")

print ("Fin del programa")