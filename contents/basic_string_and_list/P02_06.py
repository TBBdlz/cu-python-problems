"""
	P02-06: Sum of 3 dimentional vectors
"""

u: list[float] = list(map(float, (input()[1:-1].split(', '))))
v: list[float] = list(map(float, (input()[1:-1].split(', '))))
# w = u + v using list comperhension
w: list[float] = [u[i] + v[i] for i in range(len(u))]

print(f'{u} + {v} = {w}')
