import random
import matplotlib.pyplot as plt
import numpy as np

y = []
t = np.arange(0, 100, 1)
for i in range(0,100):
  x = random.randint(-100, 100)
  y.append(x)

plt.ylim(-300, 300)
plt.plot(y)
plt.show()