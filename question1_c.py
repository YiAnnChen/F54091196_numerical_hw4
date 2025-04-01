import numpy as np
from scipy.integrate import quad
a = 1
b = 2
n = 11
h = 0.1
x = np.linspace(a, b, n)
f = np.exp(x) * np.sin(4 * x)

I_mid = 2* h * (np.sum(f[1:n:2]))

print("The value using midpoint rule is:",I_mid)
