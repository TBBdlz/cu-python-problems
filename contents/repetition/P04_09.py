"""
	P04-09: Bisection (2nd method)
			Using bisection method to approximate log10(a)
"""

a: float = float(input())
L: float = 0
U: float = 0
x: float = 10 // a

while x != 0:
	x //= a
	U += 1

ans_range: list[float] = [L, U]