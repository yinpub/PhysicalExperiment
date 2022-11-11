import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

wavelength=2  
#波长

T=20
#周期

def f(x,y):
    #单波
    return np.e**((2*np.pi/wavelength)*np.sqrt(y**2+(x)**2)* 1j)

x= np.linspace(-5,5, 200)

y= np.linspace(-5,5, 200)



def g(i):   #时间因子         
    return np.e**((-2*np.pi/T)*i*1j)


fig=plt.figure()

ax=Axes3D(fig)
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
ax.set_zlim(-5,5)
X, Y = np.meshgrid(x, y)
t=0
F=(g(t)*f(X,Y)).real
#ax.contour(X,Y,Z)  #等高线图
line=ax.plot_surface(X,Y,F)

def animate(t):
    F=(g(t)*f(X,Y)).real
    plt.cla()
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-5, 5)
    line=ax.plot_surface(X,Y,F)
    return line

ani=FuncAnimation(fig=fig,func=animate,frames=300,interval=0.1,blit=False)

plt.show()