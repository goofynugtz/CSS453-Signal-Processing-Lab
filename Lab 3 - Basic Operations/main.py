import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-darkgrid")

t = np.linspace(-30, 30, 2000)

def x(t):
  f = []
  for i in t:
    if 0 <= i and i < 5:
      f.append(1)
    elif 5 <= i and i < 8:
      f.append(2)
    elif 8 <= i and i < 12:
      f.append(12)
    else:
      f.append(0)
  f = np.array(f)
  return f


def y(t):
  f = []
  for i in t:
    if 0 <= i and i < 7:
      f.append(2)
    elif 7 <= i and i < 10:
      f.append(10)
    elif 10 <= i and i < 15:
      f.append(15)
    else:
      f.append(0)
  f = np.array(f)
  return f


fig, ax = plt.subplots(6, 2, figsize=(12,32))

x_plot = x(t)
y_plot = y(t)

ax[0,0].plot(t, x_plot, label="x(t)")
ax[0,0].set_xlabel("Given x(t)")
ax[0,0].legend()

ax[0,1].plot(t, y_plot, label="y(t)")
ax[0,1].set_xlabel("Given y(t)")
ax[0,1].legend()

ax[1,0].plot(t, x_plot, label="x(t)")
ax[1,0].plot(t, y_plot, label="y(t)")
ax[1,0].plot(t, x_plot + y_plot, label="x(t)+y(t)")
ax[1,0].set_xlabel("1) Addition")
ax[1,0].legend()

ax[1,1].plot(t, x_plot, label="x(t)")
ax[1,1].plot(t, y_plot, label="y(t)")
ax[1,1].plot(t, x_plot - y_plot, label="x(t)-y(t)")
ax[1,1].set_xlabel("2) Subtraction")
ax[1,1].legend()

ax[2,0].plot(t, x_plot, label="x(t)")
ax[2,0].plot(t, y_plot, label="y(t)")
ax[2,0].plot(t, x_plot * y_plot, label="x(t)*y(t)")
ax[2,0].set_xlabel("3) Multiplication")
ax[2,0].legend()

ax[2,1].plot(t, (x(t)/2) + (y(t)/3), label="x(t)/2 + y(t)/3")
ax[2,1].set_xlabel("4) x(t)/2 + y(t)/3")
ax[2,1].legend()

ax[3,0].plot(t, x_plot, label="x(t)")
ax[3,0].plot(t, x(-t), label="x(-t)")
ax[3,0].set_xlabel("5) x(-t)")
ax[3,0].legend()

ax[3,1].plot(t, y_plot, label="y(t)")
ax[3,1].plot(t, y(-t), label="y(-t)")
ax[3,1].set_xlabel("6) y(-t)")
ax[3,1].legend()

ax[4,0].plot(t, x_plot, label="x(t)")
ax[4,0].plot(t, x(2*t), label="x(2t)")
ax[4,0].set_xlabel("7) x(2t)")
ax[4,0].legend()

ax[4,1].plot(t, x_plot, label="x(t)")
ax[4,1].plot(t, x(-2*t+5), label="x(-2t + 5)")
ax[4,1].set_xlabel("8) x(-2t + 5)")
ax[4,1].legend()

ax[5,0].plot(t, x(0.5*t - 5), label="x(0.5t - 5)")
ax[5,0].set_xlabel("9) x(0.5t - 5)")
ax[5,0].legend()

ax[5,1].plot(t, x(-0.5*t - 5), label="x(-0.5t - 5)")
ax[5,1].set_xlabel("10) x(-0.5t - 5)")
ax[5,1].legend()

plt.show()