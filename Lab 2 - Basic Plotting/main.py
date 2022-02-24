import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import unit_impulse as dell

fig, ax = plt.subplots(4, 2, figsize=(12,24))

# 1. Unit Step Function
t = np.linspace(-1, 1, 100)

def unit_step(t, x):
  y = np.array([])
  for i in t:
    if i >= x: y = np.append(y, 1)
    else: y = np.append(y, 0)
  return y

ax[0,0].plot(t, unit_step(t, 0))
ax[0,0].set_ylim(-1,2)
ax[0,0].set_xlabel("Unit Step function")


# 2. Unit Impulse
t = np.linspace(-10, 10, 100)
ax[0,1].plot(t, dell(len(t), 50))
ax[0,1].set_xlabel("Unit Impulse function")


# 3. Ramp Function
t = np.linspace(-1, 1, 100)

def ramp(t, x):
  y = np.array([])
  for i in t:
    if i > x: y = np.append(y, i)
    else: y = np.append(y, 0)
  return y

ax[1,0].plot(t, ramp(t, 0))
ax[1,0].set_xlabel("Ramp function")
ax[1,0].set_ylim(-0.5,1)


# 4. Periodic Sinusodial Sequence
t = np.arange(-2, 2, 0.05)

def sinusodial_seq(t, frequency=1):
  omega = 2 * np.pi * frequency
  y = np.sin(omega*t)
  return y

ax[1,1].plot(t, sinusodial_seq(t, 1))
ax[1,1].set_xlabel("Periodic Sinusodial")
ax[1,1].set_ylim(-5,5)


# Pulse
t = np.linspace(0, 1, 500, endpoint=False)
ax[2,0].plot(t, signal.square(2 * np.pi * 5 * t))
ax[2,0].set_xlabel("Square Pulse")
ax[2,0].set_ylim(-10,10)


# 5. Periodic Rectangular Pulse
sampling_rate = 1000
wave_frequency = 0.5
time = 60
t = np.linspace(0, time, sampling_rate)

def periodic_rectangular_pulse(t,frequency,function,p):
  y = np.array([])
  period = p
  for i in range(len(t)):
    curr = np.floor(t[i])
    if (curr % (1/frequency)!=0):
      if ((i % period)/float(period)) > -1e-5:
        y = np.append(y ,function(curr))
      else:
        y = np.append(y, 0)
    else:
      y = np.append(y, 0)
  return y

def fun(x):
  return np.sin(2*np.pi*0.05*x)

x1 = periodic_rectangular_pulse(t, wave_frequency, fun, sampling_rate)

ax[2,1].plot(t, x1)
ax[2,1].set_xlabel("Periodic Rectangular Pulse")
ax[2,1].set_ylim(-2,2)


# 6. Asymmetric Sawtooth Waveform
frequency = 3
TPeriod = 1/frequency
time = 1
sampling_rate = 1000
width = 0.2

def asymmetric_sawtooth(t,T,W,skew):
  w1 = 0.5*(W + float(skew*W))
  y = np.array([])
  Ti = (t[-1]-t[0])/(t[1]-t[0])
  T = T*Ti
  for index,val in enumerate(t):
    curr = index%int(T)
    if (curr-int(W*0.5*Ti)) < 1e-5:
      if skew>0:
        w1 = skew * W*0.5
        if curr-(w1*Ti)<1e-5:
          y = np.append(y,0.5+((1/float(Ti))*curr * (1/float(W))))
        else:
          w2 = (0.5*W)-(skew*W*0.5)
          if w2==0:
            y = np.append(y, 0)
          else:
            slope = (0.5+skew)/float(w2)
            y = np.append(y, (0.5+skew)+(-(1/float(Ti))*curr*slope))
      else:
        val = abs(skew)*0.5
        slope = (0.5+val)/(W*0.5)
        y = np.append(y, (0.5+val)+(-(1/float(Ti))*curr*slope))
    else:
      y = np.append(y,0)
  return y

t = np.linspace(0, time,sampling_rate,endpoint=True)
x_t = asymmetric_sawtooth(t=t, T=TPeriod, W=width, skew=0)

ax[3,0].plot(t, x_t)
ax[3,0].set_xlabel("Asymmetric Sawtooth Waveform")
ax[3,0].set_ylim(0,1)

# 7. Guassian Pulse
frequency = 10000
bandwidth = 0.5
sampling_rate = 10000000
cutoff = -40
t = np.linspace(-0.001, 0.001,sampling_rate)
ax[3,1].plot(t, signal.gausspulse(t, frequency, bandwidth, cutoff))
ax[3,1].set_xlabel("Gaussian Pulse")

plt.show()