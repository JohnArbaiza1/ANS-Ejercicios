#-------------------------------------------------------------------------------
# Dibuja un gráfico de barras para comparar la cantidad de ventas mensuales de dos 
# tiendas diferentes en un período de un año, utilizando Matplotlib
#-------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import random # hacemos uso de la biblioteca de randomn para sacar las cantidades 
import numpy as np # tambien usaremos la biblioteca de numpy

#Definiendo las listas y variable a emplear
storeOne = []
storeTwo = []
#Nos devolvera una referncia cuyos elementos son secuencia desde inicio hasta fin
meses = np.arange(1,13) 

#Ciclos for para sacar las cantidades 
for i in range(12):
     aleatorio = random.randint(1,201)
     storeOne.append(aleatorio)

for j in range(12):
    aleatorio2 = random.randint(1,201)
    storeTwo.append(aleatorio2)

#Mosttando las cantidades 
print("\nVentas de la tienda 1")
print("=" * 50)
print(storeOne)
print("=" * 50)
print("\nVentas de la tienda 2")
print("=" * 50)
print(storeTwo)
print("=" * 50)

#Haciendo las comparaciones por medio de las graficas 
fig, ax = plt.subplots()
#Dibujando las barras 
ancho = 0.35
ax.bar(meses - ancho/2, storeOne, ancho, label='Tienda 1')
ax.bar(meses + ancho/2, storeTwo, ancho, label='Tienda 2')

# Configurar etiquetas de eje x y título
ax.set_xticks(meses)
ax.set_xticklabels(['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
ax.set_xlabel('Mes')
ax.set_ylabel('Ventas (miles de dólares)')
ax.set_title('Comparación de ventas mensuales')

# Agregar leyenda
ax.legend()

#Mostrando el grafico
plt.show()
