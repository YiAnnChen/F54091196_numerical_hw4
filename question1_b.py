import numpy as np
from scipy.integrate import quad
a = 1
b = 2
n = 11
h = 0.1
x = np.linspace(a, b, n)
f = np.exp(x) * np.sin(4 * x)

I_simp = (h / 3) * (f[0] + 4 * np.sum(f[1:n-1:2])+ 2 * np.sum(f[2:n-2:2]) + f[n-1])

print("The value using simpson rule is:",I_simp)
