from regression import regression_multi_D_output
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

this = Path(__file__).resolve().parent

xvals = np.linspace(0, 10, 50)
yvals = xvals + np.random.uniform(-1, 1, 50)
zvals = yvals + np.random.uniform(-1, 1, 50)

dpoints = np.array([xvals, yvals, zvals]).T
polyorder = 1

f, *_ = regression_multi_D_output(dpoints, polyorder, 2)

xvals_fit = xvals
yz = [f(x) for x in xvals_fit]
yvals_fit = [k[0] for k in yz]
zvals_fit = [k[1] for k in yz]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(xvals, yvals, zvals, marker="o")
ax.plot(xvals_fit, yvals_fit, zvals_fit)
plt.show()
plt.savefig(this/'test_parametrisation')