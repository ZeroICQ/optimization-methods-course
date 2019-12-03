import math
import timeit
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy.matrices import matrix_multiply_elementwise

n = 6
np.random.seed(5)
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


def newtone_method():
    print("Newton")
    x_k = sp.Matrix(np.random.rand(n))
    for i in range(10):
        x_k = x_k - (second_deriv().subs({X: x_k})**-1).evalf() * first_deriv().subs({X: x_k}).evalf()

    print(x_k)
    print(f.subs({X: x_k}).evalf())


def mag(x):
    return math.sqrt(sum(i**2 for i in x))

def grad_method():
    print("Gradient")
    lamb = 0.001
    eps = 1e-5
    x_k = sp.Matrix(np.random.rand(n))

    while True:
        x_k_p1 = x_k - lamb * first_deriv().subs({X: x_k}).evalf()
        magnitude = mag(x_k_p1 - x_k)
        # print(magnitude)
        if magnitude < eps:
            print(magnitude)
            print(x_k_p1)
            print(f.subs({X: x_k_p1}).evalf())
            break
        x_k = x_k_p1


if __name__ == '__main__':
    start = timeit.timeit()
    newtone_method()
    end = timeit.timeit()
    print(end - start)

    start = timeit.timeit()
    grad_method()
    end = timeit.timeit()
    print(end - start)