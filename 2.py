DIRS = ((0, 1), (1, 0), (0, -1), (-1, -0))
keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

char_to_dir = {"R": (0, 1), "U": (-1, 0), "D": (1, 0), "L": (0, -1)}


def maybe_increment(num, val):
    newNum = num + val
    return num if newNum < 0 or newNum > 2 else newNum


def bathroom_security(input):
    steps = input.split("\n")
    pos = [1, 1]
    result = []
    for step in steps:
        for char in step:
            dir = char_to_dir[char]
            for idx in range(2):
                pos[idx] = maybe_increment(pos[idx], dir[idx])
        x, y = pos
        result.append(keypad[x][y])
    return "".join(list(map(str, result)))

data = open('2_data.txt', 'r').read().strip()
print(bathroom_security(data))
