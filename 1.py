data = "R3, R1, R4, L4, R3, R1, R1, L3, L5, L5, L3, R1, R4, L2, L1, R3, L3, R2, R1, R1, L5, L2, L1, R2, L4, R1, L2, L4, R2, R2, L2, L4, L3, R1, R4, R3, L1, R1, L5, R4, L2, R185, L2, R4, R49, L3, L4, R5, R1, R1, L1, L1, R2, L1, L4, R4, R5, R4, L3, L5, R1, R71, L1, R1, R186, L5, L2, R5, R4, R1, L5, L2, R3, R2, R5, R5, R4, R1, R4, R2, L1, R4, L1, L4, L5, L4, R4, R5, R1, L2, L4, L1, L5, L3, L5, R2, L5, R4, L4, R3, R3, R1, R4, L1, L2, R2, L1, R4, R2, R2, R5, R2, R5, L1, R1, L4, R5, R4, R2, R4, L5, R3, R2, R5, R3, L3, L5, L4, L3, L2, L2, R3, R2, L1, L1, L5, R1, L3, R3, R4, R5, L3, L5, R1, L3, L5, L5, L2, R1, L3, L1, L3, R4, L1, R3, L2, L2, R3, R3, R4, R4, R1, L4, R1, L5"

def easter_bunny_hq(data):
    DIRS = ((0, 1), (1, 0), (0, -1), (-1, -0))
    letter_to_dir = {"R": 1,"L": -1}
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

print(easter_bunny_hq("R2, L3"))
print(easter_bunny_hq("R2, R2, R2"))
print(easter_bunny_hq("R5, L5, R5, R3"))
print(easter_bunny_hq(data))
