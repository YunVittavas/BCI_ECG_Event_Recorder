from scipy.io import wavfile
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
import os

os.chdir('/media/pi/DEVICE_07/')

fs, x = wavfile.read('TEST0011.wav')
n = len(x)
time = np.linspace(0, fs*(n-1)/n, n)
ecg = np.abs(x)

fig, ax = plt.subplots()
fig.subplots_adjust(left=0.1, bottom=0.25)

init_range = [0,100]

ax.plot(time, ecg)
ax.set_xlim(init_range)
ax.set_ylim([5.7e7, 6.3e7])

axfreq = fig.add_axes([0.15, 0.075, 0.7, 0.03])
time_slider = Slider(
	ax = axfreq,
	label = 'Time (s)',
	valmin = 0,
	valmax = 400,
	valinit = 0
	)

def update(val):
	init_range = [time_slider.val, time_slider.val+100]
	ax.set_xlim(init_range)
time_slider.on_changed(update)

plt.show()



