"""
	P01-03: Find root of quadratic equation ax^2 + bx + c = 0
			using x = (-b +/- sqrt(b^2 - 4ac)) / 2a formula
	Program input:
		a: float
		b: float
		c: float
		a, b, c represent coefficients in quadratic equation
	Program output:
		roots of quadratic equation
"""
from math import sqrt


a = float(input())
b = float(input())
c = float(input())


def solve_quadratic(a: float, b: float, c: float) -> tuple:
	"""
	Given the coefficients of a quadratic equation in standard form, return the two roots of the
	equation
	
	:param a: the coefficient of the x^2 term
	:type a: float
	:param b: the y-intercept of the line
	:type b: float
	:param c: the coefficient of the quadratic term
	:type c: float
	:return: a tuple of two values.
	"""
	delta = sqrt(b ** 2 - 4 * a * c)
	return (-b - delta) / (2*a), (-b + delta) / (2*a)


x1, x2 = solve_quadratic(a, b, c)

print(x1, x2)
