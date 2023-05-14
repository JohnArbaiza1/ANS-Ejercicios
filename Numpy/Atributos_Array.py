import numpy as np

#Existen varios atributos y funciones que describen las características de un array.

#Definiendo el array 
a1 = np.array([1,2,3])
print(a1)
print(type(a1))

#Arreglo de dos dimensiones
arreglo2D = np.array([[1,2,3],[4,5,6]])
print(arreglo2D)

#a.ndim : Devuelve el número de dimensiones del array a
print("\nDimensiones del arreglo: "+str(a1.ndim))
print("\nDimensiones del arreglo: "+str(arreglo2D.ndim)+" Y tiene un numero de filas y columnas de: "+str(arreglo2D.shape))

# a.size : Devuelve el número de elementos del array a
print("\nCantidad de datos: "+str(a1.size))

#Arreglo aleatorio 
#a.shape : Devuelve una tupla con las dimensiones del array a.
arregloAleatorio = np.random.random((5,2))
print("\nUsano la funcion shape")
print("Dimensiones del arreglo 2d -> "+str(arreglo2D.shape))

#Otros ejemplos 
print("\nPosicion 0,1 del vector 2d -> "+str(arreglo2D[0,1]))
arreglo2D[0,1] = 4
print("Posicion 0,1 del vector 2d -> "+str(arreglo2D[0,1]))

respuesta = arreglo2D[(arreglo2D % 2==0)]
print("Arreglo respuesta -> "+str(respuesta))

respuesta2 = arreglo2D[((arreglo2D % 2 ==0) & (arreglo2D > 4))]
print("Respuesta a la segunda condicion -> "+str(respuesta2))

respuestaSuma = arreglo2D + arreglo2D
print(respuestaSuma)
