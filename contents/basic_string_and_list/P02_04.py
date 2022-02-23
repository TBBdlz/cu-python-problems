"""
	P02-04: Leading zeros
"""

if __name__ == '__main__':
    m: int = int(input())
    n: int = int(input())
    print('0' * (n - len(str(m))) + str(m))
