"""
	P03-05: CU Faculty number
"""
import sys

faculty_numbers: list[int] = [1, 2, 20, 21, 22, 23, 24,
                              25, 26, 27, 28, 29, 30, 31,
                              32, 33, 34, 35, 36, 37, 38,
                              39, 40, 51, 53, 55, 58]


def check_fac_no(msg: str) -> str:
    """
    It checks if the given message is a valid faculty number and prints the result to the standard
    output

    :param msg: str - the message that the user has entered
    :type msg: str
    :return: the string 'OK' or 'Error'
    """
    global faculty_numbers
    if len(msg) != 2:
        print('Error', file=sys.stderr)
        return

    if int(msg) in faculty_numbers:
        print('OK')
    else:
        print('Error', file=sys.stderr)


def main() -> None:
    """
    It takes a string as input, and checks if it is a factorion number
    """
    input_msg = input()
    check_fac_no(input_msg)


if __name__ == '__main__':
    main()
