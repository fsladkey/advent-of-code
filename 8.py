import re

def add_rect(grid, y, x):
    for idx in range(x):
        for idy in range(y):
            grid[idx][idy] = '*'


def rotate_row(grid, row, rotations):
    for _ in range(rotations):
        grid[row].insert(0, grid[row].pop())
    return grid


def rotate_col(grid, col, rotations):
    for _ in range(rotations):
        prev_val = grid[-1][col]
        for idx in range(len(grid)):
            current_val = grid[idx][col]
            grid[idx][col] = prev_val
            prev_val = current_val
    return grid


def two_factor(input):
    grid = [[' '] * 50 for _ in range(6)]
    lines = input.split('\n')
    actions = {
        '(\d+)x(\d+)': add_rect,
        'x=(\d+)\D+(\d+)': rotate_col,
        'y=(\d+)\D+(\d+)': rotate_row
    }
    for line in lines:
        for pattern, action in actions.items():
            match = re.search(pattern, line)
            if match:
                action(grid, int(match.groups(0)[0]), int(match.groups(0)[1]))
    return grid

def num_lights(grid):
    return [item for sublist in grid for item in sublist].count('*')


data = open('8_data.txt', 'r').read().strip()
result = two_factor(data)
for row in result:
    print(''.join(row))
print(num_lights(result))
