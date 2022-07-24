"""
	P04-11: but using list
"""

n: int = int(input())
red_lst: list = [0] * n
blue_lst: list = [0] * n

for i in range(n):
	x, y = [int(e) for e in input().split()]
	if i % 2 == 0:
		red_lst[i] = x
		blue_lst[i] = y
	else:
		red_lst[i] = y
		blue_lst[i] = x

command: str = input()
if command.lower() == 'zig-zag':
	print(min(red_lst), max(blue_lst))
elif command.lower() == 'zag-zig':
	print(min(blue_lst), max(red_lst))