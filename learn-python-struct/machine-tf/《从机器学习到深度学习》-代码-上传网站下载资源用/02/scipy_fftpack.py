import numpy as np
from scipy.fftpack import fft, ifft

x = np.array([2.0, 3.0, -1.0, -3.0, 0.5])

y = fft(x)

print(y)

yinv = ifft(y)

print(yinv)



y = fft(x, 6)

print(y)

yinv = ifft(y)

print(yinv)
