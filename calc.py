from tkinter import*
tk=Tk()
tk.geometry('260x370')
#текстове поле
ent=Entry(justify='right', font=('Consolass', 14))
ent.place(x=2,y=20, width=220, heigh=30)
#Point
Point=Button(text='.',font='14')
Point.place(x=140, y=310, width=40, heigh=40)
#0
def B0_click():
    ent.insert(END, '0')
B0=Button(text='0', font='14', command=B0_click)
B0.place(x=20, y=310, width=100, heigh=40)
#Point
def Point_click():
    ent.insert(END, '.')
Point=Button(text='.', font='14', command=Point_click)
Point.place(x=140, y=310, width=40, heigh=40)
#Plus
def Plus_click():
    global a,b
    a=float(ent.get())
    b='+'
    ent.delete(0,END)
Plus=Button(text='+',font='14',command=Plus_click)
Plus.place(x=200, y=310, width=40, heigh=40)
#1
def B1_click():
    ent.insert(END, '1')
B1=Button(text='1', font='14', command=B1_click)
B1.place(x=20, y=250, width=40, heigh=40)
#2
def B2_click():
    ent.insert(END, '2')
B2=Button(text='2', font='14', command=B2_click)
B2.place(x=80, y=250, width=40, heigh=40)
#3
def B3_click():
    ent.insert(END, '3')
B3=Button(text='3', font='14', command=B3_click)
B3.place(x=140, y=250, width=40, heigh=40)
#Minus
def Minus_click():
    global a, b
    a = float(ent.get())
    b = '-'
    ent.delete(0, END)
Minus = Button(text='-', font='14', command=Minus_click)
Minus.place(x=200, y=250, width=40, height=40)
#4
def B4_click():
    ent.insert(END, '4')
B4=Button(text='4', font='14', command=B4_click)
B4.place(x=20, y=190, width=40, heigh=40)
#5
def B5_click():
    ent.insert(END, '5')
B5=Button(text='5', font='14', command=B5_click)
B5.place(x=80, y=190, width=40, heigh=40)
#6
def B6_click():
    ent.insert(END, '6')
B6=Button(text='6', font='14', command=B6_click)
B6.place(x=140, y=190, width=40, heigh=40)
#Multiply
def Multiply_click():
    global a,b
    a = float(ent.get())
    b = '*'
    ent.delete(0, END)
Multiply = Button(text='*', font='14', command=Multiply_click)
Multiply.place(x=200, y=190, width=40, heigh=40)
#7
def B7_click():
    ent.insert(END, '7')
B7=Button(text='7', font='14', command=B7_click)
B7.place(x=20, y=130, width=40, heigh=40)
#8
def B8_click():
    ent.insert(END, '8')
B8=Button(text='8', font='14', command=B8_click)
B8.place(x=80, y=130, width=40, heigh=40)
#9
def B9_click():
    ent.insert(END, '9')
B9=Button(text='9', font='14', command=B9_click)
B9.place(x=140, y=130, width=40, heigh=40)
#Divide
def Divide_click():
    global a,b
    a = float(ent.get())
    b = '/'
    ent.delete(0, END)
Divide = Button(text='/', font='14', command=Divide_click)
Divide.place(x=200, y=130, width=40, heigh=40)
#BC
def BC_click():
    ent.delete(0,END)
BC=Button(text='c',font='14', command=BC_click)
BC.place(x=20,y=70, width=100, heigh=40)
#Equal
def Equal_click():
    global a,b
    c=float(ent.get())
    ent.delete(0,END)
    if b == '+':
        a = a + c
    elif b == '-':
        a = a - c
    elif b == '*':
        a = a * c
    elif b == '/':
        if c != 0:
            a = a / c
        else:
            ent.insert(END, "Ділення на 0 неможливе")
            return
    ent.insert(END, a)
Equal=Button(text='=', font='14', command=Equal_click)
Equal.place(x=140, y=70, width=100, heigh=40)
tk.mainloop()