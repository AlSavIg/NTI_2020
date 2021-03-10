from random import randint

height = randint(5, 15)
width = randint(5, 15)
file_output = open("input.txt", "w")
file_output.write(str(height) + " " + str(width) + "\n")

matrix = [[0] * width for i in range(height)]


for i in range(height):
    for j in range(width):
        file_output.write(str(matrix[i][j]) + " ")
    file_output.write("\n")
file_output.close()
