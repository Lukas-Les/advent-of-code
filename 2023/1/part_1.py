def load_input():
    with open("input.txt", "r") as f:
        return f.read().strip()


numbers = []

for line in load_input().split("\n"):
    line_res = []
    for char in line:
        if char.isnumeric():
            line_res.append(int(char))
            break
    for char in line[::-1]:
        if char.isnumeric():
            line_res.append(int(char))
            break
    numbers.append(f"{line_res[0]}{line_res[1]}")

numbers = [int(x) for x in numbers]
print(sum(numbers))
