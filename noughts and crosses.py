import random

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
    elif x_row1 == 2:
        return 11

    elif x_row2 == 3:
        return 1
    elif o_row2 == 3:
        return 2
    elif x_row2 == 2:
        return 12

    elif x_row3 == 3:
        return 1
    elif o_row3 == 3:
        return 2
    elif x_row3 == 2:
        return 13

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
    elif x_line1 == 2:
        return 11

    elif x_line2 == 3:
        return 1
    elif o_line2 == 3:
        return 2
    elif x_line2 == 2:
        return 12

    elif x_line3 == 3:
        return 1
    elif o_line3 == 3:
        return 2
    elif x_line3 == 2:
        return 13

def dia():
    num1 = field[0][0] + field[1][1] + field[2][2]
    num_1 = num1.replace("_", "")
    if num1 == "xxx":
        return 1
    elif num1 == "ooo":
        return 2
    elif num_1 == "xx":
        return 11

    num2 = field[2][0] + field[1][1] + field[0][2]
    num_2 = num2.replace("_", "")
    if num2 == "xxx":
        return 1
    elif num2 == "ooo":
        return 2
    elif num_2 == "xx":
        return 12

field = []
for j in range(3):
    field.append([])
    for k in range(3):
        field[j].append("_")
for j in field:
    print(j)

while True:
    k = int(input("\nenter k "))
    j = int(input("enter j "))
    print("\n")

    field[j][k] = "x"
    for j in field:
        print(j)
    print('\n')

    print(check())

    if row() == 1:
        print("victory")
        break
    if row() == 2:
        print("game over")
        break

    if line() == 1:
        print("victory")
        break
    if line() == 2:
        print("game over")
        break

    if dia() == 1:
        print("victory")
        break
    if dia() == 2:
        print("game over")
        break

    if check() == 0:
        print("tie")
        break


    if row() == 11:
        while True:
            j = random.randrange(3)
            if field[j][0] == "_":
                field[j][0] = "o"
                for j in field:
                    print(j)
                print('\n')
                break
    elif row() == 12:
        while True:
            j = random.randrange(3)
            if field[j][1] == "_":
                field[j][1] = "o"
                for j in field:
                    print(j)
                print('\n')
                break
    elif row() == 13:
        while True:
            j = random.randrange(3)
            if field[j][2] == "_":
                field[j][2] = "o"
                for j in field:
                    print(j)
                print('\n')
                break

    elif line() == 11:
        while True:
            k = random.randrange(3)
            if field[0][k] == "_":
                field[0][k] = "o"
                for j in field:
                    print(j)
                print('\n')
                break
    elif line() == 12:
        while True:
            k = random.randrange(3)
            if field[1][k] == "_":
                field[1][k] = "o"
                for j in field:
                    print(j)
                print('\n')
                break
    elif line() == 13:
        while True:
            k = random.randrange(3)
            if field[2][k] == "_":
                field[2][k] = "o"
                for j in field:
                    print(j)
                print('\n')
                break

    elif dia() == 11:
        if field[0][0] == "_":
            field[0][0] = "o"
            for j in field:
                print(j)
            print('\n')
        if field[1][1] == "_":
            field[1][1] = "o"
            for j in field:
                print(j)
            print('\n')
        if field[2][2] == "_":
            field[2][2] = "o"
            for j in field:
                print(j)
            print('\n')
    elif dia() == 12:
        if field[2][0] == "_":
            field[2][0] = "o"
            for j in field:
                print(j)
            print('\n')
        if field[1][1] == "_":
            field[1][1] = "o"
            for j in field:
                print(j)
            print('\n')
        if field[0][2] == "_":
            field[0][2] = "o"
            for j in field:
                print(j)
            print('\n')

    else:
        while True:
            j = random.randrange(3)
            k = random.randrange(3)
            if field[j][k] == "_":
                field[j][k] = "o"
                for j in field:
                    print(j)
                print('\n')
                break

    print(check())

    if row() == 1:
        print("victory")
        break
    if row() == 2:
        print("game over")
        break

    if line() == 1:
        print("victory")
        break
    if line() == 2:
        print("game over")
        break

    if dia() == 1:
        print("victory")
        break
    if dia() == 2:
        print("game over")
        break

    if check() == 0:
        print("tie")
        break