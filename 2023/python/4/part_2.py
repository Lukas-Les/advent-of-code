def load_input():
    with open("input.txt") as f:
        for line in f:
            yield line.strip()


def parse_line(line):
    card_id, line = line.split(":")
    card_id = card_id.replace("Card", "").strip()
    line = line.strip()
    lucky_numbers, my_numbers = line.split("|")
    lucky_numbers = lucky_numbers.strip()
    my_numbers = my_numbers.strip()
    lucky_numbers = lucky_numbers.split(" ")
    my_numbers = my_numbers.split(" ")
    return card_id, list(filter(None, lucky_numbers)), list(filter(None, my_numbers))


def get_wining_numbers(lucky_numbers, my_numbers):
    result = 0
    for number in my_numbers:
        if number in lucky_numbers:
            result += 1
    return result


cards = []


def handler():
    for line in load_input():
        card_id, lucky_numbers, my_numbers = parse_line(line)
        cards.append({
            "card_id": card_id,
            "wins": get_wining_numbers(lucky_numbers, my_numbers),
            "copies": 1
        })
    for i in range(0, len(cards)):
        wins = cards[i].get("wins")
        for j in range(1, wins + 1):
            cards[i + j]["copies"] += 1 * cards[i].get("copies")
    result = 0
    for card in cards:
        result += card.get("copies")

    return result


if __name__ == '__main__':
    print(handler())