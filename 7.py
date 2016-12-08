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
