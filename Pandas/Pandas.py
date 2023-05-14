#Ejemplos de ejercicios usando la libreria de pandas 

#Haciendo el import de la libreria {
import pandas as pd 

#=============================================================
#Ejemplo 1: Series
 
#Creando la serie a partir de una lista
seriData = pd.Series(['Programacion', 'Fisica', 'Matematicas'], dtype="str")
#Imprimimos la serie
print("\nEjemplo de series a partir de una lista")
print(seriData)

#-----------------------------------------------------------------

#Creando la serie a poartir de un diccionario
print("\nSerie a partir de un diccionario")
serieDiccionario = pd.Series({'Programcion':7.0, 'Fisica':8.2, 'Matematicas':6.7})
print(serieDiccionario)

#------------------------------------------------------------------

#Segunda forma para crear series 
print("\nSegunda forma para crear series")
serie2 = pd.Series([10,9,8], ['Matematicas', 'Economia', 'Programcion'])
print(serie2)

#------------------------------------------------------------------

#Busacndo valores de la serie atraves de las posiciones de los indices
print("\nBuscando valores de las series")
print("El valor de la posicion seleccionada es: ",serieDiccionario[0])

#Buscando el valor de la serie por medio del nombre del indice
print("\nBuscando valores por medio del nombre de los indices")
print("Elvalor obtenido de la busqueda es: ",serie2[ 'Economia'])
print()
print("*" * 40)

#==========================================================================

#RESUMEN DESCRIPTIVO DE UNA SERIE

#count() : Devuelve el número de elementos que no son nulos ni NaN en la serie s.
print("Resultado de la funcion count es: "+ str(seriData.count()))
print("*" * 40)
#------------------------------------------------------------------

#sum() : Devuelve la suma de los datos de la serie s cuando los datos son de un tipo numérico, o la
#concatenación de ellos cuando son del tipo cadena str
print("Suma de valores de la serie: ",serie2.sum())
print("*" * 40)
#------------------------------------------------------------------

#cumsum() : Devuelve una serie con la suma acumulada de los datos de la serie s cuando los datos 
# son de un tipo numérico.
print("Usando la funcion cumsum:\n",serie2.cumsum())
print("*" * 40)
#------------------------------------------------------------------

#value_counts() : Devuelve una serie con la frecuencia (número de repeticiones) de cada valor de la serie s.
print("Usando la funcion value_counts")
print(serie2.value_counts())
print("*" * 40)
#------------------------------------------------------------------

#min() : Devuelve el menor de los datos de la serie s
print("Uso de la funcion min")
print(serieDiccionario.min())
print("*" * 40)
#------------------------------------------------------------------

# max() : Devuelve el mayor de los datos de la serie s
print("Uso de la funcion max")
print(serieDiccionario.max())
print("*" * 40)
#------------------------------------------------------------------

# mean() : Devuelve la media de los datos de la serie s cuando los datos son de un tipo numérico
print("Uso de la funcion mean")
print(serie2.mean())
print("*" * 40)
#------------------------------------------------------------------

#Creamos una nueva serie
serieNumerica = pd.Series([1,2,3,4,5,], dtype=int)

#var() : Devuelve la varianza de los datos de la serie s cuando los datos son de un tipo numérico
print("uso de la funcion var")
print(serieNumerica.var())
print("*" * 40)
#------------------------------------------------------------------

#std() : Devuelve la desviación típica de los datos de la serie s cuando los datos son de un tipo numérico
print("Uso de la funion std")
print(serieNumerica.std())
print("*" * 40)
#------------------------------------------------------------------
print("Uso de la funcion describe")
#describe(): Devuelve una serie con un resumen descriptivo que incluye el número de datos, su suma,
#  el mínimo, el máximo, la media, la desviación típica y los cuartiles.
print(serie2.describe())
