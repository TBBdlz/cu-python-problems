"""
	P05-05: Amount of difference data
"""

# you can do the sort -> count method
# but if we have plenty of space we should use set method
def main() -> None:
	data: list[int] = [int(k) for k in input().split()]
	dset: set[int] = set(data)
	print(len(dset))
	print(dset)


if __name__ == '__main__':
	main()