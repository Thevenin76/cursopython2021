# Ejercicio 4
saldo=2000

print("1. Ingreso de dinero")
print("2. Retiro de dinero")
print("3. Mostrar de dinero")
print("4. Salir")

seleccion=int(input("Elija una opción: " ))

if seleccion==1:
    ingreso=float(input("Dinero a Ingresar: "))
    saldo+=ingreso
    print(f"Nuevo saldo en la cuenta {saldo}" )
elif seleccion==2:
    salida=float(input("Dinero de salida: "))
    if salida>saldo:
        print("No tiene saldo suficiente")
    else:
        saldo-=salida
        print(f"Nuevo saldo disponible: {saldo}")
elif seleccion==3:
    print(f"Saldo: {saldo}")
elif seleccion==4:
    print("Operación Terminada")        
