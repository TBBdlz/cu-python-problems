"""
	P01-04: Body surface area
			Calculate body surface area using
			Mosteller, Haycock, Boyd formula.
	Program input:
		weight[kg]: float
		height[cm]: float
	Program output:
		3 Body surface area value from 3 formulas
"""
from math import sqrt, log10, pow


def mosteller_formula(w: float, h: float) -> float:
    return sqrt(w * h) / 60


def haycock_formula(w: float, h: float) -> float:
    return 0.024265 * pow(w, 0.5378) * pow(h, 0.3964)


def boyd_formula(w: float, h: float) -> float:
    return 0.0333 * pow(w, 0.6157 - 0.0188 * log10(w)) * pow(h, 0.3)


if __name__ == '__main__':
    weight: float = float(input())
    height: float = float(input())
    print(mosteller_formula(weight, height))
    print(haycock_formula(weight, height))
    print(boyd_formula(weight, height))
