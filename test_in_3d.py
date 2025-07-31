import numpy as np
from regression import findparams_general
import matplotlib.pyplot as plt

def true_func(x1, x2):
    return 2 + 3*x1 - x2 + 0.5*x1**2 + x1*x2 - 0.3*x2**2

x1_vals = np.random.uniform(0, 100, size=10)
x2_vals = np.random.uniform(0, 100, size=10)
polyorder = 2


dpoints = np.array([
    [x1, x2, true_func(x1, x2)]
    for x1, x2 in zip(x1_vals, x2_vals)
])


params, labels = findparams_general(dpoints, polyorder)

def f(x,y):
    res = params[0]
    for l, p in zip(labels, params[1:]):
        r = 1
        if l == (1,):
            r *= y
        elif l == (0,):
            r *= x
        else:
            r *= x*y
        res += p * r
    return res
        

x = np.linspace(dpoints[:,0].min()-1, dpoints[:,0].max()+1, 100)
y = np.linspace(dpoints[:,1].min()-1, dpoints[:,1].max()+1, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.scatter(x1_vals, x2_vals, [true_func(x1, x2) for x1,x2 in zip(x1_vals, x2_vals)], marker='o')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()