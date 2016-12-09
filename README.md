### Day 1

```python
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
```

### Day 2

```python
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

```
### Day 3

```python
def valid_triangle(points):
    for idx in range(3):
        if sum(points[:idx] + points[idx + 1:]) <= points[idx]:
            return False
    return True


def reducer(total, tri):
    return total + 1 if valid_triangle(tri) else total


def valid_triangles(input):
    return reduce(reducer, input, 0)


def parse_input_vertical(input):
    results = []
    nums = input.split()
    current_idx = 0
    sub_result = [[] for _ in (range(3))]
    for num in nums:
        sub_result_idx = current_idx % 3
        sub_result[sub_result_idx].append(int(num))
        if current_idx == 8:
            results += sub_result
            sub_result = [[] for _ in (range(3))]
            current_idx = -1
        current_idx += 1
    return results

def parse_input_horizantal(input):
    lines = input.split("\n")
    return [list(map(int, x.split())) for x in lines]


data = open('3_data.txt', 'r').read().strip()
test = open('3_test.txt', 'r').read().strip()
print(valid_triangles(parse_input_horizantal(data)))
print(valid_triangles(parse_input_vertical(data)))

```
### Day 4

```python
import re
from collections import Counter
from string import ascii_lowercase


def extract_info(line):
    pattern = '(.+?(?=d*))(\d+)\[(.+)\]'
    match = re.search(pattern, line)
    letters = match.group(1)
    sector_id = int(match.group(2))
    checksum = match.group(3)
    return (letters, sector_id, checksum)


def caeser_cipher(string, offset):
    alpha = ascii_lowercase
    cipher_dict = {'-': ' '}
    result = ''
    for idx in range(26):
        letter = alpha[idx]
        cipher = alpha[(idx + offset) % 26]
        cipher_dict[letter] = cipher
    for letter in string:
        result += cipher_dict[letter]
    return result


def security_through_obscurity(input, decrypt=False):
    lines = input.split('\n')
    sum = 0
    for line in lines:
        letters, sector_id, checksum = extract_info(line)
        counts = Counter(letters.replace('-', ''))
        message = caeser_cipher(letters, sector_id)
        if decrypt and 'north' in message:
            return sector_id
        def compare(a, b):
            if counts[a] == counts[b]:
                return cmp(a, b)
            return cmp(counts[b], counts[a])
        checksum_match = "".join(sorted(counts.keys(), compare))[:5]
        if checksum == checksum_match:
            sum += sector_id
    return sum

data = open('4_data.txt', 'r').read().strip()
print(security_through_obscurity(data))
print(security_through_obscurity(data, decrypt=True))

```
### Day 5

```python
from hashlib import md5

def hash_password(input):
    result = ''
    idx = 0
    while len(result) < 8:
        string = input + str(idx)
        hash = md5(string).hexdigest()
        if hash[:5] == ('0' * 5):
            result += hash[5]
        idx += 1
    return result


def hash_password_with_index(input):
    result = [None] * 8
    idx = 0
    count = 0
    while count < len(result):
        string = input + str(idx)
        hash = md5(string).hexdigest()
        if hash[:5] == ('0' * 5):
            try:
                index = int(hash[5])
                value = hash[6]
                if (not result[index]):
                    result[index] = value
                    count += 1
            except:
                'look ma, no errors!'
        idx += 1
    return "".join(result)

print(hash_password('abc'))
print(hash_password('wtnhxymk'))
print(hash_password_with_index('abc'))
print(hash_password_with_index('wtnhxymk'))

```
### Day 6

```python
from collections import Counter

def signals_and_noise(input, cb):
    lines = input.split('\n')
    counters = [Counter() for _ in range(len(lines[0]))]
    for line in lines:
        for idx in range(len(line)):
            current_idx_counter = counters[idx]
            letter = line[idx]
            current_idx_counter[letter] += 1
    return ''.join(list(map(cb, counters)))


data = open('6_data.txt', 'r').read().strip()
print(signals_and_noise(data, lambda x: x.most_common(1)[0][0]))
print(signals_and_noise(data, lambda x: x.most_common()[-1][0]))
```

### Day 7

```python
def is_abba(string):
    return string[0] != string[1] and string[0:2] == string[2:4][::-1]


def is_aba(string):
    return string[0] != string[1] and string[0] == string[2]


def contains_abba(string):
    if len(string) < 4:
        return False
    for i in range(len(string) - 2):
        if is_abba(string[i:i + 4]):
            return True
    return False


def contains_bab(aba, strings):
    for str in strings:
        if (aba[1] + aba[0] + aba[1]) in str:
            return True
    return False


def split_string(string):
    accept = []
    reject = []
    acceptable = True
    slice = ''
    for i in range(len(string)):
        if string[i] == '[':
            accept.append(slice)
            acceptable = False
            slice = ''
        elif string[i] == ']':
            reject.append(slice)
            acceptable = True
            slice = ''
        else:
            slice += string[i]
    accept.append(slice) if acceptable else reject.append(slice)
    return (accept, reject)


def supports_TLS(string):
    accept, reject = split_string(string)
    if any([contains_abba(str) for str in reject]):
        return False
    return any([contains_abba(str) for str in accept])


def supports_SSL(string):
    accept, reject = split_string(string)
    for str in accept:
        abas = get_abas(str)
        for aba in abas:
            if contains_bab(aba, reject):
                return True
    return False


def reducer(cb):
    return lambda total, string: total + 1 if cb(string) else total


def num_support_protocal(input, cb):
    lines = input.split('\n')
    return reduce(reducer(cb), lines, 0)


data = open('7_data.txt', 'r').read().strip()
print(num_support_protocal(data, supports_TLS))
print(num_support_protocal(data, supports_SSL))
```

### Day 8

```python
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

```
