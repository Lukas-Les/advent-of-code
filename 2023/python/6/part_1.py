def load_input():
    with open("input.txt", "r") as f:
        text = f.readlines()
        times, distances = [], []
        for line in text:
            if line.startswith("Time"):
                times.extend([int(i) for i in line.split(":")[1].strip().split(" ") if i])
            elif line.startswith("Distance:"):
                distances.extend([int(i) for i in line.split(":")[1].strip().split(" ") if i])
        for item in zip(times, distances):
            yield item


def count_ways(time, distance):
    w = 0
    for time_holding in range(1, time):
        traveled_distance = (time - time_holding) * time_holding
        if traveled_distance > distance:
            w += 1
    return w


def handler():
    result = 1
    for i in load_input():
        result *= count_ways(*i)
    return result


if __name__ == '__main__':
    print(handler())
