from random import randint

height = randint(5, 15)
width = randint(5, 15)
file_output = open("input.txt", "w")
file_output.write(str(height) + " " + str(width) + "\n")

s_pos_i = randint(1, height // 2)
s_pos_j = randint(1, width // 2)

f_pos_i = randint(height // 2 + 1, height - 1)
f_pos_j = randint(width // 2 + 1, width - 1)

for i in range(height):
    if i == 0 or i == height - 1:
        for j in range(width):
            file_output.write("0" + " ")
    elif s_pos_i <= i <= f_pos_i:
        for j in range(width):
            if j == 0 or j == width - 1:
                file_output.write("0" + " ")
            elif s_pos_j <= j <= f_pos_j:
                    file_output.write("1" + " ")
            else:
                file_output.write("0" + " ")
    else:
        for j in range(width):
            file_output.write("0" + " ")
    file_output.write("\n")
file_output.close()
