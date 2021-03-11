def debugger_print_matrix(matrix):
    print()
    for i in range(len(matrix)):
        print(*matrix[i])


def read_from_file(main_matrix):
    file_input = open("input.txt", "r")
    num = int(file_input.readline())
    main_matrix = [list(map(float, file_input.readline().split()))
                   for i in range(num)]
    file_input.close()

    return num, main_matrix


def read_from_flow(main_matrix):
    num = int(input())
    main_matrix = [list(map(float, input().split())) for i in range(num)]

    return num, main_matrix


def beauty_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()
