def debugger_print_matrix(matrix):
    print()
    for i in range(len(matrix)):
        print(*matrix[i])


def read_from_file():
    global main_matrix
    file_input = open("input.txt", "r")
    height, width = map(int, file_input.readline().split())
    main_matrix = [list(map(int, file_input.readline().split()))
                   for i in range(height)]
    file_input.close()

    return height, width


def read_from_flow():
    global main_matrix
    height, width = map(int, input().split())
    main_matrix = [list(map(int, input().split())) for i in range(height)]

    return height, width


inside_area = 0
main_matrix = []
height, width = read_from_flow()
debugger_print_matrix(main_matrix)

for i in range(1, height - 1):
    for j in range(1, width - 1):
        up = main_matrix[i + 1][j] != 0
        down = main_matrix[i - 1][j] != 0
        right = main_matrix[i][j + 1] != 0
        left = main_matrix[i][j - 1] != 0
        up_left = main_matrix[i + 1][j - 1] != 0
        up_right = main_matrix[i + 1][j - 1] != 0
        down_left = main_matrix[i - 1][j - 1] != 0
        down_right = main_matrix[i - 1][j + 1] != 0
        case = ((up and down and right and left and up_left)
                 and (up_right and down_left and down_right))
        if case:
            inside_area += 1

print(inside_area)
