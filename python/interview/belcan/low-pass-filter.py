# filename: low-pass-filter.py
#
# by: Abhay Gupta
# date: 21-08-24

# Fix matplotlib plotting error
from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")

import numpy as np
import matplotlib.pyplot as plt

def low_pass_filter(time, amplitude, samp_rate):
    """ Implement a low pass filter """

    ampl_f = np.fft.fftshift(np.fft.fft(amplitude))
    ampl_f2 = np.fft.fft(amplitude)
    time_f = np.linspace(-1, 1, samp_rate*5)*10/2

    100 # sample rate
    
    print(len(time_f))
    print(len(ampl_f))

    plt.plot(time_f, ampl_f2);
    plt.show();

    amplitude = np.fft.ifft(np.fft.ifftshift(ampl_f)*len(amplitude))

    return amplitude

if __name__=="__main__":
    
    freq = 10           # Freq cycles per second (hz)
    samp_rate = 10      # Sampling rate (measurements per sec)
    filt_freq = 20 
    samp_time = 5

    time = np.linspace(0, samp_time, samp_rate * samp_time)
    amplitude = np.sin(freq * 2*np.pi * time) + np.sin(freq*4 * 2*np.pi * time)


    plt.plot(time, amplitude)
    plt.show()

    amplitude = low_pass_filter(time, amplitude, samp_rate)

    plt.plot(time, amplitude)
    plt.show()








