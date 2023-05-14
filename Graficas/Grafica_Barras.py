# Hacemos el import del modulo
import matplotlib.pyplot as plt

#Diagramas de barras
#bar(x, y): Dibuja un diagrama de barras verticales donde x es una lista con la posición
#de las barras en el eje X, e y es una lista con la altura de las barras en el eje Y
ig,grafica = plt.subplots()
grafica.bar([1,2,3],[3,2,1])
plt.show()