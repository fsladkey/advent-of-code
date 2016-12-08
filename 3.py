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
