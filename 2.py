DIRS = ((0, 1), (1, 0), (0, -1), (-1, -0))
keypad1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
keypad2 = [
    [None, None, 1, None, None],
    [None, 2, 3, 4, None],
    [5, 6, 7, 8, 9],
    [None, 'A', 'B', 'C', None],
    [None, None, 'D', None, None],
]

char_to_dir = {"R": (0, 1), "U": (-1, 0), "D": (1, 0), "L": (0, -1)}


def try_inc(num, val, keypad):
    newNum = num + val
    return num if newNum < 0 or newNum >= len(keypad) else newNum


def bathroom_security(input, kp):
    steps = input.split("\n")
    pos = [2, 0]
    result = []
    for step in steps:
        for char in step:
            dir = char_to_dir[char]
            next = [try_inc(num, dir[x], kp) for x, num in enumerate(pos)]
            x, y = next
            if kp[x][y] is not None:
                pos = next
        x, y = pos
        result.append(kp[x][y])
    return "".join(list(map(str, result)))

data = open('2_data.txt', 'r').read().strip()
print(bathroom_security(data, keypad1))
print(bathroom_security(data, keypad2))
