def load_input():
    with open("input.txt", "r") as f:
        for line in f.readlines():
            yield line
        yield "."


def locate_numbers(line: str, last_idx: int) -> list:
    result = []
    start = None
    for idx, char in enumerate(line):
        if start is None and char.isnumeric():
            start = idx
            continue
        if start and not char.isnumeric():
            result.append((start, start))
            start = None
            continue
        if (
                start is not None
                and idx != last_idx
                and char.isnumeric()
                and not line[idx + 1].isnumeric()
        ):
            result.append((start, idx))
            start = None
        elif start is not None and idx == last_idx:
            result.append((start, idx))
    return result


def is_part_label(char):
    if char == ".":
        return False
    return True


def check_in_other_lines(_range, line, last_idx):
    start = _range[0] - 1
    end = _range[1] + 2
    for i in range(start, end):
        if i < 0 or i > last_idx:
            continue
        try:
            if is_part_label(line[i]):
                return True
        except IndexError:
            return False


def is_part_number(number_location: tuple, line: str, last_idx: int, line_above: str = None, line_bellow: str = None):
    if number_location[0]:
        if is_part_label(line[number_location[0] - 1]):
            return True
    if number_location[1] != last_idx:
        if is_part_label(line[number_location[1] + 1]):
            return True
    if line_above:
        if check_in_other_lines(number_location, line_above, last_idx):
            return True
    if line_bellow:
        if check_in_other_lines(number_location, line_bellow, last_idx):
            return True


def handler():
    result = 0
    line_above = ""
    line = ""
    for line_bellow in load_input():
        line_bellow = line_bellow.strip()
        if line:
            last_idx = len(line) - 1
            numbers_locations = locate_numbers(line, last_idx)
            for num in numbers_locations:
                if is_part_number(
                    number_location=num,
                    line=line,
                    last_idx=last_idx,
                    line_above=line_above,
                    line_bellow=line_bellow,
                ):
                    result += int(line[num[0]:num[1] + 1])
        line_above = line
        line = line_bellow

    return result


if __name__ == '__main__':
    print(handler())
