from random import randint

height = randint(5, 15)
width = randint(5, 15)
file_output = open("input.txt", "w")
file_output.write(str(height) + " " + str(width) + "\n")
for i in range(height):
    if i == 0 or i == height - 1:
        for j in range(width):
            file_output.write("0" + " ")
    else:
        for j in range(width):
            if j == 0 or j == width - 1:
                file_output.write("0" + " ")
            else:
                file_output.write(str(randint(0, 1)) + " ")
    file_output.write("\n")
file_output.close()
