from random import randint


height = randint(10, 30)
width = randint(10, 30)
COUNT_OF_QUADRILATERAL = 2
file_output = open("input.txt", "w")
file_output.write(str(height) + " " + str(width) + "\n")

matrix = [[0] * width for i in range(height)]

s_pos_i = [randint(1, height // 2 - 5) for i in range(COUNT_OF_QUADRILATERAL)]
s_pos_j = [randint(1, width // 2 - 5) for i in range(COUNT_OF_QUADRILATERAL)]

f_pos_i = [randint(height // 2 + 1, height - 3) for i in range(COUNT_OF_QUADRILATERAL)]
f_pos_j = [randint(width // 2 + 1, width - 3) for i in range(COUNT_OF_QUADRILATERAL)]

for a in range(COUNT_OF_QUADRILATERAL):
    for i in range(1, height):
        if s_pos_i[a] <= i <= f_pos_i[a]:
            for j in range(1, width):
                if s_pos_j[a] <= j <= f_pos_j[a]:
                    matrix[i][j] = 1

for i in range(1, height - 1):
    for j in range(1, width - 1):
        if matrix[i + 1][j] == 0 and matrix[i - 1][j] == 1 and matrix[i][j + 1] == 1:
            for a in range(1, width):
                matrix[i - 1][a] = 0
        if matrix[i + 1][j] == 1 and matrix[i - 1][j] == 0 and matrix[i][j + 1] == 1:
            for a in range(1, width):
                matrix[i + 1][a] = 0

for i in range(1, height - 1):
    for j in range(1, width - 1):
        if matrix[i + 1][j] == 1 and matrix[i - 1][j] == 1:
            matrix[i][j] = 1
        elif ((matrix[i + 1][j] == 0 and matrix[i - 1][j] == 1) or
              (matrix[i + 1][j] == 1 and matrix[i - 1][j] == 0)):
            for a in range(1, width):
                matrix[i][a] = 0


for i in range(height):
    for j in range(width):
        file_output.write(str(matrix[i][j]) + " ")
    file_output.write("\n")
file_output.close()
