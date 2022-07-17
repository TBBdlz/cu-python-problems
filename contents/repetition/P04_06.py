"""
	P04-06: swap bracket notation
"""


def swap_bracket(sarg: str) -> None:
    for char in sarg:
        if char == '(':
            print('[', end='')
        elif char == ')':
            print(']', end='')

        elif char == '[':
            print('(', end='')
        elif char == ']':
            print(')', end='')
        else:
            print(char, end='')
    print()  # print new line character


if __name__ == '__main__':
    expression: str = input()
    swap_bracket(expression)
