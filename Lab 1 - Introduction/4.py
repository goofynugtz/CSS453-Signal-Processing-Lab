import random
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# sampling_rate = 100
# wave_frequency = 5
time = 60 #(secs)
t = np.linspace(0, time, 30, endpoint=False)
x2 = np.sin(2*np.pi*t)

# x1 = signal.square(x2)
# def rectangular(t):
  # return 1 * (abs(t) < 0.5)
plt.stem(t, x2, use_line_collection=True)
plt.ylim(-5,5)

plt.show()