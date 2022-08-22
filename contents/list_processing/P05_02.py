table = [
	('Robert', 'Dick'),
	('William', 'Bill'),
	('James', 'Jim'),
	('John', 'Jack'),
	('Margaret', 'Peggy'),
	('Edward', 'Ed'),
	('Sarah', 'Sally'),
	('Andrew','Andy'),
	('Anthony', 'Tony'),
	('Deborah', 'Debbie')
]

def process_data(name):
	for pair in table:
		if name == pair[0]:
			print(pair[1])
			return
		elif name == pair[1]:
			print(pair[0])
			return
	print('Not found')


n: int = int(input())
name_lst: list = []
for _ in range(n):
	name = input()
	name_lst.append(name)

for i in range(n):
	process_data(name_lst[i])
	
