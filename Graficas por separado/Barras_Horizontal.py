# Hacemos el import del modulo
import matplotlib.pyplot as plt

#Barras horizontales
#barh(x, y): Dibuja un diagrama de barras horizontales donde x es una lista con la posición
#de las barras en el eje Y, e y es una lista con la longitud de las barras en el eje X.
ig, grafica = plt.subplots()
grafica.barh([1,2,3],[3,2,1])
plt.show()