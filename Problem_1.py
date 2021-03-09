def debugger_print_matrix(matrix):
    for i in range(height):
        print(*matrix[i])


height, width = map(int, input().split())

main_matrix = [list(map(int, input().split())) for i in range(height)]
inside_area = 0

for i in range(1, height - 1):
    for j in range(1, width - 1):
        up = main_matrix[i + 1][j] != 0
        down = main_matrix[i - 1][j] != 0
        right = main_matrix[i][j + 1] != 0
        left = main_matrix[i][j - 1] != 0
        if up and down and right and left:
            inside_area += 1

print(inside_area)
