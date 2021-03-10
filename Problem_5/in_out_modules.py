def debugger_print_matrix(matrix):
    print()
    for i in range(len(matrix)):
        print(*matrix[i])


def read_from_file(main_matrix, gifts):
    file_input = open("input.txt", "r")
    height, width, n, k = map(int, file_input.readline().split())
    x_s, y_s = map(int, file_input.readline().split())
    main_matrix = [list(map(int, file_input.readline().split()))
                   for i in range(n)]
    gifts = [list(map(int, file_input.readline().split())) for i in range(k)]
    file_input.close()

    return height, width, n, k, x_s, y_s, main_matrix, gifts


def read_from_flow(main_matrix, gifts):
    height, width, n, k = map(int, input().split())
    x_s, y_s = map(int, input().split())
    main_matrix = [list(map(int, input().split())) for i in range(n)]
    gifts = [list(map(int, input().split())) for i in range(k)]
    return height, width, n, k, x_s, y_s, main_matrix, gifts


def beauty_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()
    print()
