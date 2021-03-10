def neighbors(i, j):
    return ((i - 1, j),
    (i + 1, j),
    (i, j - 1),
    (i, j + 1),
    (i + 1, j - 1),
    (i + 1, j + 1),
    (i - 1, j - 1),
    (i - 1, j + 1))


def get_area(m):
    area = 0
    for i in range(1, len(m) - 1):
        for j in range(1, len(m[0]) - 1):
            if m[i][j] != 0:
                nbs = [m[n[0]][n[1]] for n in neighbors(i, j)]
            if 0 not in nbs:
                area += 1
    return area


h, w = map(int, input().split())
m = []
for i in range(h):
    line = map(int, input().split())
    m.append(list(line))

print(get_area(m))
