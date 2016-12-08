from collections import Counter

DIRS = ((0, 1), (1, 0), (0, -1), (-1, -0))
letter_to_dir = {"R": 1, "L": -1}


def easter_bunny_hq(data):
    steps = data.split(", ")
    dir_idx = 0
    pos = [0, 0]
    for step in steps:
        letter = step[0]
        num = int(step[1:])
        increment_dir = letter_to_dir[letter]
        dir_idx = (dir_idx + increment_dir) % len(DIRS)
        for _ in range(num):
            dir = DIRS[dir_idx]
            pos[0] += dir[0]
            pos[1] += dir[1]
    return abs(pos[0]) + abs(pos[1])


def easter_bunny_hq_double(data):
    steps = data.split(", ")
    dir_idx = 0
    pos = [0, 0]
    location_count = Counter(tuple(pos))
    for step in steps:
        letter = step[0]
        num = int(step[1:])
        increment_dir = letter_to_dir[letter]
        dir_idx = (dir_idx + increment_dir) % len(DIRS)
        for _ in range(num):
            dir = DIRS[dir_idx]
            pos[0] += dir[0]
            pos[1] += dir[1]
            location_count[tuple(pos)] += 1
            if location_count[tuple(pos)] == 2:
                return abs(pos[0]) + abs(pos[1])

data = open('1_data.txt', 'r').read()
print(easter_bunny_hq(data))
print(easter_bunny_hq_double(data))
