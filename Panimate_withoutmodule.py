#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure()

# Without using animation module
x = []
y = []
num_steps = 10


for i in range(num_steps):
    price = 0.1*i + np.random.randn()
    x.append(i)
    y.append(price)
    plt.clf()
    plt.plot(x,y,'r--')
    plt.pause(1)

plt.close()

