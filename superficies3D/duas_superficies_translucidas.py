import numpy   as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

def f():
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z1 = np.sin(np.sqrt(x**2 + y**2))
    z2 = np.cos(np.sqrt(x**2 + y**2))

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z2, color='red', alpha=0.5, edgecolor='none')
    ax.plot_surface(x, y, z1, color='blue', alpha=0.5, edgecolor='none')

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title('Superficie Translucida')

    plt.show()



f()