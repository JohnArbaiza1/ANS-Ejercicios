#-------------------------------------------------------------------------------------------
#Escribir una función que reciba un diccionario con las notas de las asignaturas de un curso y una cadena con el
#nombre de un color y devuelva un diagrama de barras de las notas en el color dado.
#-------------------------------------------------------------------------------------------

#Hacemos el import 
import matplotlib.pyplot as plt

#Definimos nuestro diccionario 
notas = {'Matematica':6, 'Lenguaje':7, 'Ciencias':10}

fig, grafica = plt.subplots()
grafica.bar(notas.keys(), notas.values(), color='aqua')
plt.show()

