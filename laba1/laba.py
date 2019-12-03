import math
import time
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy.matrices import matrix_multiply_elementwise

np.random.seed(5)
eps = 1e-4
X = None
A = None
b = None
n = None
f = None


def fill_globals(size):
    global X, A, b, n, f
    n = size
    X = sp.MatrixSymbol('x', n, 1)
    A = np.random.rand(n, n) * 10
    A = sp.Matrix(A @ A.transpose())
    b = sp.Matrix(np.random.rand(n, 1))
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
    iterations = 0
    while True and iterations < 10000:
        x_prev = x_k
        x_k = x_k - (second_deriv().subs({X: x_k})**-1).evalf() * first_deriv().subs({X: x_k}).evalf()
        iterations += 1
        magnitude = mag(x_prev - x_k)
        if magnitude < eps:
            break

    print(x_k)
    print(f.subs({X: x_k}).evalf())


def mag(x):
    x = np.array(x, dtype=np.float64)
    return np.sqrt(np.sum([i**2 for i in x]))

def grad_method(n):
    print("Gradient")
    lamb = 0.001/n
    x_k = sp.Matrix(np.random.rand(n))
    iterations = 0
    while True and iterations < 10000:
        x_k_p1 = x_k - lamb * first_deriv().subs({X: x_k}).evalf()
        magnitude = mag(x_k_p1 - x_k)
        iterations +=1
        if iterations % 100 == 0:
            print(iterations)
            print(magnitude)
        if magnitude < eps:
            print(magnitude)
            print(x_k_p1)
            print(f.subs({X: x_k_p1}).evalf())
            break
        x_k = x_k_p1


if __name__ == '__main__':
    newtone_times = []
    grad_times = []
    number = 15
    x = []
    for n in range(1, number):
        print(n)
        x.append(n)
        fill_globals(n)
        start = time.time()
        newtone_method()
        end = time.time()
        newtone_method_elpsed = end - start
        print("Newtone method took {}".format(newtone_method_elpsed))

        start = time.time()
        grad_method(n)
        end = time.time()
        grad_method_elapsed = end - start
        print("Gradient method took {}".format(grad_method_elapsed))

        newtone_times.append(newtone_method_elpsed)
        grad_times.append(grad_method_elapsed)


    plt.title('N to time')
    plt.xlabel('N')
    plt.ylabel('Time')
    plt.plot(x, newtone_times, 'o-')
    plt.plot(x, grad_times, 'o-')
    plt.legend(['Newtone', 'Gradient'])
    plt.show()


