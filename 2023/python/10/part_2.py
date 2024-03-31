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


def mark(ground, position):
    str_as_arr = list(ground[position[1]])
    str_as_arr[position[0]] = "#"
    ground[position[1]] = "".join(str_as_arr)


def find_next_pipes(ground, current_pos, current_pipe=None, previous_pos=None, step=0):
    step += 1
    directions = pipes_map[current_pipe] if current_pipe else [N, E, S, W]

    for direction in directions:
        looking_at_c = move(current_pos, direction)
        looking_at_s = show_symbol(ground, looking_at_c)
        if (
                looking_at_c != previous_pos
                and looking_at_s in pipes_keys
                and is_pipe_connected(looking_at_s, looking_at_c, current_pos)
        ):
            return looking_at_c, looking_at_s, current_pos, step


def handler():
    weights = dict()
    ground = load_input()
    current_pos = find_start_pos(ground)
    weights[current_pos] = 0
    next_pipe = find_next_pipes(ground=ground, current_pos=current_pos)
    while next_pipe:
        mark(ground, current_pos)
        current_pos = next_pipe[0]
        current_pipe = next_pipe[1]
        previous_pos = next_pipe[2]
        step = next_pipe[3]
        next_pipe = find_next_pipes(
            ground=ground,
            current_pos=current_pos,
            current_pipe=current_pipe,
            previous_pos=previous_pos,
            step=step,
        )
    result = 0
    top, bottom = False, False
    for line in ground:
        start = None
        end = None
        for i in range(len(line)):
            if line[i] == "X":
                start = i
                break
        for i in range(0, len(line), -1):
            if line[i] == "X":
                end = i
                break
        if start is not None and end is not None:
            pass

if __name__ == '__main__':
    print(handler())
