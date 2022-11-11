
class Particle:
    def __init__(self,x,y,v):
        self.x=x
        self.y=y
        self.v=v



class ParticleSimulator:
    def __init__(self,particles):
       self.particles=particles
    def evolve(self,dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)

        for i in range(nsteps):
            for p in self.particles:
                #计算位移矢量d_x####
                d_x=timestep*p.v
                #计算速度更新量(假设k/m=1）
                d_v=timestep*20*p.x#这里的常数是k，T=2*pi(m/k)**0.5,可得k越大T越小
               
                #更新位置坐标#####
                p.x +=d_x
                p.v -=d_v
              
               

from matplotlib import pyplot as plt
from matplotlib import animation

def visualize(simulator):

    X=[p.x for p in simulator.particles]
    Y=[p.y for p in simulator.particles]

    fig=plt.figure()
    ax=plt.subplot(111,aspect='equal')
    line,=ax.plot(X,Y,'ro')

    plt.xlim(-10,10)
    plt.ylim(-10,10)

    def init():
        line.set_data([],[])
        return line,

    def animate(i):
        simulator.evolve(0.01)
        X=[p.x for p in simulator.particles]
        Y=[p.y for p in simulator.particles]

        line.set_data(X,Y)
        return line,

    anim=animation.FuncAnimation(fig,animate,init_func=init,blit=True,interval=5)
    plt.show()

def test_visualize():
    particles=[Particle(3,5,10)]

    simulator =ParticleSimulator(particles)
    visualize(simulator)

test_visualize()
