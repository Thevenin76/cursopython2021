#Introducciíon a listas
array=["futbol", "PC", 18.6,18,[6,7,10.4], True, False]

print(array)

print(array[2])

print(array[-3])

print(array[0:3])

#Hasta el final
print(array[2:3])

#averiguar elementos del array
print(len(array))

#añadir dato
array.append(66)
print(array)

#insertar
array.insert(1,90)
print(array)

#extender
array.extend(["D100", "DA01000"])
print(array)

#concaternar
array2=[200,250,"hola"]
array3=array+array2
print(array3)

#Buscar en array
print("PC" in array)

#Encontrar
print(array.index("PC"))

#Contar
print(array.count("PC"))

#Eliminar datos
array.remove("PC")
print(array)

#Eliminar datos
array.remove(18)
print(array)



array.reverse()
print(array)

array5=[18.6,18,4,5]
array5.sort()
print(array5)

#Limpiar array
array.clear()