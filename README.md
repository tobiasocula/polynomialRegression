Polynomial regression implementation.  
Given a matrix $A\in\mathbb{R}^{n\times k}$ representing $n$ datapoints in $\mathbb{R}^k$, the goal is to perform a least-square method. The implementation returns a polynomial function of order $p$ (this can be a multi-variable function) that best fits the data.  
More formally, we have to find a polynomial function of order $p$: $F:\mathbb{R}^{k-m}\to\mathbb{R}^m$ that minimizes $\lVert F(a_1,a_2,...,a_{k-m})-(a_{k-m+1},a_{k-m+2},...,a_k)\rVert$, or $\lVert\sum_{d=0}^{p}\sum_{i\leq p}(c_ix_1^{i_1}x_2^{i_2}...x_{k-m}^{i_{k-m}})-(a_{k-m+1},a_{k-m+2},...,a_k)\rVert$. So the algorithm should find the parameters $c_0,c_1,...,c_l$, where $l=\sum_{d=0}^{p}\binom{d+(k-m)-1}{d}=\binom{p+k-m}{p}=$ the amount of terms in the sum.  
Examples of results:
1. A best-fit polynomial of degree 3 for 10 datapoints in $\mathbb{R}^2$ looks like
![Logo](test_2D.png)
2. A best-fit linear multi-variable function for 10 datapoints in $\mathbb{R}^3$ looks like
![Logo](test_3D.png)
3. A best-fit parametric linear function for 10 datapoints in $\mathbb{R}^3$ looks like
![Logo](test_parametrisation.png)
There are three functions implemented: one for the 2D-case, where a regular polynomial least-squares problem gets solved and a function $f:\mathbb{R}\to\mathbb{R}$ gets returned, a more general case where a function $f:\mathbb{R}^{k-1}\to\mathbb{R}$ gets returned and the most general case where a function $f:\mathbb{R}^{k-m}\to\mathbb{R}^m$ gets given.
