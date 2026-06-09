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
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(x, y, z1, cmap='plasma', alpha=0.6, edgecolor='none', antialiased=True, shade=True)
    ax.contour(x, y, z1, zdir='z',cmap='plasma', offset=0.0, levels=50, linewidths=1.5, antialiased=True)
   

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title('Superficie Translucida')

    plt.savefig('superficie_translucida.png', dpi=300)

    plt.show()

f()