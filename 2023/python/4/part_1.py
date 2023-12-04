def load_input():
    with open("input.txt") as f:
        for line in f:
            yield line.strip()


def parse_line(line):
    car_id, line = line.split(":")
    line = line.strip()
    lucky_numbers, my_numbers = line.split("|")
    lucky_numbers = lucky_numbers.strip()
    my_numbers = my_numbers.strip()
    lucky_numbers = lucky_numbers.split(" ")
    my_numbers = my_numbers.split(" ")
    return car_id, list(filter(None, lucky_numbers)), list(filter(None, my_numbers))


def calculate_score(total_matches):
    if total_matches == 0:
        return 0
    total_score = 0
    for i in range(1, total_matches + 1):
        if total_score < 2:
            total_score += 1
            continue
        total_score = total_score * 2
    return total_score


def handler():
    result = 0
    for line in load_input():
        winners = []
        car_id, lucky_numbers, my_numbers = parse_line(line)
        for lucky_number in lucky_numbers:
            if lucky_number in my_numbers:
                winners.append(lucky_number)
        if winners:
            result += calculate_score(len(winners))
    return result


if __name__ == '__main__':
    print(handler())
