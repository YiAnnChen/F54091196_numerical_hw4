from __future__ import division
from pylab import *
from scipy.special.orthogonal import p_roots
G = 0.0
def question_func(x):
    return x**2 * np.log(x)

def gauss(f,a,b,n):
    G=0.0
    [x,w] = p_roots(n)
    #for i in range(n):
        #print(x[i],w[i])
    for i in range(n):
        G += w[i]*f(0.5*(b-a)*x[i]+ 0.5*(b+a))
    G = 0.5*(b-a)*G
    return G

print("The value using Gaussian Quadrature with 3 is:",gauss(question_func,1,1.5,3))
print("The value using Gaussian Quadrature with 4 is:",gauss(question_func,1,1.5,4))