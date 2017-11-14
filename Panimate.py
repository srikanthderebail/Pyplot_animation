#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Using the animation module
fig = plt.figure()
x = []
y = []
def animate(t,x,y):
    price = 0.1*t + np.random.randn()
    x.append(t)
    y.append(price)
    plt.clf()
    plt.plot(x,y,'r--')

ani=animation.FuncAnimation(fig,animate,frames=np.linspace(0,0.1,10),fargs=(x,y),interval=1000,repeat=False)
plt.show()
plt.close()



