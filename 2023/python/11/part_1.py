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
    galaxies_keys = list(galaxies.keys())
    for i in range(len(galaxies) - 1):
        galaxy_id = galaxies_keys[i]
        for j in range(1 + i, len(galaxies)):
            next_galaxy_id = galaxies_keys[j]
            g1_x = galaxy_id[0]
            g1_y = galaxy_id[1]
            g2_x = next_galaxy_id[0]
            g2_y = next_galaxy_id[1]
            galaxies[galaxies_keys[i]].append((next_galaxy_id, abs(g2_x - g1_x) + abs(g2_y - g1_y)))
    result = 0
    for i in galaxies.values():
        for j in i:
            result += j[1]

    return result


if __name__ == '__main__':
    print(handler())