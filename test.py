import numpy as np
from .regression import findparams
import matplotlib.pyplot as plt

dpoints = np.array([
    [1,-5],
    [4,-10],
    [10,5],
    [5,-20]
])
polyorder = 3

params = findparams(dpoints, polyorder)

def func(x):
    res = 0
    for i,p in enumerate(params):
        res += x**i*p
    return res

fig, ax = plt.subplots()
x = np.linspace(dpoints[:,0].min()-1, dpoints[:,0].max()+1, 100)
y = func(x)
ax.plot(x,y)
ax.scatter(dpoints[:,0],dpoints[:,1])
plt.show()