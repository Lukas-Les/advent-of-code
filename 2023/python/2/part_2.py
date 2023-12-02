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
    r, g, b = [], [], []
    for game in games:
        game = game.split(",")
        for item in game:
            count, color = item.strip().split(" ")
            count = int(count)
            if color == "red":
                r.append(count)
            elif color == "green":
                g.append(count)
            elif color == "blue":
                b.append(count)
    return max(r) * max(g) * max(b)


def handler():
    result = 0
    for line in load_input():
        game_id, games = parse_line(line)
        result += parse_games(games)
    return result


if __name__ == '__main__':
    print(handler())
