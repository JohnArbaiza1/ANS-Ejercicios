import numpy as np #Es necesario hacer el import de numpy
import matplotlib.pyplot as plt

#contourf(x, y, z): Dibuja un diagrama de contorno con las curvas de nivel de la superficie dada por los
#puntos con las coordenadas de las listas x, y y z en los ejes X, Y y Z respectivamente
fig, grafica= plt.subplots()
x =np.linspace(-3.0,3.0,100)
y=np.linspace(-3.0,3.0,100)
x,y=np.meshgrid(x,y)
z=np.sqrt(x**2 + 2*y**2)
grafica.contourf(x,y,z)
plt.show()