from scipy.optimize import least_squares
import numpy as np
from itertools import combinations_with_replacement
from math import comb
from collections import Counter
import sys

def regression_2D(dpoints, p):

    """
    MSE-fit model for datapoints in R^2
    returns function f: R -> R
    as well as its parameters

    dpoints: the n x 2 matrix whose rows are the datapoints
    p: the polynomial order to use for the output function
    """

    assert dpoints.shape[0] > p, AssertionError()

    def F(x):
        return [
            sum(x[j] * dpoints[i,0]**j for j in range(p+1)) - dpoints[i,1]
            for i in range(dpoints.shape[0])
        ]

    inp = np.random.uniform(0, 10, p+1)

    res = least_squares(F, inp, method="lm").x
    def f(x):
        return np.polyval(res[::-1], x)

    return f, res

def regression_multi_D(dpoints, p):

    """
    Same thing, but works for datapoints in any R^k
    dpoints: the n x k matrix whose rows are the datapoints
    the function uses the first k-1 components of the points
    as the input and the last component as its output
    p: the polynomial order to use for the output function (this time
    a multi-variable polynomial function)
    the function for the least-squares problem uses d = comb(p+k,p) parameters
    """

    k = dpoints.shape[1]
    n = dpoints.shape[0]

    assert p <= k, AssertionError()
    assert p < n, AssertionError()
    
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
    res = least_squares(F, inp, method="lm").x

    def f(x):
        # f: R^(k-1) -> R
        result = res[0]
        if isinstance(x, (int, float)):
            for l, p in zip(labels, res[1:]):
                result += x ** len(l) * p
            return result
        for l, p in zip(labels, res[1:]):
            result += np.prod([x[j] for j in l]) * p
        return result

    return f, res, labels


def regression_multi_D_output(dpoints, p, m):

    """
    Now we use the first k-m components of each datapoint for the input
    and the last m components as the output (multi-dimensional output)
    """

    k = dpoints.shape[1]
    # now we have comb(p+k-m,p) possible parameters
    d = comb(p+k-m,p)

    R = np.empty(shape=(d,m))
    funcs = [] # we now have m component functions of the main function

    for j in range(m):
        # select first k-m components of each datapoint, as well as one column (for each function)
        func, params, labels = regression_multi_D(dpoints[:,list(range(k-m)) + [k-m+j]], p)
        R[:,j] = params
        funcs.append(func)

    def f(x):
        # f: R^(k-m) -> R^m
        return tuple(ff(x) for ff in funcs)
    
    return f, R, labels