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
