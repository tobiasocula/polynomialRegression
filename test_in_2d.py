import numpy as np
from regression import findparams
import matplotlib.pyplot as plt

def true_func(x):
    return 6 * np.sin(0.7*x**3) - 5*x**2 + x - 2

xvals = np.random.uniform(0, 100, size=10)
polyorder = 1

dpoints = np.array([
    [x, true_func(x)]
    for x in xvals
])

params = findparams(dpoints, polyorder)

def f(x):
    res = 0
    for i,p in enumerate(params):
        res += x**i*p
    return res

fig, ax = plt.subplots()
x = np.linspace(dpoints[:,0].min()-1, dpoints[:,0].max()+1, 100)
y = f(x)
ax.plot(x,y)
ax.scatter(dpoints[:,0],true_func(dpoints[:,0]))
plt.show()