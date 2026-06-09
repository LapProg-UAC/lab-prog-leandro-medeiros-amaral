import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

def f():
    # Setup data
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    r = np.sqrt(x**2 + y**2)
    
    z1 = np.sin(r)
    z2 = np.cos(r)
    z3 = np.sin(r+np.pi/4)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(x, y, z1, cmap='autumn', alpha=0.6, edgecolor='none', antialiased=True, shade=True)
    ax.plot_surface(x, y, z2, cmap='winter', alpha=0.6, edgecolor='none', antialiased=True, shade=True)
    ax.plot_surface(x, y, z3, cmap='BuPu', alpha=0.6, edgecolor='none', antialiased=True, shade=True)  

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title('Superficie Translucida')

    plt.savefig('superficie_translucida.png', dpi=300)

    plt.show()

f()