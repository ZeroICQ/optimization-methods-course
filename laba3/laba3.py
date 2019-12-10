'''
f_0 = 0.5 * x^T * A * x + b^T * x
f = ||x - x_0 || - z <= 0, z - радиус, x_0 - центр
f^2 =  ||x - x_0 ||^2 - z^2 <= 0

L(x, y) = 0.5 * x^T * A * x + b^T * x + y * (||x - x_0 ||^2 - z^2 )

1. y > 0

Ax + b + 2y(x - x_0) = 0
||x - x_0||^2 = r^2

'''

import time
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

np.random.seed(5)
X = None
A = None
b = None
n = None
f_0 = None
x_0 = None
r = None


def fill_globals(size):
    global X, A, b, n, f_0, n, x_0, r
    n = size
    X = sp.MatrixSymbol('x', n, 1)
    A = np.random.randint(1, 5, (n, n))
    A = A @ A.transpose()
    sp_A = sp.Matrix(A)
    b = np.random.randint(1, 10, (n, 1))
    sp_b = sp.Matrix(b)
    f_0 = (0.5 * (X.T * sp_A * X))[0] + sp_b.dot(sp.Matrix(X))
    x_0 = np.random.randint(1, 10, (n, 1))
    r = np.random.randint(1, 10, (n, 1))


if __name__ == '__main__':
    fill_globals(6)

    x = np.linalg.solve(-x_0, r)
    print(np.allclose(np.dot(-x_0, x), b))

