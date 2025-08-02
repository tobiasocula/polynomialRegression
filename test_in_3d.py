import numpy as np
from regression import regression_multi_D
import matplotlib.pyplot as plt
from pathlib import Path

this = Path(__file__).resolve().parent

def true_func(x1, x2):
    return 2 + 3*x1 - x2 + 0.5*x1**2 + x1*x2 - 0.3*x2**2

xvals = np.random.uniform(0, 100, size=10)
yvals = np.random.uniform(0, 100, size=10)
polyorder = 1


dpoints = np.array([
    [x, y, true_func(x, y)]
    for x, y in zip(xvals, yvals)
])


f, params, labels = regression_multi_D(dpoints, polyorder)

x = np.linspace(dpoints[:,0].min()-1, dpoints[:,0].max()+1, 100)
y = np.linspace(dpoints[:,1].min()-1, dpoints[:,1].max()+1, 100)
X, Y = np.meshgrid(x, y)

def f_grid(X, Y):
    # Stack X and Y into a shape (2, m, n)
    vars_stack = np.array([X, Y])  # shape (2, 100, 100)
    result = np.full_like(X, fill_value=params[0])  # start with constant term

    for label, coef in zip(labels[1:], params[1:]):
        # label is a tuple of indices, e.g. (0, 1)
        # grab variables by indices and multiply
        term_vals = np.ones_like(X)
        for idx in label:
            term_vals = term_vals * vars_stack[idx, :, :]
        result += coef * term_vals

    return result

Z = f_grid(X, Y)


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.scatter(xvals, yvals, [true_func(x1, x2) for x1,x2 in zip(xvals, yvals)], marker='o')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.savefig(this/'test_3D')