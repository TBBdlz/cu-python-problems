from typing import List, Tuple, Union


def is_valid_input(input_str: str) -> bool:
    try:
        x, y = map(int, input_str.split())
        return True
    except ValueError:
        return False


def process_input(input_str: str, start_left_array: List[int], start_right_array: List[int]) -> None:
    if not is_valid_input(input_str):
        print('Invalid input')
        exit()

    x, y = map(int, input_str.split())
    start_left_array.append(x)
    start_right_array.append(y)


def get_min_max_values(start_left_array: List[int], start_right_array: List[int]) -> Tuple[int, int]:
    return min(start_left_array), max(start_right_array)


def add_to_arrays(x: int, y: int, start_left_array: List[int], start_right_array: List[int], count: int) -> int:
    if count % 2 == 0:
        start_left_array.append(y)
        start_right_array.append(x)
    else:
        start_left_array.append(x)
        start_right_array.append(y)
    return count + 1


def process_helix_input() -> None:
    start_left_array: List[int] = []
    start_right_array: List[int] = []
    count: int = 0

    initial_input: str = input()
    process_input(initial_input, start_left_array, start_right_array)

    while True:
        raw_input: str = input()
        if raw_input.lower() == 'zig-zag':
            min_val, max_val = get_min_max_values(
                start_left_array, start_right_array)
            print(min_val, max_val)
            break
        elif raw_input.lower() == 'zag-zig':
            min_val, max_val = max(start_left_array), min(start_right_array)
            print(min_val, max_val)
            break
        elif is_valid_input(raw_input):
            x, y = map(int, raw_input.split())
            count = add_to_arrays(x, y, start_left_array,
                                  start_right_array, count)
        else:
            print('Invalid input')
            exit()


if __name__ == '__main__':
    process_helix_input()
