"""
	P03-07: day number
"""

d: int = int(input())
m: int = int(input())
y: int = int(input())


def get_day_in_year(dx, mx, yx):
    days_in_month: list = [[1, 31], [2, 28], [3, 31], [4, 30],
                           [5, 31], [6, 30], [7, 31], [8, 31],
                           [9, 30], [0, 31], [1, 30], [2, 31]]

    # check if it is leapyear
    ac = yx - 543  # BC
    if ac % 400 == 0:
        days_in_month[1][1] = 29
    elif ac % 4 == 0 and ac % 100 != 0:
        days_in_month[1][1] = 29

    num_days: int = 0
    if mx != 1:
        for i in range(m-1):
            num_days += days_in_month[i+1][1]
        num_days += dx
    else:
        num_days = dx
    return num_days


print(get_day_in_year(d, m, y))
