"""
	P04-08: Draw triangle with height: h
"""

print_star = lambda: print('*', end='')
print_space = lambda: print(' ', end='')
def draw_triangle(height: int) -> None:
    for i in range(height):
        for j in range(2*height-1):
            if i == 0:
                if j == height-1:
                    print_star()
                else:
                    print_space()
            elif i < h-1:
                if j in {height-i-1, height+i-1}:
                    print_star()
                else:
                    print_space()
            elif i == height-1:
                print('*', end='')
        print()


if __name__ == '__main__':
	h: int = int(input())
	draw_triangle(h)