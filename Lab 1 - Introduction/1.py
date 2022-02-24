import numpy as np
import matplotlib.pyplot as plt
T = 3;
t = np.arange(0, 15, 0.25)

y = np.cos(2*3.14*t/T)

# plt.plot(y,t, 'r')
# plt.subplot(1,2,1)
plt.ylim(-3, 3)
plt.stem(t,y, use_line_collection=True)

plt.show()