"""
	P03-08: Mobile telephone number
"""
mobile_num_data: str = input()

if len(mobile_num_data) != 10:
    print('Not a mobile number')
elif mobile_num_data[:2] in {'06', '08', '09'}:
	print('Mobile number')
else:
	print('Not a mobile number')