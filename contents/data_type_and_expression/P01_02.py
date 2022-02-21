"""
	P01-02: Approximation of n!
"""
from math import pow, sqrt, exp, pi

n: int = int(input())


def factorial_boundary(n: int) -> float:
    lower_bound: float = sqrt(2 * pi) * pow(n, n + 0.5) * \
        exp(-n + 1 / (12 * n + 1))
    upper_bound: float = sqrt(
        2 * pi) * pow(n, n + 0.5) * exp(-n + 1 / (12 * n))
    return lower_bound, upper_bound


lower_bound, upper_bound = factorial_boundary(n)
print(lower_bound)
print(upper_bound)
