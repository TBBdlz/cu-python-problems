"""
	P03-09: plus, minus, even, odd
"""
n: int = int(input())

if n > 0:
    print('positive')
elif n == 0:
    print('zero')
else:
    print('negative')

if n % 2 == 0:
    print('even')
else:
    print('odd')
