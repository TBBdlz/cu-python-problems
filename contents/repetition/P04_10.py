"""
	P04-10: Run-Length Encoding
"""



enc_data: str = input()

temp = enc_data[0]
counter = 1
for char in enc_data[1:]:
	if char == temp:
		counter += 1
	else:
		print(temp, counter, end=' ')
		temp = char
		counter = 1
print(temp, counter)