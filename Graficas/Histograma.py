import numpy as np #Para el histograma se requiere importar el modulo de la libreria de numpy
import matplotlib.pyplot as plt

#hist(x, bins): Dibuja un histograma con las frecuencias resultantes de agrupar los datos
#de la lista x en las clases definidas por la lista bins.
fig, grafica = plt.subplots()
x = np.random.normal(5,1.5, size=1000)
grafica.hist(x, np.arange(0,11))
plt.show()