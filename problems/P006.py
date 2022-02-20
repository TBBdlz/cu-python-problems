monthEnum: dict[str, int] = {'January': 1, 'February': 2, 'March': 3, 'April': 4,
                             'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9,
                             'October': 10, 'November': 11, 'December': 12}

name1, monthStr1, date1, byear1 = input().split()
month1 = monthEnum[monthStr1]
date1 = date1.replace(',', '')
date1 = int(date1)
byear1 = int(byear1)

name2, monthStr2, date2, byear2 = input().split()
month2 = monthEnum[monthStr2]
date2 = date2.replace(',', '')
date2 = int(date2)
byear2 = int(byear2)

if byear1 < byear2:
    print(name1)
elif byear1 == byear2:
    if (
        month1 >= month2
        and month1 == month2
        and date1 < date2
        or month1 > month2
    ):
        print(name1)
    elif month1 == month2 and date1 == date2:
        print(name1, name2)
    else:
        print(name2)
else:
    print(name2)
