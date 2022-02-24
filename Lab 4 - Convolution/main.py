import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import unit_impulse as dell
plt.style.use("seaborn-darkgrid")

""" 
Convulation is the operation of taking two signals, inverting one of them
and then shifting while multiplying values of the two signals and summing
them up 
"""

# Question 1 - Convolve
x_t = np.random.randint(-10,10,size=10)
h_t = np.random.randint(-10,10,size=10)
t = np.arange(0,10)

fig1, ax1 = plt.subplots(2, 2, figsize=(8,8))

ax1[0,0].stem(t,x_t)
ax1[0,0].set_xlabel("Random x(t)")
ax1[0,1].stem(t,h_t)
ax1[0,1].set_xlabel("Random h(t)")
ax1[1,0].stem(np.arange(0,len(x_t)+len(h_t)-1), np.convolve(x_t,h_t))
ax1[1,0].set_xlabel("Convolution of x(t) and h(t)")
# Question 2 - Proof
ax1[1,1].stem(np.arange(0,len(x_t)+len(h_t)-1), np.convolve(h_t,x_t))
ax1[1,1].set_xlabel("Convolution of h(t) and x(t)")

# Question 3
n = 50
# dell is unit_impulse funtion from scipy.signal as imported
x_n = 3 * dell(60,n+2) - dell(60,n-1) + 2 * dell(60,n-3)
t = np.linspace(0, 60, 60)

def unit_step(t, x):
  y = np.array([])
  for i in t:
    if i >= x: y = np.append(y, 1)
    else: y = np.append(y, 0)
  return y

h_n = unit_step(t,n+4) - unit_step(t,n-3)

fig2, ax2 = plt.subplots(figsize=(8,8))
axes2 = []
axes2.append(plt.subplot2grid(shape=(2,2), loc=(0,0)))
axes2.append(plt.subplot2grid(shape=(2,2), loc=(0,1)))
axes2.append(plt.subplot2grid(shape=(2,2), loc=(1,0), colspan=2))
axes2[0].plot(x_n)
axes2[0].set_xlabel("Defined x[n]")
axes2[1].plot(h_n)
axes2[1].set_xlabel("Defined h[n]")
axes2[2].plot(np.convolve(x_n, h_n))
axes2[2].set_xlabel("Convolution of x[n] and h[n]")

# Question 4
plt.style.use("seaborn-darkgrid")
t = np.linspace(-2,2,500)
x_n = np.sin(2 * np.pi * t)
noise = np.random.randn(len(x_n))-0.5
x_n = x_n + noise

h_1 = np.ones(3)/3
h_2 = np.ones(3)/7
h_3 = np.ones(11)/11

convol1 = np.convolve(h_1,x_n,mode='full')
convol2 = np.convolve(h_2,x_n,mode='full')
convol3 = np.convolve(h_3,x_n,mode='full')

fig3,ax3 = plt.subplots(2,2, figsize=(8,8))

ax3[0,0].plot(t,x_n, lw=0.5, label="x[n]")
ax3[0,0].legend()

ax3[1,0].plot(t,x_n, lw=0.5, label="x[n]")
ax3[1,0].plot(np.linspace(-2,2,*convol1.shape),convol1, lw=1, label="x[n]*h1[n]")
ax3[1,0].legend()

ax3[0,1].plot(t,x_n, lw=0.5, label="x[n]")
ax3[0,1].plot(np.linspace(-2,2,*convol2.shape),convol2, lw=1, label="x[n]*h2[n]")
ax3[0,1].legend()

ax3[1,1].plot(t,x_n, lw=0.5, label="x[n]")
ax3[1,1].plot(np.linspace(-2,2,*convol3.shape),convol3, lw=1, label="x[n]*h3[n]")
ax3[1,1].legend()


# Question 5
def h(inp): 
  impulse_response = np.ones(10)/2
  out = np.convolve(inp, impulse_response, mode="full")
  return out

def h1(inp): 
  impulse_response = np.ones(10)/4
  out = np.convolve(inp, impulse_response, mode="full")
  return out

def h2(inp):
  impulse_response = np.ones(10)/10
  out = np.convolve(inp, impulse_response, mode="full")
  return out


# Randomly choosen signals
start, end = -10, 10
t = np.linspace(start,end,500)
x = np.sin(t) # Input signal

Hout1 = h(x)
w = np.random.randn(len(Hout1))   # Random (+ve) Noise
Hout1WithW = Hout1+w
Hout2 = h(Hout1WithW)

H1out = h1(x)
z = np.random.randn(len(H1out))-1 # Random (-ve) Noise
H1outWithZ = H1out + z
H2out = h2(H1outWithZ)

Y = H2out + Hout2

fig1, ax1 = plt.subplots(5,2, figsize=(10,20))

def t_axis(inp):
  return np.arange(start,end+(t[1]-t[0])*(inp.__len__()-t.__len__()+1),(t[1]-t[0]))

ax1[0,0].plot(t, x)
ax1[0,0].set_xlabel("x(t)")

ax1[0,1].plot(t_axis(Hout1), Hout1)
ax1[0,1].set_xlabel("h(x(t))")

ax1[1,0].plot(t_axis(w), w)
ax1[1,0].set_xlabel("w(t)")

ax1[1,1].plot(t_axis(Hout1WithW),Hout1WithW)
ax1[1,1].set_xlabel("h(x(t)) + w(t)")

ax1[2,0].plot(t_axis(Hout2), Hout2)
ax1[2,0].set_xlabel("h(x(t)) + w(t)")

ax1[2,1].plot(t_axis(H1out),H1out)
ax1[2,1].set_xlabel("h1(x(t))")

ax1[3,0].plot(t_axis(z),z)
ax1[3,0].set_xlabel("z(t)")

ax1[3,1].plot(t_axis(H1outWithZ), H1outWithZ)
ax1[3,1].set_xlabel("h1(x(t)) + z(t)")

ax1[4,0].plot(t_axis(H2out), H2out)
ax1[4,0].set_xlabel("h2(h1(x(t)) + z(t))")

ax1[4,1].plot(t_axis(Y), Y)
ax1[4,1].set_xlabel("y(t)")

plt.show()