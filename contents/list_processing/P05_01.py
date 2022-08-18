"""
	P05-01: Missing number
"""


def main() -> None:
	"""
	It takes a string as input, and prints the digits that are missing from the string
	"""
	input_arg: str = input()
	digits: list = [str(i) for i in range(10)]
	for char in input_arg:
		if char.isdigit() and ((char) in digits):
			digits.remove((char))
	print_result(digits)


def print_result(digits: list) -> None:
	"""
	It prints the digits in the list, separated by commas, or prints 'None' if the list is empty
	
	:param digits: list
	:type digits: list
	"""
	if not digits:
		print('None')
	else:
		print(','.join(digits))


if __name__ == '__main__':
	main()
