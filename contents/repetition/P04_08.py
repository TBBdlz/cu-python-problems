"""
	P04-08: Draw triangle with height: h
"""

print_star = lambda: print('*', end='')
print_space = lambda: print(' ', end='')
def draw_triangle(height: int) -> None:
    for y in range(height):
        for x in range(2*height-1):  # (x, y) is coordinates in the plane
            if y == 0:
                if x == height-1:
                    print_star()
                else:
                    print_space()
            elif y < h-1:
                if x in {height-y-1, height+y-1}:
                    print_star()
                else:
                    print_space()
            elif y == height-1:
                print('*', end='')
        print()


if __name__ == '__main__':
	h: int = int(input())
	draw_triangle(h)