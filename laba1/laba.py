import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy.matrices import matrix_multiply_elementwise

n = 6
np.random.seed(0)
X = sp.MatrixSymbol('x', 6, 1)
A = np.random.rand(n, n) * 10
A = sp.Matrix(A @ A.transpose())
b = sp.Matrix(np.random.rand(6, 1))

f = (0.5 * (X.T * sp.Matrix(A) * X))[0] + b.dot(sp.Matrix(X))


def second_deriv():
    result = []
    for i in range(n):
        result.append([])
        for j in range(n):
            result[i].append(f.diff(X[i]).diff(X[j]))
    return sp.Matrix(result)


def first_deriv():
    result = []
    for i in range(n):
        result.append(f.diff(X[i]))
    return sp.Matrix(result)


if __name__ == '__main__':
    x_k = sp.Matrix(np.random.rand(n))

    # print("end")
    # val = f.subs({X: x_k})
    # print(val.evalf())

    for i in range(10):
        print(i)
        x_k = x_k - (second_deriv().subs({X: x_k})**-1).evalf() * first_deriv().subs({X: x_k}).evalf()


    print(x_k)
    print(f.subs({X: x_k}).evalf())
