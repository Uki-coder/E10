import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy as sci

def voltage_time(x,a,b,c):
    return c*np.exp(-x/b)+a

def draw_calc(input_time, input_voltage, output_popt, output_err, output_delta, output_epsilon, p0):
    mpl.use('TkAgg')
    plt.rcParams['text.usetex'] = True

    time = np.loadtxt(input_time)
    voltage = np.loadtxt(input_voltage)
    time_space = np.linspace(-0.02*max(time), 1.05*max(time), 1000)

    fig, ax = plt.subplots()
    ax.scatter(time, voltage)
    ax.set_xlabel('$t$ [s]')
    ax.set_ylabel('$U$ [V]')
    plt.grid()

    popt, pcov = sci.optimize.curve_fit(voltage_time, time, voltage, maxfev=10000)
    perr = np.sqrt(np.diag(pcov))
    pdelta = 3*perr
    pepsilon = np.abs(pdelta/popt) * 100

    np.savetxt(output_err, perr)
    np.savetxt(output_popt, popt)
    np.savetxt(output_delta, pdelta)
    np.savetxt(output_epsilon, pepsilon)

    ax.plot(time_space, voltage_time(time_space, *popt), color='b', label='dopasowanie dla zależności $U(t)$')
    ax.scatter(time, voltage, color='r', marker='o', label='pomiary $U(t)$')
    ax.legend()
    plt.show()