def debugger_print_matrix(matrix):
    print()
    for i in range(len(matrix)):
        print(*matrix[i])


def read_from_file(main_matrix):
    file_input = open("input.txt", "r")
    height, width = map(int, file_input.readline().split())
    main_matrix = [list(map(int, file_input.readline().split()))
                   for i in range(height)]
    file_input.close()

    return height, width, main_matrix


def read_from_flow(main_matrix):
    height, width = map(int, input().split())
    main_matrix = [list(map(int, input().split())) for i in range(height)]

    return height, width, main_matrix


def beauty_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()
