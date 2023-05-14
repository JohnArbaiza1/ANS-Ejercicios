import pandas as pd

#----------------------------------------------------------------------------------
#Un objeto del tipo DataFrame define un conjunto de datos estructurado en forma de tabla donde cada columna
#es un objeto de tipo Series, es decir, todos los datos de una misma columna son del mismo tipo, y las filas son
#registros que pueden contender datos de distintos tipos.

#Un DataFrame contiene dos índices, uno para las filas y otro para las columnas, y se puede acceder a sus
#elementos mediante los nombres de las filas y las columnas
#----------------------------------------------------------------------------------

#Creación de un DataFrame a partir de un diccionario de listas:
print("\nDataFrame a partie de un diccionario de listas")
dataFrame = {'Nombre': ['Maria', 'Pedro', 'Miguel'],
             'Edad' : [12,16,18],
             'Grado' : ['Economia', 'Medicina', 'Arquitectura'],
            'Correo': ['juan@gmail.com', 'maria@gmail.com', 'pedro@gmail.com']}

df = pd.DataFrame(dataFrame)
print(df)
print("=" * 50)
#----------------------------------------------------------------------------------

#CREACIÓN DE UN DATAFRAME A PARTIR DE UNA LISTA DE LISTAS
print("DataFrame a partir de una lista de listas")
dFrameList = pd.DataFrame([['Nohely', 20], ['Raquel', 18], ['Carmen', 25]],columns=['Nombre', 'Edad'])
print(dFrameList)
print("=" * 50)
#----------------------------------------------------------------------------------

#CREACIÓN DE UN DATAFRAME A PARTIR DE UNA LISTA DE DICCIONARIOS
print("DataFrame a partir de una lista de diccionarios ")
dataFList = pd.DataFrame([{'Nombre': 'Maria', 'Edad':20}, {'Nombre':'Pedro', 'Edad':23},
                          {'Nombre':'Julieta', 'Edad':20}])
print(dataFList)
print("=" * 50)
#----------------------------------------------------------------------------------

#CREACIÓN DE UN DATAFRAME A PARTIR DE UN ARRAY
print("DataFrame a partir de un array")
import numpy as np
data2 = pd.DataFrame(np.random.randn(4,3), columns=['a', 'b', 'c'])
print(data2)
print("=" * 50)
#----------------------------------------------------------------------------------

#DataFrame usando un archivo de Excel
#para cerarlo debemos poner el nombre del archivo y luego el nombre de la hoja y el decimal
#Se debe espeficicar la ruta en caso de trabajr en diferentes carpetas
datos = pd.read_excel('.\Pandas\Datos.xlsx', sheet_name='Hoja1', decimal='.')
print(datos)
print("=" * 50)
print("Otros datos del archivo")
print("=" * 50)
print(datos.shape) #Cantidad de filas y columnas
print("=" * 50)
print(datos.size) #Nuemro de elementos
print("=" * 50)
print(datos.columns) #Nombre de las columnas
print("=" * 50)
print(datos.dtypes)
print("=" * 50)
print("-"*9," Primeros registros","-"*9)
print(datos.head(3)) #Mostrando los primeros registros
print("=" * 50)
print("-"*9," Ultimos registros","-"*9)
print(datos.tail(2))#Mostrando los ultimos registros
print("=" * 50)
#Cambiando el nombre de las columnas 
print(datos.rename(columns={'Nombre': 'nombre', 'Edad': 'edad', 'Nota': 'nota', 'Fecha': 'fecha'}))
print("=" * 50)
#----------------------------------------------------------------------------------

#Forma 1
print("Nombre -->" + str(datos.iloc[3, 0])+ "Nota -->"+ str(datos.iloc[3,2]))
print()
#Forma 2
print(datos.loc[3, 'Nota'])
print("=" * 50)
#----------------------------------------------------------------------------------

#Creando un archivo para excel
#Para esto se necesita la libreria de numpy la cual anteriormente ya fue importada 
data2 = pd.DataFrame(np.random.rand(4,4), columns=['a', 'b', 'c','d'])
print(data2)
#Creano el archivo
#data2.to_excel('./Pandas/Numeros_Aleatorio.xlsx', sheet_name='DatosNumericos')
