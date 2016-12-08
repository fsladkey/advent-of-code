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

print(hash_password('abc'))
