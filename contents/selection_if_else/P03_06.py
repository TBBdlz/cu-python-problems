# sourcery skip: de-morgan, merge-duplicate-blocks, merge-else-if-into-elif, remove-redundant-if
"""
	P03-06: Changing department
"""

grade_mapping = {
    'A': 4.0,
    'B+': 3.5,
    'B': 3.0,
    'C+': 2.5,
    'C': 2.0,
    'D+': 1.5,
    'D': 1.0,
    'F': 0.0
}

idX, gpaxX, com_gpaX, cal1_gpaX, cal2_gpaX = list(input().split())
gpaxX = float(gpaxX)
idY, gpaxY, com_gpaY, cal1_gpaY, cal2_gpaY = list(input().split())
gpaxY = float(gpaxY)
cal1_gpaX: float = grade_mapping[cal1_gpaX]
cal1_gpaY: float = grade_mapping[cal1_gpaY]
cal2_gpaX: float = grade_mapping[cal2_gpaX]
cal2_gpaY: float = grade_mapping[cal2_gpaY]

first_condX: bool = com_gpaX == 'A' and cal1_gpaX >= 2 and cal2_gpaX >= 2
first_condY: bool = com_gpaY == 'A' and cal1_gpaY >= 2 and cal2_gpaY >= 2

if not (first_condX or first_condY):
    print(None)
elif first_condX and not first_condY:
    print(idX)
elif not first_condX and first_condY:
    print(idY)
elif first_condX and first_condY:
    if gpaxX > gpaxY:
        print(idX)
    elif gpaxX < gpaxY:
        print(idY)
    else:
        if cal1_gpaX > cal1_gpaY:
            print(idX)
        elif cal1_gpaX < cal1_gpaY:
            print(idY)
        else:
            if cal2_gpaX > cal2_gpaY:
                print(idX)
            elif cal2_gpaX < cal2_gpaY:
                print(idY)
            else:
                print('Both')
