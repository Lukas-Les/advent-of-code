import math


def load_input():
    with open("input.txt") as f:
        return [list(i) for i in f.read().split("\n")]


GALAXY = "#"


def expand_space(space):
    x_to_expand = []
    y_to_expand = []
    for x in range(len(space[0])):
        found = False
        for y in range(len(space)):
            if GALAXY in space[y][x]:
                found = True
                break
        if not found:
            x_to_expand.append(x)
    for y in range(len(space)):
        if GALAXY not in space[y]:
            y_to_expand.append(y)

    for x in x_to_expand:
        for y in range(len(space)):
            space[y].insert(x, ".")
    for y in y_to_expand:
        space.insert(y, ["."] * len(space[0]))

    return space


def handler():
    space = expand_space(load_input())
    galaxies = dict()
    space_width = len(space[0])
    for y in range(len(space)):
        for x in range(space_width):
            if space[y][x] == GALAXY:
                galaxies[(x, y)] = []

    for i in range(len(galaxies)):
        for j in range(1, len(galaxies)):
            g1_x = list(galaxies.keys())[i][0]
            g1_y = list(galaxies.keys())[i][1]
            g2_x = list(galaxies.keys())[j][0]
            g2_y = list(galaxies.keys())[j][1]
            if g1_y == 0:
                g1_y = 1
            if g2_y == 0:
                g2_y = 1
            a = abs(g2_x - g1_x)
            b = abs(g2_y - g1_y)
            r = a + b
            a = 1

    return space


if __name__ == '__main__':
    print(handler())