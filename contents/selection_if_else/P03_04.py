"""
	P03-04: Dicision workflow
"""

a, b, c, d = [int(i) for i in input().split()]
if a > b:
	a, b = b, a
	if d >= a:
		if c >= d:
			c -= a
	else:
		c += a
	b = a + c + d
else:
	if c >= a >= b:  # yes python can do this
		d += a
	if d >= c:
		b += 2
	else:
		b *= 2
print(f'{a} {b} {c} {d}')
