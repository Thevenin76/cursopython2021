#Bucle While
import math

numero=0

while numero<20:
    print (f"{numero}")
    numero+=1

print("Fin del programa")

numero=int(input("Ingresar un numero: "))

while numero<0:
    print("Ingrese nº positivo")
    numero=int(input("Vuelva a ingresar un numero: "))

print(f"El resultado de la raiz cuadrada es: {math.sqrt(numero):.2f}")