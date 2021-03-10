from in_out_modules import *


def walking_lab(i, j):
    global field
    global count
    field[i][j] = 1
    if field[i + 1][j] == 0:
        walking_lab(i + 1, j)
    elif field[i + 1][j] == 2:
        count += 1
        walking_lab(i + 1, j)
    if field[i - 1][j] == 0:
        walking_lab(i - 1, j)
    elif field[i - 1][j] == 2:
        count += 1
        walking_lab(i - 1, j)
    if field[i][j + 1] == 0:
        walking_lab(i, j + 1)
    elif field[i][j + 1] == 2:
        count += 1
        walking_lab(i, j + 1)
    if field[i][j - 1] == 0:
        walking_lab(i, j - 1)
    elif field[i][j - 1] == 2:
        count += 1
        walking_lab(i, j - 1)


def create_field(field, height, width):
    for i in range(height):
        for j in range(width):
            if [i, j] in walls:
                field[i][j] = 1
            elif [i, j] in gifts:
                field[i][j] = 2


walls = []
gifts = []
count = 0
height, width, n, k, x_s, y_s, walls, gifts = read_from_file(walls, gifts)
field = [[0] * width for i in range(height)]

create_field(field, height, width)

beauty_print(field)

walking_lab(x_s, y_s)
beauty_print(field)

result = k - count

print(result)
