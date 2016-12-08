def valid_triangle(points):
    print(points)
    for idx in range(3):
        if sum(points[:idx] + points[idx + 1:]) <= points[idx]:
            return False
    return True


def reducer(total, tri):
    return total + 1 if valid_triangle(tri) else total


def valid_triangles(input):
    lines = input.split("\n")
    possible_triangles = [list(map(int, x.split())) for x in lines]
    return reduce(reducer, possible_triangles, 0)

data = open('3_data.txt', 'r').read().strip()
print(valid_triangles(data))
