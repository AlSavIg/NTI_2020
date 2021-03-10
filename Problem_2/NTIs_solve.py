def find_bound(lst):
    s = -1
    e = -1
    for i in range(1, len(lst)):
        if lst[i - 1] == 0 and lst[i] != 0:
            s = i - 1
        if lst[i] != 0 and lst[i + 1] == 0:
            e = i + 1
        if s > 0 and e > 0:
            return s, e
    raise RuntimeError("No bounds!")


def get_bounding_box(m):
    rows = [sum(row) for row in m]
    cols = []
    for i in range(len(m[0])):
        col = []
        for j in range(len(m)):
            col.append(m[j][i])
        cols.append(sum(col))
    rs, re = find_bound(rows)
    cs, ce = find_bound(cols)
    return rs, cs, re, ce

h, w = map(int, input().split())
m = []
for i in range(h):
    line = map(int, input().split())
    m.append(list(line))

print(*get_bounding_box(m))
