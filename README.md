Given a $n\times k$ matrix whose rows represent points in $\mathbb{R}^k$ and an integer $p$, this function calculates the best-fit parameters for the return function $f:\mathbb{R}^{k-m}\to \mathbb{R}^m$ with for each $f_i$ having its polynomial order equal to $p$.
Examples of results:
1. A best-fit quadratic polynomial for 10 datapoints in $\mathbb{R}^2$ looks like
![Logo](test_2D.png)
2. A best-fit quadratic multi-variable polynomial for 10 datapoints in $\mathbb{R}^3$ looks like
![Logo](test_3D.png)
3. A best-fit parametric linear function for 10 datapoints in $\mathbb{R}^3$ looks like
![Logo](test_parametrisation.png)
There are three functions implemented: one for the 2D-case, where a regular polynomial least-squares problem gets solved and a function $f:\mathbb{R}\to\mathbb{R}$ gets returned, a more general case where a function $f:\mathbb{R}^{k-1}\to\mathbb{R}$ gets returned and the most general case where a function $f:\mathbb{R}^{k-m}\to\mathbb{R}^m$ gets given.
