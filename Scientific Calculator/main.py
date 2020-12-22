
#scientific Calculator

# imports

from tkinter import *
import parser
import math


# MAIN SCREEN

root = Tk()
root = root
root.title("Calculator")
root.geometry("308x535")
root.configure(bg="black")
root.resizable(20,20)

# The all Values and Functions

i = 0
def get_value(num):
    global i
    display.insert(i,num)
    i += 1

def clear_all():
    display.delete(0,END)


def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"ERROR")


def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string [: -1]
        clear_all()
        display.insert(0,new_string)

def sqrt():
    num = float(display.get())
    nums = math.sqrt(num)
    clear_all()
    display.insert(0,nums)


def factorial():
    num = int(display.get())
    nums = math.factorial(num)
    clear_all()
    display.insert(0,nums)

def sin_degree():
    num = float(display.get())
    nums = math. sin(num)
    clear_all()
    display.insert(0, nums)


def cos_degree():
    num = float(display.get())
    nums = math. cos(num)
    clear_all()
    display.insert(0, nums)

def tan_degree():
    num = float(display.get())
    nums = math. tan(num)
    clear_all()
    display.insert(0, nums)

def logarithm():
    num = float(display.get())
    nums = math.log(num)
    clear_all()
    display.insert(0,nums)

def expression():
    num = float(display.get())
    nums = math.exp(num)
    clear_all()
    display.insert(0, nums)


def percentage():
    whole = float(display.get())
    int(float(str(get_operater("%"))))
    num = float(display.get())
    nums = whole / num * 100
    clear_all()
    display.insert(0,nums)



def get_operater(operator):
    global i
    Length = len(operator)
    display.insert(i,operator)
    i += Length






# the input feed
display = Entry(root)
display.grid(row=1,column= 6,sticky= W + E)


# Making the buttons or the functions

add = Button(text="+",fg="black",height= 7,width=5,command= lambda : get_operater("+")).place(x=200,y = 180)
point = Button(text=".",fg="black",height= 3,width=6,command= lambda : get_value(".")).place(x= 140,y=290)
equal_to = Button(text="=",fg="black",height= 2,width=13,command= lambda :calculate()).place(x=200,y =300)
subtract = Button(text="-",fg="black",height= 2,width=6,command= lambda : get_operater("-")).place(x= 250,y =250)
multiply = Button(text="x",fg="black",height= 2,width=6,command = lambda : get_operater("*")).place(x= 250,y =205)
division = Button(text="/",fg="black",height= 2,width=6,command= lambda : get_operater("/")).place(x= 250,y =160)
pi = Button(text="pi",fg="black",height= 3,width=6,command= lambda :get_operater("*3.14")).place(x=20,y =290)
backspace = Button(text="<[x]",fg="red",height= 2,width=6,command= lambda : undo()).place(x=250,y =115)
clear = Button(text="CE",fg="blue",height= 3,width=5,command= lambda :clear_all()).place(x=200,y = 115)
square =  Button(text="2^",fg="black",height= 3,width=6,command= lambda :get_operater("**2")).place(x=20,y =350)
space = Button(text="space",fg="black",height= 3,width=20,command= lambda :get_value("  ")).place(x= 80,y = 470)
open_parenthesis = Button(text="(",fg="black",height= 3,width=6,command= lambda :get_operater("(")).place(x= 200,y = 350)
close_parenthesis = Button(text=")",fg="black",height= 3,width=5,command= lambda :get_operater(")")).place(x= 260,y =350)
factor= Button(text = "factorial",fg = "black",height=3,width = 6,command= lambda : factorial()).place(x= 80,y = 350)
sqrt_root = Button(text="sqrt",fg="black",height= 3,width=6,command= lambda : sqrt()).place(x= 140,y =350)
percentile =  Button(text="%", fg="black", height= 3, width=8, command= lambda : percentage()).place(x=20, y =410)
sin =  Button(text="sin",fg="black",height= 3,width=8,command= lambda : sin_degree()).place(x= 90,y = 410)
cos = Button(text="cos",fg="black",height= 3,width=8,command= lambda : cos_degree()).place(x= 160,y =410)
tan = Button(text="tan",fg="black",height= 3,width= 8,command= lambda : tan_degree()).place(x= 230,y =410)
log =  Button(text="log",fg="black",height= 3,width=6,command= lambda : logarithm()).place(x=20,y =470)
exp = Button(text="exp",fg="black",height= 3,width= 6,command= lambda : expression()).place(x= 240,y =470)


three = Button(text="3",fg="black",height= 3,width=6,command= lambda : get_value(3)).place(x= 140,y =230)
two = Button(text="2",fg="black",height= 3,width=6,command= lambda : get_value(2)).place(x=80,y =230)
one = Button(text="1",fg="black",height= 3,width=6,command= lambda : get_value(1)).place(x=20,y =230)
six = Button(text="6",fg="black",height= 3,width=6,command= lambda : get_value(6)).place(x= 140,y =170)
five = Button(text="5",fg="black",height= 3,width=6,command= lambda : get_value(5)).place(x=80,y =170)
four = Button(text="4",fg="black",height= 3,width=6,command= lambda : get_value(int(4))).place(x=20,y =170)
nine = Button(text="9",fg="black",height= 3,width=6,command= lambda : get_value(9)).place(x= 140,y = 110)
eight = Button(text="8",fg="black",height= 3,width=6,command= lambda : get_value(8)).place(x=80,y =110)
seven = Button(text="7",fg="black",height= 3,width=6,command= lambda : get_value(7)).place(x=20,y =110)
zero = Button(text="0",fg="black",height= 3,width=6,command= lambda : get_value(0)).place(x=80,y =290)





root.mainloop()






