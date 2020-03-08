from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

# Sampling rate
fs = 10  # Hz

# sampling interval
length = 50  # second
N = fs * length
t = np.linspace(0, length, num=N, endpoint=False)

# frequency
f = 1/(2*np.pi)  # Hz
u = np.sin(2 * np.pi * f * t)

# plot signal
plt.plot(t, u, '.-')
plt.margins(0.1, 0.1)
plt.xlabel('x')
plt.ylabel('u')
plt.title('Original Signal')
plt.show()

# FFT 
fft = np.fft.fft(u)
ampl = 1/N * np.absolute(fft)

# FFT frequency bins
freqs = np.fft.fftfreq(N, 1/fs)

# plot shifted data on a shifted axis
plt.stem(np.fft.fftshift(freqs), np.fft.fftshift(ampl))
plt.margins(0.1, 0.1)
plt.xlabel('frequency')
plt.ylabel('FFT Amplitude')
plt.title('FFT of Signal')
plt.tight_layout()
plt.show()

# Inverse FFT
inv_fft = np.fft.ifft(fft)

plt.plot(t, inv_fft, '.-')
plt.margins(0.1, 0.1)
plt.xlabel('x')
plt.ylabel('Inverted FFT Amplitude')
plt.title('IFFT of FFT of Signal')
plt.show()

# difference between the signal and the inverted FFT
diff = u - inv_fft

# plot difference
plt.plot(t, diff, '.-')
plt.margins(0.1, 0.1)
plt.xlabel('x')
plt.ylabel('error in u')
plt.title('Error in FFT signal recovery')
plt.show()

# calculate derivative of signal using Fourier method 
ik = 1j*np.hstack((range(0,int(N/2)), range(-int(N/2),0)));
u_hat = np.fft.fft(u)/8
v_hat = ik*u_hat
v = np.real(np.fft.ifft(v_hat))

# plot Fourier Derivative
plt.plot(t, v, '.-')
plt.margins(0.1,0.1)
plt.xlabel('x')
plt.ylabel('u_prime')
plt.title('Derivative using Fourier Methods')
plt.show()

# actual derivative
derivative = np.cos(t)

# plot actual derivative
plt.plot(t, derivative, '.-')
plt.margins(0.1,0.1)
plt.xlabel('x')
plt.ylabel('u_prime')
plt.title('Actual Derivative')
plt.show()

# plot the error in the Fourier method for calculating derivative
der_diff = derivative - v
plt.plot(t, der_diff, '.-')
plt.margins(0.1,0.1)
plt.xlabel('x')
plt.ylabel('error in u_prime')
plt.title('Error in Derivative calculation using Fourier method')
plt.show()