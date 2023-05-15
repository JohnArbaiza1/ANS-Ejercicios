#---------------------------------------------------------------------------------------
#Dado un array de NumPy con n elementos enteros, escribir una función que calcule la media, la mediana y 
#la desviación estándar de los elementos del array.
#---------------------------------------------------------------------------------------

import numpy as np


#Definimos la funcion que se nos pide 
def calculos(valoresN):
    #Calculando los resultados de las operaciones indicadas
    media = np.mean(valoresN)
    mediana = np.median(valoresN)
    desviacionEs = np.std(valoresN)
    #redondeamos el resultado
    redondeado = round(desviacionEs, 2)
    return media, mediana, redondeado

#Funcion encargada de mostrar los resulatdos 
def resultado(media, mediana, desviacionEs):
    print("El resultado de la media es: ",media)
    print("El resultado de la mediana es: ",mediana)
    print("El resultado de la desviacion es: ", desviacionEs)


#definimos nuestro array 
valorresN = np.array([10,40,60,70,80])
#Le pasamos los parametros
media, mediana, desviacionEs = calculos(valorresN)
#Llamamos a la funcion encaragada de mostrar los resultados
resultado(media, mediana, desviacionEs)
