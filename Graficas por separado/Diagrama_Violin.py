import matplotlib.pyplot as plt

#violinplot(x): Dibuja un diagrama de violín con los datos de la lista x
fig , ax =plt.subplots()
ax.violinplot([1,2,3,4,5,6,7])
plt.show()