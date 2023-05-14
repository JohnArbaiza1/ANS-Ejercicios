# Hacemos el import del modulo
import matplotlib.pyplot as plt

# Matplotlib es una librería de Python especializada en la creación de gráficos en dos dimensiones.
# Esta Permite crear y personalizar los tipos de gráficos más comunes, entre ellos:

#Ejemplos 

#DIAGRAMAS DE DISPERSIÓN O PUNTOS
'''fig, grafica = plt.subplots()
grafica.scatter([1,2,3,4,],[1,2,0,0,])
plt.show()'''

#DIAGRAMAS DE LÍNEAS
'''fig, ax = plt.subplots()
ax.plot([1,2,3,4,5],[1,2,0,0,5], color='yellow')
plt.show()'''

#DIAGRAMAS DE AREAS
'''fig, grafica = plt.subplots()
grafica.fill_between([1,2,3,4,5],[1,2,0,0,5], color='yellow')
plt.show()'''

#Diagramas de barras
'''fig,grafica = plt.subplots()
grafica.bar([1,2,3],[3,2,1])
plt.show()'''

#Barras horizontales
'''fig, grafica = plt.subplots()
grafica.barh([1,2,3],[3,2,1])
plt.show()'''

#Histograma
import numpy as np
'''fig, grafica = plt.subplots()
x = np.random.normal(5,1.5, size=1000)
grafica.hist(x, np.arange(0,11))
plt.show()'''

#DIAGRAMAS DE SECTORES o pastel
'''fig , ax =plt.subplots()
ax.pie([10,34,67,12])
plt.show()'''

#DIAGRAMAS DE CAJA Y BIGOTES
'''fig, ax = plt.subplots()
ax.boxplot([1,2,3,4,5,6,7])
plt.show()'''

#DIAGRAMAS DE VIOLÍN
'''fig , ax =plt.subplots()
ax.violinplot([1,2,3,4,5,6,7])
plt.show()'''

#DIAGRAMAS DE CONTORNO
fig, grafica= plt.subplots()
x =np.linspace(-3.0,3.0,100)
y=np.linspace(-3.0,3.0,100)
x,y=np.meshgrid(x,y)
z=np.sqrt(x**2 + 2*y**2)
grafica.contourf(x,y,z)
plt.show()





