def load_input():
    with open("input.txt", "r") as f:
        return f.read().strip()


def parse_line(_line):
    for char in _line:
        if char.isnumeric():
            return int(char)


result = 0

for line in load_input().split("\n"):
    number = f"{parse_line(line)}{parse_line(line[::-1])}"
    if number:
        result += int(number)

print(result)
