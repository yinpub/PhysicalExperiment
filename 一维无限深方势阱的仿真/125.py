class Particle:
    def __init__(self,x,y,a):
        self.x=x
        self.y=y
        self.a=a

import numpy as np
import matplotlib.pyplot as plt
import random
import math
class ParticleSimulator:
    

    
    def __init__(self,particles):
       self.particles=particles
    def evolve(self,dt):
        timestep = 0.01
        nsteps = int(dt/timestep)
        

        for i in range(nsteps):
            for p in self.particles:
                ####       
                 for h in range(100):
                     
                   
                    u=random.uniform(0, p.a)#随机生成x坐标
                    print(u)
                    v=random.uniform(0, 2/p.a)  #随机生成y坐标
                    print(v)
                    w=(2/p.a)*(math.sin((math.pi/p.a)*u)**2)#方
                    if v<w:
                        break
                 
                 #完成位置的更新
            
                 '''u=random.uniform(1,3)#随机生成x坐标
                 print(u)'''
                 print(u)
                 p.x=u
            


            
#########

from matplotlib import pyplot as plt
from matplotlib import animation

def visualize(simulator):

    X=[p.x for p in simulator.particles]
    Y=[p.y for p in simulator.particles]

    fig=plt.figure()
    ax=plt.subplot()
    line,=ax.plot(X,Y,'ro')

    plt.xlim(-10,10)
    plt.ylim(-5,5)

    def init():
        line.set_data([],[])
        return line,

    def animate(i):
        simulator.evolve(0.01)
        X=[p.x for p in simulator.particles]
        Y=[p.y for p in simulator.particles]

        line.set_data(X,Y)
        return line,
    #每隔 毫秒调用一次动画函数
    anim=animation.FuncAnimation(fig,animate,init_func=init,blit=True,interval=100)

    plt.axvline(8)
    plt.axvline(0)
    plt.show()

def test_visualize():
    particles=[Particle(0.5,0.5,8)]


    simulator =ParticleSimulator(particles)
    visualize(simulator)

test_visualize()
