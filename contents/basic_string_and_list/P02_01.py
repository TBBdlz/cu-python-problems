"""
	P02-01: ID number
"""


def last_digit(id_str: str) -> int:
    sum_part: int = sum((13 - i) * int(id_str[i]) for i in range(12))
    return (11 - sum_part % 11) % 10


if __name__ == '__main__':
    id_num: str = input()
    n12: int = last_digit(id_num)
    print(f'{id_num[0]} {id_num[1:5]} {id_num[5:10]} {id_num[10:12]} {n12}')
