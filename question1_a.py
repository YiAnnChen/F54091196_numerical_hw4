import numpy as np
from scipy.integrate import quad
a = 1
b = 2
n = 11
h = 0.1
x = np.linspace(a, b, n)
f = np.exp(x) * np.sin(4 * x)

I_trap = (h / 2) * (f[0] + 2 * np.sum(f[1:n-1]) + f[n-1])
#I_true, _ = quad(lambda x: np.exp(x) * np.sin(4 * x), a, b)

#print("True value =", I_true)

print("The value using trapezoidal rule is:",I_trap)
