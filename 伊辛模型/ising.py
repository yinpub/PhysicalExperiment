from __future__ import division
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
from matplotlib import animation

def initialstate(N):   
    ''' generates a random spin configuration for initial condition'''
    state = 2*np.random.randint(2, size=(N,N))-1
    return state

def mcmove(config, beta):
    '''Monte Carlo move using Metropolis algorithm '''
    for i in range(N):
        for j in range(N):
                a = np.random.randint(0, N)
                b = np.random.randint(0, N)
                s =  config[a, b]
                nb = config[(a+1)%N,b] + config[a,(b+1)%N] + config[(a-1)%N,b] + config[a,(b-1)%N]
                cost = 2*s*nb
                if cost < 0:
                    s *= -1
                elif rand() < np.exp(-cost*beta):
                    s *= -1
                config[a, b] = s
    return config

nt      = 256         # 温度点数量
N       = 4**2        # 点阵尺寸, N x N  
eqSteps = 2**10       # MC方法平衡步数

tm = 2.269;    T=np.random.normal(tm, .64, nt)          #设2.269为临界点
T  = T[(T>1.2) & (T<3.8)];   #筛选出在温度范围内的温度点
nt = np.size(T)             #计算出剩余温度点数量
print(nt)
Tindex=3;#修改这个参数，进而选择你要实验的温度。
iT=1.0/T[Tindex]; 

#iT=1.0/2.269  #当处于相变点附近时

f ,ax= plt.subplots(); # plot the calculated values 

img=[]
configs=[]

config = initialstate(N)
img.append([ax.imshow(config)])


for i in range(eqSteps):         # equilibrate
    mcmove(config, iT)           # Monte Carlo moves
    img.append([ax.imshow(config)])

print('begin play')

ani = animation.ArtistAnimation(f, img, interval=20, blit=True,repeat_delay=0,repeat=False)    
plt.show()