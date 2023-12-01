def load_input():
    with open("input.txt", "r") as f:
        return f.read().strip()


words_to_int = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers = []


def parse_line(line, rev=False):
    cache = ""
    for char in line:
        if char.isnumeric():
            return int(char)
        elif char.isalpha():
            cache += char
        if cache in words_to_int:
            return words_to_int.index(cache)
        for word in words_to_int:
            if word in cache:
                return words_to_int.index(word)
    return ""


def parse_line_reverse(line):
    cache = ""
    for char in line[::-1]:
        if char.isnumeric():
            return int(char)
        elif char.isalpha():
            cache += char
        temp_cache = cache[::-1]
        if temp_cache in words_to_int:
            return words_to_int.index(temp_cache)
        for word in words_to_int:
            if word in temp_cache:
                return words_to_int.index(word)
    return ""


for line in load_input().split("\n"):
    line_res = f"{parse_line(line)}{parse_line_reverse(line)}"
    numbers.append(line_res)

numbers = [int(x) for x in numbers]
print(sum(numbers))


