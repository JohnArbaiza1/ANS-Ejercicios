import matplotlib.pyplot as plt

#  scatter(x, y): Dibuja un diagrama de puntos con las coordenadas de la
# lista x en el eje X y las coordenadas de la lista y en el eje Y
fig, grafica = plt.subplots()
grafica.scatter([1,2,3,4],[1,2,0,0])
plt.show()