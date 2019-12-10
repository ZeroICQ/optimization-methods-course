import time
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

np.random.seed(5)
eps = 1e-4
X = None
A = None
b = None
n = None
f_0 = None
c = None
d = None


def fill_globals(size):
    global X, A, b, n, f_0, n, c, d
    n = size
    X = sp.MatrixSymbol('x', n, 1)
    A = np.random.randint(1, 5, (n, n))
    A = A @ A.transpose()
    sp_A = sp.Matrix(A)
    b = np.random.randint(1, 10, (n, 1))
    sp_b = sp.Matrix(b)
    f_0 = (0.5 * (X.T * sp_A * X))[0] + sp_b.dot(sp.Matrix(X))
    c = np.random.randint(1, 10, (n, 1))
    d = np.random.randint(1, 10, (n, 1))


if __name__ == '__main__':
    fill_globals(6)
    # y=0
    x = np.linalg.inv(-A)@b
    f_0.subs({X: x})
    print("Solution for y=0")
    print(x)
    print(f_0.subs({X: sp.Matrix(x)}))
    # y > 0
    print("Solution for y>0")
    y = (d - (c.transpose()@np.linalg.inv(A)@b))/(c.transpose()@np.linalg.inv(A)@c)
    x = -np.linalg.inv(A)@(b+y.transpose()@c)
    print(x)
    print(f_0.subs({X: sp.Matrix(x)}).evalf())
