import re
from collections import Counter


def extract_info(line):
    pattern = '(.+?(?=d*))(\d+)\[(.+)\]'
    match = re.search(pattern, line)
    letters = match.group(1).replace('-', '')
    sector_id = int(match.group(2))
    checksum = match.group(3)
    return (letters, sector_id, checksum)


def security_through_obscurity(input):
    lines = input.split('\n')
    sum = 0
    for line in lines:
        letters, sector_id, checksum = extract_info(line)
        counts = Counter(letters)

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
