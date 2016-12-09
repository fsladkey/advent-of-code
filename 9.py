import re

def decompress(input, recursive=False):
    idx = 0
    result = 0
    while idx < len(input):
        char = input[idx]
        if char == '(':
            match = re.match('\((\d+)x(\d+)\)', input[idx:])
            num_chars = int(match.groups(0)[0])
            repeats = int(match.groups(0)[1])
            idx += match.end()
            slice = input[idx:idx + num_chars]
            if recursive:
                result += decompress(slice, recursive=True) * repeats
            else:
                result += len(slice) * repeats
            idx += num_chars
        else:
            result += 1
            idx += 1
    return result


data = "".join(open('9_data.txt', 'r').read().split())
print(decompress(data, recursive=True))
