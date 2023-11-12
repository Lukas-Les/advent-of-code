DRAW = 3
WIN = 6


def solve(elf, me):
    if me == "X":
        score = 1
        if elf == "A":
            return DRAW + score
        elif elf == "B":
            return score
        elif elf == "C":
            return WIN + score

    elif me == "Y":
        score = 2
        if elf == "B":
            return DRAW + score
        elif elf == "A":
            return WIN + score
        elif elf == "C":
            return score

    elif me == "Z":
        score = 3
        if elf == "C":
            return DRAW + score
        elif elf == "A":
            return score
        elif elf == "B":
            return WIN + score


if __name__ == '__main__':
    with open("task_input.txt", "r") as f:
        task_input = f.read().split("\n")
result = 0
for i in task_input:
    elf, me = i.split(" ")
    result += solve(elf, me)
print(result)
