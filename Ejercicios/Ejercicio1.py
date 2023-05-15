#--------------------------------------------------------------------------------------------
#Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre 
#por pantalla un diagrama de líneas con la evolución de las ventas.
#--------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt

print("="*15," BIENVENIDO ","="*15)
print()
print(" "*11, "Informacion de ventas \n")

#Creamos una lista vacia
Ventas = []
nYears = []

#Definimos una variable que nos ayudara a poder ingresar los datos
ingresos  = 0
years = int(input("Ingrese el rango de años a verificar:"))

print()
#Ciclo for que nos ayudara para ingresar los datos
for v in range(years):
    ingresos = int(input("Ingrese las ganacias de las ventas:"))
    Ventas.append(ingresos)

#por medio de este for almacenamos el numero de años en otra lista que nos servira mas adelante
#Caundo queramos mostrar la grafica 
for y in range(years):
    datos = nYears.append( y + 1)

#Mostrando los datos de ventas 
print(Ventas)
#mostrando el diagrama

#Forma 1: por medio de dos listas
fig, grafica = plt.subplots()
plt.title(f"Ventas de un periodo de {years} años")
grafica.plot(nYears,Ventas)
plt.show()

#Forma 2: Usando una unica lista 
'''plt.plot(Ventas)
plt.grid()
plt.title(f"Ventas de un periodo de {years} años")
plt.show()'''


