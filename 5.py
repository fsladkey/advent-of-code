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
