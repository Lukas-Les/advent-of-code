def load_input():
    with open("input.txt", "r") as f:
        text = f.readlines()
        time, distance = 0, 0
        for line in text:
            if line.startswith("Time"):
                time = line.split(":")[1].replace(" ", "")
            elif line.startswith("Distance:"):
                distance = line.split(":")[1].replace(" ", "")
        return int(time), int(distance)


def handler():
    time, distance = load_input()
    w = 0
    for time_holding in range(1, time):
        traveled_distance = (time - time_holding) * time_holding
        if traveled_distance > distance:
            w += 1
    return w


if __name__ == '__main__':
    print(handler())
