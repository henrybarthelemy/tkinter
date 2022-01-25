from operator import add
import tkinter as tk
from tokenize import Double


###################  units
#     sdajw       #  1
#                 #  2
#    1231412      #  3
#                 #  4
#  1    2    3  + #  5 
#  4    5    6  - #  6
#  4    5    6  * #  7
#  ENTER  CLR   / #  8
###################
#  1    2    3  .5 units

#global expression initalized with nothing
expression = ""

#Is it the first number clicked since an op
firstNumberClick = True

#currently saved operation
currentOp = ""

# scale: 1 unit = 2 cells
# window = 7 cells width by 16 cells height
rows = []
for x in range(16):
    rows.append(x)

columns = []
for x in range(7):
    columns.append(x)

def one():
    global firstNumberClick
    if(firstNumberClick):
        lbl_equation["text"] = "1"
        firstNumberClick = False
    else:
        current = lbl_equation["text"]
        current = str(current) + "1"
        lbl_equation["text"] = current

def two():
    global firstNumberClick
    if(firstNumberClick):
        lbl_equation["text"] = "2"
        firstNumberClick = False
    else:
        current = lbl_equation["text"]
        current = str(current) + "2"
        lbl_equation["text"] = current

def three():
    global firstNumberClick
    if(firstNumberClick):
        lbl_equation["text"] = "3"
        firstNumberClick = False
    else:
        current = lbl_equation["text"]
        current = str(current) + "3"
        lbl_equation["text"] = current

def four():
    global firstNumberClick
    if(firstNumberClick):
        lbl_equation["text"] = "4"
        firstNumberClick = False
    else:
        current = lbl_equation["text"]
        current = str(current) + "4"
        lbl_equation["text"] = current

def five():
    global firstNumberClick
    if(firstNumberClick):
        lbl_equation["text"] = "5"
        firstNumberClick = False
    else:
        current = lbl_equation["text"]
        current = str(current) + "5"
        lbl_equation["text"] = current

def six():
    global firstNumberClick
    if(firstNumberClick):
        lbl_equation["text"] = "6"
        firstNumberClick = False
    else:
        current = lbl_equation["text"]
        current = str(current) + "6"
        lbl_equation["text"] = current

def seven():
    global firstNumberClick
    if(firstNumberClick):
        lbl_equation["text"] = "7"
        firstNumberClick = False
    else:
        current = lbl_equation["text"]
        current = str(current) + "7"
        lbl_equation["text"] = current

def eight():
    global firstNumberClick
    if(firstNumberClick):
        lbl_equation["text"] = "8"
        firstNumberClick = False
    else:
        current = lbl_equation["text"]
        current = str(current) + "8"
        lbl_equation["text"] = current

def nine():
    global firstNumberClick
    if(firstNumberClick):
        lbl_equation["text"] = "9"
        firstNumberClick = False
    else:
        current = lbl_equation["text"]
        current = str(current) + "9"
        lbl_equation["text"] = current

def zero():
    global firstNumberClick
    if(firstNumberClick):
        lbl_equation["text"] = "0"
        firstNumberClick = False
    else:
        current = lbl_equation["text"]
        current = str(current) + "0"
        lbl_equation["text"] = current

def dot():
    global firstNumberClick
    if(firstNumberClick):
        lbl_equation["text"] = "0."
        firstNumberClick = False
    elif not ("." in lbl_equation["text"]):
        current = lbl_equation["text"]
        current = str(current) + "."
        lbl_equation["text"] = current

def clear():
    global expression
    global firstNumberClick
    global currentOp
    expression = ""
    firstNumberClick = True
    currentOp = ""
    lbl_equation["text"] = ""

def plus():
    global expression
    global firstNumberClick
    global currentOp
    if(expression == ""):
        expression = lbl_equation["text"]
        firstNumberClick = True
    else:
        num1 = float(lbl_equation["text"])
        num2 = float(expression)
        answer = num1 + num2
        if (answer - int(answer)) == 0:
            answer = (int(answer))
        else:
            round(answer, 8)
        lbl_equation["text"] = str(answer)
        expression = str(answer)
        firstNumberClick = True
    currentOp = "+"

def multiply():
    global expression
    global firstNumberClick
    global currentOp
    if(expression == ""):
        expression = lbl_equation["text"]
        firstNumberClick = True
    else:
        num1 = float(lbl_equation["text"])
        num2 = float(expression)
        answer = num1 * num2
        if (answer - int(answer)) == 0:
            answer = (int(answer))
        else:
            round(answer, 8)
        lbl_equation["text"] = str(answer)
        expression = str(answer)
        firstNumberClick = True
    currentOp = "*"

def subtract():
    global expression
    global firstNumberClick
    global currentOp
    if(expression == ""):
        expression = lbl_equation["text"]
        firstNumberClick = True
    else:
        num1 = float(lbl_equation["text"])
        num2 = float(expression)
        answer = num2 - num1
        if (answer - int(answer)) == 0:
            answer = (int(answer))
        else:
            round(answer, 8)
        lbl_equation["text"] = str(answer)
        expression = str(answer)
        firstNumberClick = True
    currentOp = "-"

