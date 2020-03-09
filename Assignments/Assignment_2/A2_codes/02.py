from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

# parameters
c_k = 1.613
alpha1 = 0.39
alpha2 = 1.2
alpha3 = 4.0
alpha4 = 2.1
alpha5 = 0.522
alpha6 = 10.0
alpha7 = 12.58

# parameters for x1/M = 20
epsilon = 22.8
l = 0.250
eta = 0.00011

N = 50000
kappa = np.linspace(0, 10000, num=N, endpoint=False)


E = (c_k)*(np.power(epsilon,2/3))*(np.power(kappa,-5/3))*np.power(kappa*l/np.power(np.power(kappa*l,alpha2) + alpha1,1/alpha2),5/3+alpha3)*np.exp(-alpha4*kappa*eta)*(1 + alpha5*(1/np.pi * np.arctan(alpha6*np.log10(kappa*eta) + alpha7) + 0.5))

plt.plot(kappa, E, '.-', label = 'x1/M = 20')
plt.margins(0.1, 0.1)
plt.yscale('log')
plt.xscale('log')
plt.ylim([0.0000001, 1])
plt.xlim([1, 10000])
plt.legend(loc="upper right")
plt.xlabel('k')
plt.ylabel('E')
plt.title('Energy Spectra')

# parameters for x1/M = 30
epsilon = 9.13
l = 0.288
eta = 0.00014

N = 50000
kappa = np.linspace(0, 10000, num=N, endpoint=False)


E = (c_k)*(np.power(epsilon,2/3))*(np.power(kappa,-5/3))*np.power(kappa*l/np.power(np.power(kappa*l,alpha2) + alpha1,1/alpha2),5/3+alpha3)*np.exp(-alpha4*kappa*eta)*(1 + alpha5*(1/np.pi * np.arctan(alpha6*np.log10(kappa*eta) + alpha7) + 0.5))

plt.plot(kappa, E, '.-', label = 'x1/M = 30')
plt.margins(0.1, 0.1)
plt.yscale('log')
plt.xscale('log')
plt.ylim([0.0000001, 1])
plt.xlim([1, 10000])
plt.legend(loc="upper right")
plt.xlabel('k')
plt.ylabel('E')
plt.title('Energy Spectra')

# parameters for x1/M = 40
epsilon = 4.72
l = 0.321
eta = 0.00016

N = 50000
kappa = np.linspace(0, 10000, num=N, endpoint=False)


E = (c_k)*(np.power(epsilon,2/3))*(np.power(kappa,-5/3))*np.power(kappa*l/np.power(np.power(kappa*l,alpha2) + alpha1,1/alpha2),5/3+alpha3)*np.exp(-alpha4*kappa*eta)*(1 + alpha5*(1/np.pi * np.arctan(alpha6*np.log10(kappa*eta) + alpha7) + 0.5))

plt.plot(kappa, E, '.-', label = 'x1/M = 40')
plt.margins(0.1, 0.1)
plt.yscale('log')
plt.xscale('log')
plt.ylim([0.0000001, 1])
plt.xlim([1, 10000])
plt.legend(loc="upper right")
plt.xlabel('k')
plt.ylabel('E')
plt.title('Energy Spectra')


# parameters for x1/M = 48
epsilon = 3.41
l = 0.332
eta = 0.00018

N = 50000
kappa = np.linspace(0, 10000, num=N, endpoint=False)


E = (c_k)*(np.power(epsilon,2/3))*(np.power(kappa,-5/3))*np.power(kappa*l/np.power(np.power(kappa*l,alpha2) + alpha1,1/alpha2),5/3+alpha3)*np.exp(-alpha4*kappa*eta)*(1 + alpha5*(1/np.pi * np.arctan(alpha6*np.log10(kappa*eta) + alpha7) + 0.5))

plt.plot(kappa, E, '.-', label = 'x1/M = 48')
plt.margins(0.1, 0.1)
plt.yscale('log')
plt.xscale('log')
plt.ylim([0.0000001, 1])
plt.xlim([1, 10000])
plt.legend(loc="upper right")
plt.xlabel('k')
plt.ylabel('E')
plt.title('Energy Spectra')
plt.show()

plt.plot([20, 30, 40, 48], [0.0426, 0.0256, 0.0179, 0.0142])
plt.gcf().subplots_adjust(left=0.15)
plt.ylim([0.01, 0.05])
plt.xlim([10, 80])
plt.yscale('log')
plt.xscale('log')
plt.xlabel('x1/M')
plt.ylabel('k/(<u1>^2)')
plt.show()