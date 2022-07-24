"""
	P04-11: Zig-Zag or Zag-Zig
"""
from sys import maxsize


n: int = int(input())
min_zig = maxsize
max_zig = -maxsize
min_zag = maxsize
max_zag = -maxsize


for i in range(n):
	x, y = [int(e) for e in input().split()]
	if i % 2 == 0:
		min_zig = min(x, min_zig)
		max_zig = max(y, max_zig)
		min_zag = min(y, min_zag)
		max_zag = max(x, max_zag)
	else:
		min_zig = min(y, min_zig)
		max_zig = max(x, max_zig)
		min_zag = min(x, min_zag)
		max_zag = max(y, max_zag)

option = input()
if option.lower() == 'zig-zag':
	print(min_zig, max_zig)
elif option.lower() == 'zag-zig':
	print(min_zag, max_zag)
else:
	print('Invalid command')
	


