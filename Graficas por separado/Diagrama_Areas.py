import matplotlib.pyplot as plt

# fill_between(x, y): Dibuja el area bajo el polígono con los vértices dados por las
# coordenadas de la lista x en el eje X y las coordenadas de la lista y en el eje Y
fig, grafica = plt.subplots()
grafica.fill_between([1,2,3,4,5],[1,2,0,0,5], color='yellow')
plt.show()