def divide():
    global expression
    global firstNumberClick
    global currentOp
    if(expression == ""):
        expression = lbl_equation["text"]
        firstNumberClick = True
    else:
        num1 = float(lbl_equation["text"])
        num2 = float(expression)
        answer = num2 / num1
        if (answer - int(answer)) == 0:
            answer = (int(answer))
        else:
            round(answer, 8)
        lbl_equation["text"] = str(answer)
        expression = str(answer)
        firstNumberClick = True
    currentOp = "/"

def equal():
    global expression
    global firstNumberClick
    global currentOp
    if not (expression == "" or currentOp == ""):
        if(currentOp == "+"):
            plus()
        if(currentOp == "-"):
            subtract()
        if(currentOp == "*"):
            multiply()
        if(currentOp == "/"):
            divide()
    expression = ""
   

window = tk.Tk()
window.title("Python Tkinter Calculator GUI")
window.rowconfigure(rows, minsize=25, weight=1)
window.columnconfigure(columns, minsize=40, weight=1)

lbl_title = tk.Label(master=window, text="Calculator GUI", font=('Arial', 25, 'bold'), fg="lightskyblue")
lbl_title.grid(row=0, column=0, columnspan=7, rowspan = 2)

lbl_equation = tk.Label(master=window, text="", font=('Time\'s New Roman', 20, 'bold'))
lbl_equation.grid(row=2, column=0, columnspan=7, rowspan = 3)

btn_1 = tk.Button(master=window, text="1", command=one)
btn_1.grid(row=8, rowspan=2, column=0, columnspan=2, sticky="nsew")

btn_2 = tk.Button(master=window, text="2", command=two)
btn_2.grid(row=8, rowspan=2, column=2, columnspan=2, sticky="nsew")

btn_3 = tk.Button(master=window, text="3", command=three)
btn_3.grid(row=8, rowspan=2, column=4, columnspan=2, sticky="nsew")

btn_4 = tk.Button(master=window, text="4", command=four)
btn_4.grid(row=10, rowspan=2, column=0, columnspan=2, sticky="nsew")

btn_5 = tk.Button(master=window, text="5", command=five)
btn_5.grid(row=10, rowspan=2, column=2, columnspan=2, sticky="nsew")

btn_6 = tk.Button(master=window, text="6", command=six)
btn_6.grid(row=10, rowspan=2, column=4, columnspan=2, sticky="nsew")

btn_7 = tk.Button(master=window, text="7", command=seven)
btn_7.grid(row=12, rowspan=2, column=0, columnspan=2, sticky="nsew")

btn_8 = tk.Button(master=window, text="8", command=eight)
btn_8.grid(row=12, rowspan=2, column=2, columnspan=2, sticky="nsew")

btn_9 = tk.Button(master=window, text="9", command=nine)
btn_9.grid(row=12, rowspan=2, column=4, columnspan=2, sticky="nsew")

btn_0 = tk.Button(master=window, text="0", command=zero)
btn_0.grid(row=14, rowspan=2, column=0, columnspan=4, sticky="nsew")

btn_mult = tk.Button(master=window, text="*", command=multiply)
btn_mult.grid(row=8, rowspan=2, column=6, columnspan=2, sticky="nsew")

btn_plus = tk.Button(master=window, text="+", command=plus)
btn_plus.grid(row=12, rowspan=2, column=6, columnspan=2, sticky="nsew")

btn_subtract = tk.Button(master=window, text="-", command=subtract)
btn_subtract.grid(row=10, rowspan=2, column=6, columnspan=2, sticky="nsew")

btn_divide = tk.Button(master=window, text="/", command=divide)
btn_divide.grid(row=6, rowspan=2, column=6, columnspan=2, sticky="nsew")

btn_clear = tk.Button(master=window, text="C", command=clear)
btn_clear.grid(row=6, rowspan=2, column=0, columnspan=6, sticky="nsew")

btn_dot = tk.Button(master=window, text=".", command=dot)
btn_dot.grid(row=14, rowspan=2, column=4, columnspan=2, sticky="nsew")

btn_equal = tk.Button(master=window, text="=", command=equal)
btn_equal.grid(row=14, rowspan=2, column=6, columnspan=1, sticky="nsew")


def keydown(e):
    key = str(e.char)
    if(key == "1"):
        one()
    elif(key == "2"):
        two()
    elif(key == "3"):
        three()
    elif(key == "4"):
        four()
    elif(key == "5"):
        five()
    elif(key == "6"):
        six()
    elif(key == "7"):
        seven()
    elif(key == "8"):
        eight()
    elif(key == "9"):
        nine()
    elif(key == "0"):
        zero()
    elif(key == "="):
        equal()
    elif(key == "+"):
        plus()
    elif(key == "-"):
        subtract()
    elif(key == "c"):
        clear()
    elif(key == "C"):
        clear()
    elif(key == "/"):
        divide()
    elif(key == "*"):
        multiply()
    elif(key == "."):
        dot()
    elif(e.keycode == 603979789): #keycode for return
        equal()
    



window.bind("<KeyPress>", keydown)
window.focus_set()

window.mainloop()
