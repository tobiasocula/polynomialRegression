from scipy.optimize import least_squares
import numpy as np
from itertools import combinations_with_replacement
from math import comb
from collections import Counter
import sys

def findparams(dpoints, p):


    """MSE-fit model for datapoints in R^2"""

    assert dpoints.shape[0] > p, AssertionError()
    def F(x):
        return [
            sum(x[j] * dpoints[i,0]**j for j in range(p+1)) - dpoints[i,1]
            for i in range(dpoints.shape[0])
        ]

    inp = np.array((p+1)*[1])

    res = least_squares(F, inp, method="lm")
    return res.x

def findparams_general(dpoints, p):


    """Same thing, but works for datapoints in any R^k"""

    # k = dimensions of points
    # n = number of points
    # p = polyorder
    # m = k - 1
    k = dpoints.shape[1]
    n = dpoints.shape[0]

    assert p <= k and p < n, AssertionError()
    
    # F: R^d ->R^n
    # where d = comb(p+k-1,p)
    def F(x):
        # x has dimension comb(p+k-1, p)
        R = np.empty(n)

        for i in range(n):
            # iterates over rows of function matrix
            row = x[0]
            counter = 1
            for pidx in range(1, p+1):
                for t in combinations_with_replacement(dpoints[i,:k-1], pidx):
                    row += np.prod(t) * x[counter]
                    counter += 1
            R[i] = row - dpoints[i,k-1]
            
        return R
    
    labels = []
    for pidx in range(1, p+1):
        for index_combo in combinations_with_replacement(range(k-1), pidx):
            labels.append(index_combo)
    inp = np.random.uniform(0,10, comb(p+k-1,p))
    res = least_squares(F, inp, method="lm")
    return res.x, labels