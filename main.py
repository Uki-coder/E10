import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy as sci
#-------------------------------------------------------
def voltage_time(x,a,b,c):
    return c*np.exp(-x/b)+a

mpl.use('TkAgg')
plt.rcParams['text.usetex'] = True

#2c--------------------------------------------------------
time_2c = np.loadtxt('data/time_2c.txt')
voltage_2c = np.loadtxt('data/voltage_2c.txt')
time_space_2c = np.linspace(-2, max(time_2c) + 10, 1000)

fig, ax = plt.subplots()
ax.scatter(time_2c, voltage_2c)
ax.set_xlabel('$t$ [s]')
ax.set_ylabel('$U$ [V]')
plt.grid()

popt, pcov = sci.optimize.curve_fit(voltage_time, time_2c, voltage_2c, maxfev=10000)
perr = np.sqrt(np.diag(pcov))
np.savetxt('output/error_2c.txt', perr)
np.savetxt('output/popt_2c.txt', popt)

ax.plot(time_space_2c, voltage_time(time_space_2c, *popt), color = 'b', label = 'dopasowanie dla zależności $U(t)$')
ax.scatter(time_2c, voltage_2c, color='r', marker = 'o', label = 'pomiary $U(t)$')
ax.legend()
plt.show()

#c----------------------------------------------------------

time_c = np.loadtxt('data/time_c.txt')
voltage_c = np.loadtxt('data/voltage_c.txt')
time_space_c = np.linspace(-1, max(time_c) + 10, 1000)

fig, ax = plt.subplots()
ax.scatter(time_c, voltage_c)
ax.set_xlabel('$t$ [s]')
ax.set_ylabel('$U$ [V]')
plt.grid()

popt, pcov = sci.optimize.curve_fit(voltage_time, time_c, voltage_c)
perr = np.sqrt(np.diag(pcov))
np.savetxt('output/error_c.txt', perr)
np.savetxt('output/popt_c.txt', popt)

ax.plot(time_space_c, voltage_time(time_space_c, *popt), color = 'b', label = 'dopasowanie dla zależności $U(t)$')
ax.scatter(time_c, voltage_c, color='r', label = 'pomiary $U(t)$')
ax.legend()
plt.show()