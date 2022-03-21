def check():
    line_1 = field[0].count("_")
    line_2 = field[1].count("_")
    line_3 = field[2].count("_")

    result = int(line_1) + int(line_2) + int(line_3)
    if result == 0:
        return 0

def row():
    x_row1 = list(zip(*field))[0].count("x")
    o_row1 = list(zip(*field))[0].count("o")

    x_row2 = list(zip(*field))[1].count("x")
    o_row2 = list(zip(*field))[1].count("o")

    x_row3 = list(zip(*field))[2].count("x")
    o_row3 = list(zip(*field))[2].count("o")

    if x_row1 == 3:
        return 1
    elif o_row1 == 3:
        return 2

    elif x_row2 == 3:
        return 1
    elif o_row2 == 3:
        return 2

    elif x_row3 == 3:
        return 1
    elif o_row3 == 3:
        return 2

def line():
    x_line1 = field[0].count("x")
    o_line1 = field[0].count("o")

    x_line2 = field[1].count("x")
    o_line2 = field[1].count("o")

    x_line3 = field[2].count("x")
    o_line3 = field[2].count("o")

    if x_line1 == 3:
        return 1
    elif o_line1 == 3:
        return 2

    elif x_line2 == 3:
        return 1
    elif o_line2 == 3:
        return 2

    elif x_line3 == 3:
        return 1
    elif o_line3 == 3:
        return 2

def dia():
    num1 = field[0][0] + field[1][1] + field[2][2]
    if num1 == "xxx":
        return 1
    elif num1 == "ooo":
        return 2
    num2 = field[2][0] + field[1][1] + field[0][2]
    if num2 == "xxx":
        return 1
    elif num2 == "ooo":
        return 2

field = []
for j in range(3):
    field.append([])
    for k in range(3):
        field[j].append("_")
for j in field:
    print(j)

while True:
    if check() == 0:
        print("tie")
        break

    if row() == 1:
        print("player 1 wins")
        break
    if row() == 2:
        print("player 2 wins")
        break

    if line() == 1:
        print("player 1 wins")
        break
    if line() == 2:
        print("player 2 wins")
        break

    if dia() == 1:
        print("player 1 wins")
        break
    if dia() == 2:
        print("player 2 wins")
        break


    print("\nplayer 1:")
    k = int(input("enter k "))
    j = int(input("enter j "))
    print("\n")

    field[j][k] = "x"
    for j in field:
        print(j)
    print('\n')

    if check() == 0:
        print("tie")
        break

    if row() == 1:
        print("player 1 wins")
        break
    if row() == 2:
        print("player 2 wins")
        break

    if line() == 1:
        print("player 1 wins")
        break
    if line() == 2:
        print("player 2 wins")
        break

    if dia() == 1:
        print("player 1 wins")
        break
    if dia() == 2:
        print("player 2 wins")
        break

    print("\nplayer 2:")
    k = int(input("enter k "))
    j = int(input("enter j "))
    print("\n")

    field[j][k] = "o"
    for j in field:
        print(j)
    print('\n')