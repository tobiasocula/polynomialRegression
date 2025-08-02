import numpy as np
from regression import regression_2D
import matplotlib.pyplot as plt
from pathlib import Path

this = Path(__file__).resolve().parent

xvals = np.random.uniform(0, 20, size=10)
def func(x):
    return 2*x+3
yvals = func(xvals) + np.random.uniform(-10, 10, size=10)
polyorder = 3

dpoints = np.array([xvals, yvals]).T

f, params = regression_2D(dpoints, polyorder)

fig, ax = plt.subplots()
x = np.linspace(dpoints[:,0].min()-1, dpoints[:,0].max()+1, 100)
y = f(x)
ax.plot(x,y)
ax.scatter(dpoints[:,0],dpoints[:,1])
plt.show()
plt.savefig(this/"test_2D")