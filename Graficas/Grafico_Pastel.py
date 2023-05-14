import matplotlib.pyplot as plt

#pie(x): Dibuja un diagrama de sectores con las frecuencias de la lista x.
fig , ax =plt.subplots()
ax.pie([10,34,67,12])
plt.show()