from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 1, 40, endpoint=True)
y = signal.square(2 * np.pi * 4 * t)

# plt.plot(t, y)
plt.stem(t, y, use_line_collection=True)
plt.show()