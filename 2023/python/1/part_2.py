def load_input():
    with open("input.txt", "r") as f:
        return f.read().strip()


words_to_int = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
shortest_word = min([len(i) for i in words_to_int])
result = 0


def str_to_int(cache):
    for i in words_to_int:
        if i in cache:
            return words_to_int.index(i)


def parse_line(_line: str, rev: bool = False):
    cache = ""
    if rev:
        _line = _line[::-1]
    for char in _line:
        if char.isnumeric():
            return int(char)
        elif char.isalpha():
            cache += char
        if len(cache) >= shortest_word:
            num = str_to_int(cache if not rev else cache[::-1])
            if num:
                return num


for line in load_input().split("\n"):
    line_res = f"{parse_line(line)}{parse_line(line, rev=True)}"
    result += int(line_res)

print(result)
