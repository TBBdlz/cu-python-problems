expression: str = input()

for char in expression:
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
print()
