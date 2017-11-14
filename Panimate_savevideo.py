#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure()

x = []
y = []
num_steps = 10

# Initialize writer for saving video
FFMpegWriter = animation.writers['ffmpeg']
metadata = dict(title='Mode evolution', artist='Srikanth')
writer = FFMpegWriter(fps=1, metadata=metadata)

with writer.saving(fig, "price_movement.mp4", 200):
    for i in range(num_steps):
        price = 0.1*i + np.random.randn()
        x.append(i)
        y.append(price)
        plt.clf()
        plt.plot(x,y,'r--')
        writer.grab_frame()
        plt.pause(1)

plt.close()

