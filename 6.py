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
