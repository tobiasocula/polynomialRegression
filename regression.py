from scipy.optimize import least_squares
import numpy as np

def findparams(dpoints, polyorder):
    # f: R^m -> R^n
    # dpoints: shape (n, 2)
    # polyorder = m-1: < n
    assert dpoints.shape[0] > polyorder, AssertionError()
    def F(x):
        return [
            sum(x[j] * dpoints[i,0]**j for j in range(polyorder+1)) - dpoints[i,1]
            for i in range(dpoints.shape[0])
        ]

    inp = np.array((polyorder+1)*[1])

    res = least_squares(F, inp, method="lm")
    return res.x