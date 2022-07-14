"""
	P04-04: approximation of sqrt(a) using bisection method
"""
import math

a: float = float(input())
# set L = 0, U = a
L = 0
U = a
answer_range = [L, U]
def mid(r): return (r[0] + r[1]) / 2


x: float = mid(answer_range)
while abs(a - x**2) > (math.pow(10, -10) * max(a, x**2)):
    if x**2 > a:
        answer_range[1] = x
    elif x**2 < a:
        answer_range[0] = x
    x = mid(answer_range)

print(f'{x:.6f}')
