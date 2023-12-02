class Color:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit


red = Color("red", 12)
green = Color("green", 13)
blue = Color("blue", 14)


def load_input():
    with open("input.txt", "r") as f:
        for line in f.readlines():
            yield line


def parse_line(line):
    game_id, line = line.split(":")
    game_id = game_id.replace("Game ", "")
    games = line.split(";")
    return game_id, games


def parse_games(games):
    for game in games:
        items = game.strip().split(",")
        r, g, b = 0, 0, 0
        for i in items:
            count, color = i.strip().split(" ")
            count = int(count)
            if color == red.name:
                r = count
            elif color == green.name:
                g = count
            elif color == blue.name:
                b = count

            if any([
                r > red.limit,
                g > green.limit,
                b > blue.limit
            ]):
                return False
    return True


def handler():
    result = 0
    for line in load_input():
        game_id, games = parse_line(line)
        if parse_games(games):
            result += int(game_id)
    return result


if __name__ == '__main__':
    print(handler())