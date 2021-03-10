from in_out_modules import *


def edge_searching(main_matrix):
    lst_ind = []
    index_i_1, index_j_1, index_i_2, index_j_2 = 0, 0, 0, 0
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if main_matrix[i][j] == 1:
                index_i_1 = i
                index_j_1 = j
                while main_matrix[i][j] == 1:
                    index_j_2 = j
                    j += 1
                j = index_j_1
                while main_matrix[i][j] == 1:
                    main_matrix[i][j] = 2
                    index_i_2 = i
                    i += 1
                i = index_i_1
                a = abs(index_i_1 - index_i_2) + 1
                b = abs(index_j_1 - index_j_2) + 1
                count = 0
                if a >= b:
                    count = a / b
                else:
                    count = b / a
                lst_ind.append([count,
                                index_i_1,
                                index_j_1,
                                index_i_2,
                                index_j_2])
            if main_matrix[i][j] == 2:
                while main_matrix[i][j] == 2 and main_matrix[i][j + 1] == 1:
                    main_matrix[i][j + 1] = 2
    return lst_ind


def max_count(lst_ind):
    max = -1
    for i in range(len(lst_indexes)):
        if lst_indexes[i][0] > max:
            max = lst_indexes[i][0]
    return max


def inpainting(main_matrix, max):
    for a in range(len(lst_indexes)):
        for i in range(lst_indexes[a][1], lst_indexes[a][3] + 1):
            for j in range(lst_indexes[a][2], lst_indexes[a][4] + 1):
                if lst_indexes[a][0] == max:
                    main_matrix[i][j] = 1
                else:
                    main_matrix[i][j] = 0


main_matrix = []
height, width, main_matrix = read_from_flow(main_matrix)
lst_indexes = edge_searching(main_matrix)
max = max_count(lst_indexes)
inpainting(main_matrix, max)
debugger_print_matrix(main_matrix)
# print(lst_indexes)
