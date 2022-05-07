# from typing import Callable

# import scipy.misc
# import scipy.optimize

# from dsalgo.type import Numeric


def binary_search() -> None:
    ...


def ternary_search() -> None:
    ...


# def find_root_newton(
#     y: Numeric,
#     n=2,
#     x0=1.0,
#     tol: float = 1e-8,
# ):
#     def f(x):
#         return x**n - y

#     return newton_(f, x0, tol)


# def newton_(
#     f: Callable,
#     x0: Numeric,
#     tol: float = 1e-8,
# ):
#     x = x0
#     while abs(f(x)) > tol:
#         der = scipy.misc.derivative(
#             func=f,
#             x0=x,
#             dx=tol,
#         )
#         x -= f(x) / der

#     return x
