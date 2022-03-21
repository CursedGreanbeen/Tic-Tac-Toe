import random

def check():
    res = 0
    for i in range(3):
        res += field[i].count("_")
    return res

def row():
    for i in range(3):
        x_row = list(zip(*field))[i].count("x")
        o_row = list(zip(*field))[i].count("o")

        if x_row == 3:
            return 1
        elif o_row == 3:
            return 2
        elif x_row == 2:
            return int('1' + str(i + 1))


def line():
    for i in range(3):
        x_line = field[i].count("x")
        o_line = field[i].count("o")

        if x_line == 3:
            return 1
        elif o_line == 3:
            return 2
        elif x_line == 2:
            return int('1' + str(i + 1))


def dia():
    dia1, dia2 = '', ''

    for i in range(3):
        dia1 += field[i][i]
        dia2 += field[i][2 - i]

    if dia1.count("x") == 3 or dia2.count("x") == 3:
        return 1
    elif dia1.count("o") == 3 or dia2.count("o") == 3:
        return 2
    elif dia1.count("x") == 2:
        return 11
    elif dia2.count("x") == 2:
        return 12


field = [['_'] * 3 for _ in range(3)]
for f in field:
    print(*f, sep=' ')
print()

endgame = {1: "victory", 2: "game over"}

while True:
    k = int(input("\nenter k "))
    j = int(input("enter j "))
    print("\n")

    field[j][k] = "x"
    for f in field:
        print(*f, sep=' ')
    print()

    if row() in endgame:
        print(endgame[row()])
        break

    if line() in endgame:
        print(endgame[line()])
        break

    if dia() in endgame:
        print(endgame[dia()])
        break

    if check() == 0:
        print("tie")
        break


    if row() == 11:
        while True:
            j = random.randrange(3)
            if field[j][0] == "_":
                field[j][0] = "o"
                for f in field:
                    print(*f, sep=' ')
                print()
                break
    elif row() == 12:
        while True:
            j = random.randrange(3)
            if field[j][1] == "_":
                field[j][1] = "o"
                for f in field:
                    print(*f, sep=' ')
                print()
                break
    elif row() == 13:
        while True:
            j = random.randrange(3)
            if field[j][2] == "_":
                field[j][2] = "o"
                for f in field:
                    print(*f, sep=' ')
                print()
                break

    elif line() == 11:
        while True:
            k = random.randrange(3)
            if field[0][k] == "_":
                field[0][k] = "o"
                for f in field:
                    print(*f, sep=' ')
                print()
                break
    elif line() == 12:
        while True:
            k = random.randrange(3)
            if field[1][k] == "_":
                field[1][k] = "o"
                for f in field:
                    print(*f, sep=' ')
                print()
                break
    elif line() == 13:
        while True:
            k = random.randrange(3)
            if field[2][k] == "_":
                field[2][k] = "o"
                for f in field:
                    print(*f, sep=' ')
                print()
                break

    elif dia() == 11:
        num = random.randrange(3)
        if field[num][num] == "_":
            field[num][num] = "o"
            for f in field:
                print(*f, sep=' ')
            print()
    elif dia() == 12:
        if field[2 - num][num] == "_":
            field[2 - num][num] = "o"
            for f in field:
                print(*f, sep=' ')
            print()

    else:
        while True:
            j = random.randrange(3)
            k = random.randrange(3)
            if field[j][k] == "_":
                field[j][k] = "o"
                for f in field:
                    print(*f, sep=' ')
                print()
                break


    if row() in endgame:
        print(endgame[row()])
        break

    if line() in endgame:
        print(endgame[line()])
        break

    if dia() in endgame:
        print(endgame[dia()])
        break

    if check() == 0:
        print("tie")
        break