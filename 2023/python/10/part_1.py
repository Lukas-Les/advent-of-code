def load_input():
    with open("input.txt", "r") as f:
        return f.read().split("\n")


N = (0, -1)
E = (1, 0)
S = (0, 1)
W = (-1, 0)


pipes_map = {
    "|": [N, S],
    "-": [W, E],
    "L": [N, E],
    "J": [N, W],
    "7": [S, W],
    "F": [S, E],
}
pipes_keys = tuple(pipes_map.keys())


def find_start_pos(ground):
    for y, line in enumerate(ground):
        for x, char in enumerate(line):
            if char == "S":
                return x, y


def move(current_pos: tuple, direction: tuple) -> tuple:
    return current_pos[0] + direction[0], current_pos[1] + direction[1]


def is_pipe_connected(pipe, pipes_c, current_pos):
    for direction in pipes_map[pipe]:
        if move(pipes_c, direction) == current_pos:
            return True
    return False


def show_symbol(ground, cords):
    return ground[cords[1]][cords[0]]


def find_next_pipes(ground, current_pos, current_pipe=None, previous_pos=None, step=0):
    step += 1
    result = []
    directions = pipes_map[current_pipe] if current_pipe else [N, E, S, W]

    for direction in directions:
        looking_at_c = move(current_pos, direction)
        looking_at_s = show_symbol(ground, looking_at_c)
        if (
                looking_at_c != previous_pos
                and looking_at_s in pipes_keys
                and is_pipe_connected(looking_at_s, looking_at_c, current_pos)
        ):
            result.append((looking_at_c, looking_at_s, current_pos, step))
    return result


def handler():
    weights = dict()
    ground = load_input()
    current_pos = find_start_pos(ground)
    weights[current_pos] = 0
    next_pipes = find_next_pipes(ground=ground, current_pos=current_pos)
    while next_pipes:
        pipes = next_pipes
        next_pipes = []
        for pipe in pipes:
            pipes_weight = weights.get(pipe[0])
            if pipes_weight and pipes_weight < pipe[3]:
                continue
            next_pipes.extend(find_next_pipes(
                ground=ground,
                current_pos=pipe[0],
                current_pipe=pipe[1],
                previous_pos=pipe[2],
                step=pipe[3],
            ))
        for np in next_pipes:
            if not weights.get(np[0]):
                weights[np[2]] = np[3]
    return max(weights.values())


if __name__ == '__main__':
    print(handler())
