import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy.matrices import matrix_multiply_elementwise


n = 6
X = sp.MatrixSymbol('x', 6, 1)
A = np.random.rand(n, n) * 10
A = sp.Matrix(A @ A.transpose())
# b = sp.Matrix(np.random.rand(n,)
b = sp.Matrix(np.random.rand(6, 1))

# f = 0.5 * (X.T * sp.Matrix(A) * X) + sp.Matrix([b.dot(sp.Matrix(X))])
f = b.dot(sp.Matrix(X))

def is_pos_def(x):
    return np.all(np.linalg.eigvals(x) > 0)


if __name__ == '__main__':
    # print("is A spd: " + str(is_pos_def(A)))
    x = np.random.rand(n)
    ll = sp.diff(f, X)
    print("f(x) is" + str(ll))
    #
    # x = np.random.rand(6)
    # for i in range(10):
    #     x = x - sp.diff(f, X, 2).I.subs(x).evalf() * sp.diff(f, X).subs(x).evalf()
