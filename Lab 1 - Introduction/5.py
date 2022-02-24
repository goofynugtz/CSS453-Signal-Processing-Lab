import random
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

frequency = 3
time = 60
sampling_rate = int(1e6)
t = np.linspace(0, time, sampling_rate, endpoint=False)
def asawtooth(period, t):
  y = -t % period
  return y
x_t = asawtooth(0.2, t)
# print(x_t)
# x_t = x_t * (x_t > 0)
plt.plot(t, x_t)
plt.xlim(0,10)
plt.show()