"""
	P02-03: Date
"""
date_str: str = input()
# tuple and map function replaced line 7-9 code
date, month, year = tuple(map(int, date_str.split('/')))
# date = int(date)
# month = int(month)
# year = int(year)
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
print(f'{months[month - 1]} {date}, {year}')
