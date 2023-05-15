#Ejercicio haciendo uso de pandas 

import pandas as pd

print()
print("=" * 20,end="")
print("| BIENVENIDO |",end="")
print("=" * 20)

#Definiendo las listas a usar
nombres = []
edad = []

datos = int(input("\nIngrese el numero de datos que desea ingresar:"))

print()
for i in range(datos):
    nom = input("•Ingrese un nombre:\n")
    Edades = int(input("•Ingrese la edad:\n"))
    nombres.append(nom)
    edad.append(Edades)

#Ahrora creamos el dataFrame que en este caso sera del tipo diccionario de listas
dataFrame ={'Nombre': nombres, 'Edad': edad}
df = pd.DataFrame(dataFrame)
print(df)

#Mandamos los datos a un archivo de Excel
dataFrame

df.to_excel('./Ejercicios/Datos.xlsx', sheet_name='Datos')


