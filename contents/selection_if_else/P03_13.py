"""
	P03-8: Biorhythm
"""
from contents.selection_if_else.P03_12 import get_day_in_year

bd, bm, by, d, m, y = [int(i) for i in input().split()]

day_total: int = 0
day_after_born: int = get_day_in_year(bd, bm, by)
day_total += day_after_born
