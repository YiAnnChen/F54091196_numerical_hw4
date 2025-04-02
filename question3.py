#a. Simpson’s rule for n = 4 and m = 4

import numpy as np
from scipy.integrate import dblquad

def f(x, y):
    return 2 * y * np.sin(x) + np.cos(x)**2

def simpson_1d(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    fx = f(x)
    return h / 3 * (fx[0] + 4 * np.sum(fx[1:n:2]) + 2 * np.sum(fx[2:n-1:2]) + fx[n])

def double_simpson(n, m):
    a, b = 0, np.pi / 4
    hx = (b - a) / n
    x_vals = np.linspace(a, b, n + 1)

    result = 0
    for i, xi in enumerate(x_vals):
        y_lower = np.sin(xi)
        y_upper = np.cos(xi)

        fy = lambda y: f(xi, y)

        if y_lower == y_upper:
            inner = 0
        else:
            inner = simpson_1d(fy, y_lower, y_upper, m)

        coeff = 1
        if i == 0 or i == n:
            coeff = 1
        elif i % 2 == 1:
            coeff = 4
        else:
            coeff = 2

        result += coeff * inner

    return hx / 3 * result

simpson_result = double_simpson(n=4, m=4)
print("a) Composite Simpson's rule result =", simpson_result)

#b
xg = np.array([-0.7745966692, 0, 0.7745966692])
wg = np.array([5/9, 8/9, 5/9])

def gaussian_double_integral():
    result = 0
    for i in range(3):
        xi = 0.5 * (np.pi/4) * xg[i] + np.pi/8
        wi = wg[i]
        y_a = np.sin(xi)
        y_b = np.cos(xi)
        Jx = (np.pi/4) / 2
        Jy = (y_b - y_a) / 2

        inner_sum = 0
        for j in range(3):
            eta = xg[j]
            yj = Jy * eta + (y_a + y_b) / 2
            inner_sum += wg[j] * f(xi, yj)

        result += wi * inner_sum * Jy

    return result * Jx

gauss_result = gaussian_double_integral()
print("b) Gaussian quadrature result =", gauss_result)
#c
exact_val, _ = dblquad(lambda y, x: 2 * y * np.sin(x) + np.cos(x)**2,
                       0, np.pi / 4,
                       lambda x: np.sin(x),
                       lambda x: np.cos(x))

absolute_error_a = simpson_result - exact_val
absolute_error_b = gauss_result - exact_val
print("c) Exact value =", exact_val)
print("c) error bound between simpson and exact =",absolute_error_a)
print("c) error bound between gauss and exact =",absolute_error_b)