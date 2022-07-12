subscribers: int = int(input())
if subscribers < 1_000:
	print(subscribers)
elif subscribers < 1_000_000:
	print(f'{round(subscribers / 1_000, 1)}K')
elif subscribers < 1_000_000_000:
	print(f'{round(subscribers / 1_000_000, 1)}M')
else: # assuming user type number greater than 0
	print(f'{round(subscribers / 1_000_000_000, 1)}B')