from random import randint


height = randint(10, 30)
width = randint(10, 30)
COUNT_OF_QUADRILATERAL = 4
file_output = open("input.txt", "w")
file_output.write(str(height) + " " + str(width) + "\n")

matrix = [[0] * width for i in range(height)]

s_pos_i_1 = randint(1, height // 4)
s_pos_j_1 = randint(1, width // 4)

f_pos_i_1 = randint(height // 4, height // 2 - 1)
f_pos_j_1 = randint(width // 4, width // 2 - 1)


s_pos_i_2 = randint(1, height // 4 - 1)
s_pos_j_2 = randint(width // 2, width // 4 * 3)

f_pos_i_2 = randint(height // 4, height // 2 - 1)
f_pos_j_2 = randint(width // 4 * 3, width - 1)


s_pos_i_3 = randint(height // 2, height // 4 * 3)
s_pos_j_3 = randint(1, width // 4 - 1)

f_pos_i_3 = randint(height // 4 * 3, height)
f_pos_j_3 = randint(width // 4, width // 2)


s_pos_i_4 = randint(height // 2, height // 4 * 3)
s_pos_j_4 = randint(width // 2 + 1, width // 4 * 3)

f_pos_i_4 = randint(height // 4 * 3, height - 1)
f_pos_j_4 = randint(width // 4 * 3, width)

s_pos_i = (s_pos_i_1, s_pos_i_2, s_pos_i_3, s_pos_i_4)
s_pos_j = (s_pos_j_1, s_pos_j_2, s_pos_j_3, s_pos_j_4)
f_pos_i = (f_pos_i_1, f_pos_i_2, f_pos_i_3, f_pos_i_4)
f_pos_j = (f_pos_j_1, f_pos_j_2, f_pos_j_3, f_pos_j_4)

for a in range(COUNT_OF_QUADRILATERAL):
    for i in range(1, height - 1):
        if s_pos_i[a] <= i <= f_pos_i[a]:
            for j in range(1, width - 1):
                if s_pos_j[a] <= j <= f_pos_j[a]:
                    matrix[i][j] = 1

for i in range(height):
    for j in range(width):
        file_output.write(str(matrix[i][j]) + " ")
    file_output.write("\n")
file_output.close()
