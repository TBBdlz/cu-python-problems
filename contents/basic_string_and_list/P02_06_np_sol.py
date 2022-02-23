"""
	P02-06: Alternative solution using numpy
"""
import numpy as np
u: np.ndarray = np.array(input()[1:-1].split(', '), dtype=np.float32)
v: np.ndarray = np.array(input()[1:-1].split(', '), dtype=np.float32)
w: np.ndarray = u + v

print(f'{u} + {v} = {w}')
