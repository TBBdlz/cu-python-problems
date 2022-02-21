"""
	P01-01: Weird formula
"""
import math

p: float = math.pi - math.factorial(10) / math.pow(8, 8) + math.pow(math.log(9.7), 7 /
                                                                    math.sqrt(71) - math.sin(math.radians(40)))
q: float = math.pow(1.2, math.pow(2.3, 1/3))
result: float = p / q

print(f'{result:.6f}')
