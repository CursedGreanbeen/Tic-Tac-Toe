import random
from tkinter import *

clicks11 = 0
clicks12 = 0
clicks13 = 0
clicks21 = 0
clicks22 = 0
clicks23 = 0
clicks31 = 0
clicks32 = 0
clicks33 = 0

corners = clicks11 + clicks13 + clicks31 + clicks33


def check():
    result = clicks11 + clicks12 + clicks13 + clicks21 + clicks22 + clicks23 + clicks31 + clicks32 + clicks33
    if result == 9:
        return 0

def end():
    line_1 = clicks11 + clicks12 + clicks13
    line_2 = clicks21 + clicks22 + clicks23
    line_3 = clicks31 + clicks32 + clicks33

    row_1 = clicks11 + clicks21 + clicks31
    row_2 = clicks12 + clicks22 + clicks32
    row_3 = clicks13 + clicks23 + clicks33

    dia_1 = clicks11 + clicks22 + clicks33
    dia_2 = clicks13 + clicks22 + clicks31

    if line_1 == 3:
        return 1
    if line_2 == 3:
        return 1
    if line_3 == 3:
        return 1
    if row_1 == 3:
        return 1
    if row_2 == 3:
        return 1
    if row_3 == 3:
        return 1
    if dia_1 == 3:
        return 1
    if dia_2 == 3:
        return 1

def corrrners():
    while True:
        k = random.randrange(3)
        if k == 0:
            global clicks13
            if clicks13 == 0:
                btn_13.config(text="O")
                clicks13 += 1
                break
        elif k == 1:
            global clicks31
            if clicks31 == 0:
                btn_31.config(text="O")
                clicks31 += 1
                break
        elif k == 2:
            global clicks33
            if clicks33 == 0:
                btn_33.config(text="O")
                clicks33 += 1
                break

def not_corners():
    while True:
        k = random.randrange(3)
        if k == 0:
            global clicks12
            if clicks12 == 0:
                btn_12.config(text="O")
                clicks12 += 1
                break
        elif k == 1:
            global clicks21
            if clicks21 == 0:
                btn_21.config(text="O")
                clicks21 += 1
                break
        elif k == 2:
            global clicks23
            if clicks23 == 0:
                btn_23.config(text="O")
                clicks23 += 1
                break
        elif k == 3:
            global clicks32
            if clicks32 == 0:
                btn_32.config(text="O")
                clicks32 += 1
                break

def click_11():
    btn_11.config(text="X")
    global clicks11
    clicks11 += 1
    if end() != 1:
        global clicks22
        if clicks22 == 0:
            btn_22.config(text="O")
            clicks22 += 1
        elif corners < 4:
            corrrners()
        else:
            not_corners()

def click_12():
    btn_12.config(text="X")
    global clicks12
    clicks12 += 1
    if end() != 1:
        global clicks22
        if clicks22 == 0:
            btn_22.config(text="O")
            clicks22 += 1
        elif corners < 4:
            corrrners()
        else:
            not_corners()

def click_13():
    btn_13.config(text="X")
    global clicks13
    clicks13 += 1
    if end() != 1:
        global clicks22
        if clicks22 == 0:
            btn_22.config(text="O")
            clicks22 += 1
        elif corners < 4:
            corrrners()
        else:
            not_corners()

def click_21():
    btn_21.config(text="X")
    global clicks21
    clicks21 += 1
    if end() != 1:
        global clicks22
        if clicks22 == 0:
            btn_22.config(text="O")
            clicks22 += 1
        elif corners < 4:
            corrrners()
        else:
            not_corners()

def click_22():
    btn_22.config(text="X")
    global clicks22
    clicks22 += 1
    if end() != 1:
        if corners < 4:
            corrrners()
        else:
            not_corners()

def click_23():
    btn_23.config(text="X")
    global clicks23
    clicks23 += 1
    if end() != 1:
        global clicks22
        if clicks22 == 0:
            btn_22.config(text="O")
            clicks22 += 1
        elif corners < 4:
            corrrners()
        else:
            not_corners()


def click_31():
    btn_31.config(text="X")
    global clicks31
    clicks31 += 1
    if end() != 1:
        global clicks22
        if clicks22 == 0:
            btn_22.config(text="O")
            clicks22 += 1
        elif corners < 4:
            corrrners()
        else:
            not_corners()

def click_32():
    btn_32.config(text="X")
    global clicks32
    clicks32 += 1
    if end() != 1:
        global clicks22
        if clicks22 == 0:
            btn_22.config(text="O")
            clicks22 += 1
        elif corners < 4:
            corrrners()
        else:
            not_corners()

def click_33():
    btn_33.config(text="X")
    global clicks33
    clicks33 += 1
    if end() != 1:
        global clicks22
        if clicks22 == 0:
            btn_22.config(text="O")
            clicks22 += 1
        elif corners < 4:
            corrrners()
        else:
            not_corners()

while check() != 0:
    root = Tk()
    root.title("tic-tac-toe")
    root.geometry("300x305")

    btn_11 = Button(text=" ", height=4, width=8, command=click_11)
    btn_11.place(x=25, y=25)

    btn_12 = Button(text=" ", height=4, width=8, command=click_12)
    btn_12.place(x=115, y=25)

    btn_13 = Button(text=" ", height=4, width=8, command=click_13)
    btn_13.place(x=205, y=25)

    btn_21 = Button(text=" ", height=4, width=8, command=click_21)
    btn_21.place(x=25, y=115)

    btn_22 = Button(text=" ", height=4, width=8, command=click_22)
    btn_22.place(x=115, y=115)

    btn_23 = Button(text=" ", height=4, width=8, command=click_23)
    btn_23.place(x=205, y=115)

    btn_31 = Button(text=" ", height=4, width=8, command=click_31)
    btn_31.place(x=25, y=205)

    btn_32 = Button(text=" ", height=4, width=8, command=click_32)
    btn_32.place(x=115, y=205)

    btn_33 = Button(text=" ", height=4, width=8, command=click_33)
    btn_33.place(x=205, y=205)

    root.mainloop()