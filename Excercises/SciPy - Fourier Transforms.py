#Fourier Transform

from scipy.fftpack import fft, ifft
import numpy as np

x = np.array([1,2,3,4])
y = ifft(x)             #inverse fourier transform
print (y)