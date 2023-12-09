def load_input():
    with open("input.txt", "r") as f:
        for l in f.readlines():
            yield l.strip()


def make_arr_of_diffs(arr):
    last_arr = arr[-1]
    if not any(last_arr):
        return arr
    new_arr = []
    for i in range(len(last_arr) - 1):
        new_arr.append(last_arr[i + 1] - last_arr[i])
    arr.append(new_arr)
    return make_arr_of_diffs(arr)


def fill_placeholders(arr):
    result = 0
    arr = arr[::-1]
    last_idx = len(arr)
    for i in range(last_idx):
        if not any(arr[i]):
            arr[i].append(0)
            continue
        r = arr[i][-1] + arr[i -1][-1]
        if i == last_idx - 1:
            result = r
        arr[i].append(r)
    return arr, result


def handler():
    result = 0
    for line in load_input():
        arr = list(map(int, line.split(" ")))
        arr = make_arr_of_diffs([arr])
        arr, r = fill_placeholders(arr)
        result += r
    return result


if __name__ == '__main__':
    print(handler())