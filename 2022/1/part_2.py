with open("input.txt", "r") as f:
    task_input = f.read()


def create_batches(text):
    result = []
    for i in text.split("\n\n"):
        r = 0
        for j in i.split("\n"):
            try:
                r += int(j)
            except ValueError:
                pass
        result.append(r)
    return result


batches = create_batches(task_input)
batches.sort()
print(sum(batches[-3:]))
