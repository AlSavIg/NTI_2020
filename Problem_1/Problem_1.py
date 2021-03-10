from in_out_modules import *


inside_area = 0
main_matrix = []
height, width, main_matrix = read_from_file(main_matrix)
debugger_print_matrix(main_matrix)

for i in range(1, height - 1):
    for j in range(1, width - 1):
        owning = main_matrix[i][j] == 1
        down = main_matrix[i + 1][j] == 1
        up = main_matrix[i - 1][j] == 1
        right = main_matrix[i][j + 1] == 1
        left = main_matrix[i][j - 1] == 1
        down_left = main_matrix[i + 1][j - 1] == 1
        down_right = main_matrix[i + 1][j + 1] == 1
        up_left = main_matrix[i - 1][j - 1] == 1
        up_right = main_matrix[i - 1][j + 1] == 1
        case = ((down and up and right and left and down_left)
                 and (down_right and up_left and up_right and owning))
        if case:
            inside_area += 1

print(inside_area)
