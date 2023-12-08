def load_input():
    with open('input.txt') as f:
        return f.read().split("\n\n")


def move(current_pos, instructions, steps, maze):
    for i in instructions:
        steps += 1
        match i:
            case "R":
                current_pos = maze[current_pos][1]
            case "L":
                current_pos = maze[current_pos][0]
        if current_pos == "ZZZ":
            return current_pos, steps
    return current_pos, steps


def handler():
    instructions, text = load_input()
    raw_maze = text.split("\n")
    maze = dict()
    for line in raw_maze:
        idx, line = line.split("=")
        left, right = line.split(",")
        maze[idx.strip()] = (left.replace("(", "").strip(), right.replace(")", "").strip())
    current_pos = "AAA"
    steps = 0
    while current_pos != "ZZZ":
        current_pos, steps = move(current_pos, instructions, steps, maze)
    return steps


if __name__ == '__main__':
    print(handler())