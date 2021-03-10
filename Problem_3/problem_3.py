from in_out_modules import *


def edge_searching(matrix):
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            owning = matrix[i][j] == 1
            down = matrix[i + 1][j] == 1
            up = matrix[i - 1][j] == 1
            right = matrix[i][j + 1] == 1
            left = matrix[i][j - 1] == 1
            down_left = matrix[i + 1][j - 1] == 0
            down_right = matrix[i + 1][j + 1] == 1
            up_left = matrix[i - 1][j - 1] == 1
            up_right = matrix[i - 1][j + 1] == 0
            up_left_point = (up_right and down_left and down and not up
                             and right and not left and down_right and
                             not up_left and owning)
            down_right_point = (up_right and down_left and not down and up
                                and not right and left and not down_right and
                                up_left and owning)
            if up_left_point:
                


main_matrix = []
height, width, main_matrix = read_from_file(main_matrix)
debugger_print_matrix(main_matrix)
