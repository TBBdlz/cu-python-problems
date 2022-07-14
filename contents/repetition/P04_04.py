"""
	P04-04: approximation of log10(a) using bisection method
"""
import math

a: float = float(input())
# set L = 0, U = a
L = 0
U = a
answer_range = [L, U]
def mid(r): return (r[0] + r[1]) / 2


x: float = mid(answer_range)
while abs(a - math.pow(10, x)) > (math.pow(10, -10) * max(a, math.pow(10, x))):
    if math.pow(10, x) > a:
        answer_range[1] = x
    elif math.pow(10, x) < a:
        answer_range[0] = x
    x = mid(answer_range)

print(f'{x:.6f}')
