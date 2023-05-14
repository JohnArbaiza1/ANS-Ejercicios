import matplotlib.pyplot as plt

#boxplot(x): Dibuja un diagrama de caja y bigotes con los datos de la lista x.
fig, ax = plt.subplots()
ax.boxplot([1,2,3,4,5,6,7])
plt.show()