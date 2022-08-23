num_lst: list = []
n: int = int(input())

state = True


def flip_state():
    global state
    state = not (state)


for _ in range(n):
    if state:
        num_lst.append(int(input()))
    else:
        num_lst = [int(input())] + num_lst
    flip_state()
print('Finished first for loop')
data_lst = [int(k) for k in input().split()]
for elem in data_lst:
    if state:
        num_lst.append(elem)
    else:
        num_lst = [elem] + num_lst
    flip_state()

temp = 0
while True:
	temp = int(input())
	if temp == -1:
		break
	elif state:
		num_lst.append(temp)
	else:
		num_lst = [temp] + num_lst
	flip_state()

print(num_lst)
