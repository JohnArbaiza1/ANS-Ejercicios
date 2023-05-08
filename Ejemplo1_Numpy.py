#Hacemos el import del modulo de numpy
import numpy as np

#? el signo (*) a la par de cada comentario es de una extension de VS Code que da color a los 
#? a los comentarios de igual manera se pueden usar otros singons para dar color como el (? y el !)

#*Creando un array apartir de listas 
numPrimos = np.array([2,3,5,7,11,13,17,19,23,29,31])
print(numPrimos)

#*Creando un array de dos dimensiones{
dimensiones = np.array([[1,2,3],[4,5,6]])
print("\nArray de dos dimensiones")
print(dimensiones)

#*Creando array con ceros 
array_Zeros = np.zeros(10)
print("\nArray con ceros")
print(array_Zeros)

#*Array con ceros 2D
array_Zeros = np.zeros((5,5))
print("\nArray con ceros 2D")
print(array_Zeros)

#*Array usando la funcion empty la cual crea  y devuelve una referencia a un array vacío con las dimensiones especificadas en la
#*tupla dimensiones.
Arreglo1 = np.empty((3))
print("\nArreglo usando empty")
print(Arreglo1)

# *Crea y devuelve una referencia a un array con las dimensiones especificadas en la tupla
# *dimensiones cuyos elementos son todos unos
arreglo_One = np.ones((4,4))
print("\nArreglo usando ones")
print(arreglo_One)

#* np.full Crea y devuelve una referencia a un array con las dimensiones especificadas en 
#* la tupla dimensiones cuyos elementos son todos valor.
arreglo_Full = np.full((4,4),(100))
print("\nArreglo usando full")
print(arreglo_Full)

#* np.identity Crea y devuelve una referencia a la matriz identidad de dimensión n.
arreglo_Identidad = np.identity(4)
print("\nArreglo con identity")
print(arreglo_Identidad)

#* np.arange Crea y devuelve una referencia a un array de una dimensión cuyos elementos son 
#* la secuencia desde inicio hasta fin tomando valores cada salto
arreglo_Rango = np.arange(0,100,2) #* Establecemos que ira de dos en dos 
print("\nArreglo usando arange")
print("\n", arreglo_Rango)

#* np.linspace Crea y devuelve una referencia a un array de una dimensión cuyos elementos 
#* son la secuencia de n valores equidistantes desde inicio hasta fin.
arregloXdistantes = np.linspace(1,10,2)
print("\n Arreglo con linspace")
print("\n",arregloXdistantes)

#* np.random Crea y devuelve una referencia a un array con las dimensiones especificadas en
#* la tupla dimensiones cuyos elementos son aleatorios.
arreglo_Aleatorio = np.random.random((5,2))
print("\n Arreglo usando random")
print("\n",arreglo_Aleatorio)