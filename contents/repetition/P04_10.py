"""
	P04-10: Run-Length Encoding
"""



enc_data: str = input()
encoding_pair: list = []

temp = enc_data[0]
counter = 0
for i in range(len(enc_data)):
	if i == len(enc_data) - 1:
		if temp == enc_data[i]:
			counter += 1
			encoding_pair.append((enc_data[i], counter))
		else:
			encoding_pair.extend(((temp, counter), (enc_data[i], 1)))
		continue

	if enc_data[i] == temp:
		counter += 1
	else:
		encoding_pair.append((temp, counter))
		temp = enc_data[i]
		counter = 1

for pair in encoding_pair:
	print(f'{pair[0]} {pair[1]}', end='')
	print(' ', end='')
print()