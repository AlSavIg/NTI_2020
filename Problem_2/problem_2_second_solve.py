from in_out_modules import *


main_matrix = []
height, width, main_matrix = read_from_flow(main_matrix)
index_i_1, index_j_1, index_i_2, index_j_2 = 0, 0, 0, 0

debugger_print_matrix(main_matrix)

for i in range(1, height - 1):
    for j in range(1, width - 1):
        if main_matrix[i][j] == 1:
            index_i_1 = i - 1
            index_j_1 = j - 1
            print(index_i_1, index_j_1, end=" ")
            start_i = i
            while main_matrix[i][j] == 1:
                index_i_2 = i + 1
                i += 1
            i = start_i
            while main_matrix[i][j] == 1:
                index_j_2 = j + 1
                j += 1
            print(index_i_2, index_j_2, end=" ")
        case = index_i_2 != 0
        if case:
            break
    if case:
        break
