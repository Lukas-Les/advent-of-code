DRAW = 3
WIN = 6


class Base:
    def __init__(
        self,
        elf_code,
        my_code,
        score,
    ):
        self.elf_code = elf_code
        self.my_code = my_code
        self.score = score
        self.loses_against = None
        self.wins_against = None

    def __repr__(self):
        return self.elf_code


Rock = Base("A", "X", 1)
Paper = Base("B", "Y", 2)
Scissors = Base("C", "Z", 3)

Rock.wins_against = Scissors
Rock.loses_against = Paper

Paper.wins_against = Rock
Paper.loses_against = Scissors

Scissors.wins_against = Paper
Scissors.loses_against = Rock


def set_object(elf: str):
    if elf == "A":
        return Rock
    elif elf == "B":
        return Paper
    elif elf == "C":
        return Scissors


def choose_path(elf: Base, path: str):
    if path == "X":
        return elf.wins_against.score
    elif path == "Y":
        return elf.score + DRAW
    elif path == "Z":
        return elf.loses_against.score + WIN


result = 0


with open("input2.txt", "r") as f:
    task_input = f.read().split("\n")
    for i in task_input:
        elf, path = i.split(" ")
        elf = set_object(elf)
        result += choose_path(elf, path)

print(result)
