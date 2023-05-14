import pandas as pd

#Series a usar para este segundo ejemplo
serData = pd.Series([1,2,3,6,7],['carros', 'motos', 'buses', 'mesas', 'tiendas'])
diccionario = pd.Series({'libros':20, 'Cuadernos':50, 'Borradores':10})

#=======================================================================================
#ATRIBUTOS DE UNA SERIE

#size : Devuelve el número de elementos de la serie
print("Uso de la funcion size")
print(serData.size)
print("*" *40)
#------------------------------------------------------------------
#OPERACIONES EN UNA SERIE

#Los operadores binarios (+, *, /, etc.) pueden utilizarse con una
#serie, y devuelven otra serie con el resultado de aplicar la
#operación a cada elemento de la serie.

#Suma 
print("Suma")
print(serData + 2)
print("*" *40)
#------------------------------------------------------------------

#Multiplicacion
print("Multiplicacion")
print(diccionario * 3)
print("*" *40)
#------------------------------------------------------------------

#Uso del operador %
print("Uso del operador %")
print(serData % 2)
print("*" *40)
#------------------------------------------------------------------

#FILTRAR UNA SERIE
print("FILTRAR UNA SERIE")
print(serData[serData > 3])
print("\n",serData <6 )
print("*" *40)
#------------------------------------------------------------------

#ORDENAR UNA SERIE

print("Ordenados segun el valor")
#sort_values(ascending=booleano) : Devuelve la serie que resulta de ordenar los valores la serie s. Si
#argumento del parámetro ascending es True el orden es creciente y si es False decreciente
print("Datos ordenados de menor a mayor")
print(serData.sort_values(ascending=True))
print("\nDatos ordenados de mayor a menor")
print(serData.sort_values(ascending=False))
print("*" *40)
#------------------------------------------------------------------

print("Ordenados segun el indice")
print("Datos ordenados de menor a mayor")
print(diccionario.sort_index(ascending=True))
print("\nDatos ordenados de mayor a menor")
print(diccionario.sort_index(ascending=False))