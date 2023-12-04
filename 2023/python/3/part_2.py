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
                and idx < last_idx - 1
                and char.isnumeric()
                and not line[idx + 1].isnumeric()
        ):
            result.append((start, idx))
            start = None
        elif start is not None and idx == last_idx:
            result.append((start, idx))
    return result


def find_gear_center(line, _range):
    for i in range(*_range):
        try:
            if line[i] == "*":
                return len(line[:i])
        except IndexError:
            break


def is_part_number(number_location: tuple, line: str, last_idx: int, line_idx, line_above: str = None, line_bellow: str = None):
    search_range = (number_location[0] - 1, number_location[1] + 2)
    if number_location[0]:
        gear_center = find_gear_center(line, search_range)
        if gear_center:
            return gear_center, line_idx
    if number_location[1] != last_idx:
        gear_center = find_gear_center(line, search_range)
        if gear_center:
            return gear_center, line_idx
    if line_above:
        gear_center = find_gear_center(line_above, search_range)
        if gear_center:
            return gear_center, line_idx - 1
    if line_bellow:
        gear_center = find_gear_center(line_bellow, search_range)
        if gear_center:
            return gear_center, line_idx + 1
    return None, None


gear_registry = dict()


def handler():
    line_above = ""
    line = ""
    line_idx = -1
    for line_bellow in load_input():
        line_bellow = line_bellow.strip()
        if line:
            last_idx = len(line)
            numbers = locate_numbers(line, last_idx)
            for number in numbers:
                gear_center, find_in_line = is_part_number(number, line, last_idx, line_idx, line_above, line_bellow)
                if not gear_center:
                    continue
                gc_id = f"{find_in_line} {gear_center}"
                gear_number = line[number[0]: number[1] + 1]
                if gear_registry.get(gc_id):
                    gear_registry[gc_id].append(gear_number)
                else:
                    gear_registry[gc_id] = [gear_number]

        line_idx += 1
        line_above = line
        line = line_bellow

    result = 0
    for i in gear_registry.values():
        if len(i) > 1:
            result += int(i[0]) * int(i[1])

    return result


if __name__ == '__main__':
    print(handler())