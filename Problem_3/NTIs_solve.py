def find_bound(lst):
    s = -1
    e = -1
    for i in range(1, len(lst)):
        if lst[i - 1] == 0 and lst[i] != 0:
            s = i
        if lst[i] != 0 and lst[i + 1] == 0:
            e = i
        if s > 0 and e > 0:
            return s, e
    raise RuntimeError("No bounds!")


def copy(m):
    lm = []
    for i in range(len(m)):
        l = []
        for j in range(len(m[0])):
            l.append(m[i][j])
        lm.append(l)
    return lm


def negate(m):
    lm = copy(m)
    for i in range(len(lm)):
        for j in range(len(lm[0])):
            if lm[i][j] == 1:
                lm[i][j] = -1
    return lm


def neighbors(i, j):
    return ((i - 1, j),
            (i + 1, j),
            (i, j - 1),
            (i, j + 1))

def mark(m):
    lm = negate(m)
    label = 0
    for y in range(len(lm)):
        for x in range(len(lm[0])):
            px = lm[y][x]
            if px == -1:
                label += 1
                search(lm, label, y, x)
    return lm


def search(m, label, y, x):
    m[y][x] = label
    nbs = neighbors(y, x)
    for ny, nx in nbs:
        if m[ny][nx] == -1:
            search(m, label, ny, nx)


def clean_m(m, label):
    lm = copy(m)
    for i in range(len(lm)):
        for j in range(len(lm[0])):
            if lm[i][j] != label:
                lm[i][j] = 0
    return lm


def get_shape(m, label):
    lm = clean_m(m, label)
    rows = [sum(row) for row in lm]
    cols = []
    for i in range(len(lm[0])):
        col = []
        for j in range(len(lm)):
            col.append(lm[j][i])
        cols.append(sum(col))

    rs, re = find_bound(rows)
    cs, ce = find_bound(cols)

    rsize = (re - rs) + 1
    csize = (ce - cs) + 1
    return rsize, csize


def get_aspect(m, label):
    rsize, csize = get_shape(m, label)
    aspect = 1
    if rsize > csize:
        aspect = rsize / csize
    else:
        aspect = csize / rsize
    return aspect


def max_label(m):
    mx = 0
    values = []
    for row in m:
        values.extend(row)
    return max(values)


def only_longest(m):
    lm = mark(m)
    aspects = {}
    for label in range(1, max_label(lm) + 1):
        aspects[label] = get_aspect(lm, label)

    longest = list(sorted(aspects.items(), key=lambda x: x[1]))[-1]
    longest_label = longest[0]
    return clean_m(lm, longest_label)


h, w = map(int, input().split())
m = []
for i in range(h):
    line = map(int, input().split())
    m.append(list(line))

longest = only_longest(m)

print()

for row in longest:
    line = ["1" if val > 0 else "0" for val in row]
    print (" ".join(line))
