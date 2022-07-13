"""
	P04-03: Find average value from standard inputs.
"""

counter: int = 0
total: int = 0

arg = input()
while arg != 'q':
    counter += 1
    total += float(arg)
    arg = input()

if counter == 0:
	print('No Data')
else:
	print(total / counter)
