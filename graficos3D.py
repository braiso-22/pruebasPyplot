import numpy as np
import matplotlib.pyplot as plt

# Mostrar un subplot con una linea en 3D
figura, ejes = plt.subplots(figsize=(8, 4), subplot_kw={'projection': '3d'}) 
x = np.arange(7)
y = x[::-1]
z = x*y
ejes.plot3D(x, y, z)
ejes.scatter3D(x, y, z, c=z, cmap='Greens')
plt.show()

# Mostrar un subplot con una superficie en 3D
figura1, ejes1 = plt.subplots(1,3,figsize=(8, 4), subplot_kw={'projection': '3d'}) 
x1 = np.arange(0,5,1)
y1 = np.arange(5,10,1)
x1, y1 = np.meshgrid(x1,y1)
z1 = np.sin(
    np.sqrt(x1**2 + y1**2)
)
grafica = ejes1[0].plot_surface(x1,y1,z1)

x1 = np.arange(-5,5,0.25)
y1 = x1[:]
x1, y1 = np.meshgrid(x1,y1)

#print(x,"\n\n",y)
z1 = np.sin(
    np.sqrt(x1**2 + y1**2)
)
grafica = ejes1[1].plot_surface(x1,y1,z1)
grafica1 = ejes1[2].plot_wireframe(x1,y1,z1)
plt.show()




