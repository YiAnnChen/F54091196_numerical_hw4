import numpy as np

def simpson(a, b, n):
    h = (b - a) / n
    t = np.linspace(a, b, n + 1)
    f = t**2 * np.sin(1/t)
    I_simp = (h / 3) * (f[0] + 4 * np.sum(f[1:n:2]) + 2 * np.sum(f[2:n-1:2]) + f[-1])
    return I_simp

print("The value using composite Simpson's rule with n=4 is", simpson(1e-6, 1, 4))
