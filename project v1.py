from Tkinter import *
master = Tk()
######################### Class Area
######################### First Frame
a = list()
b = list()
w_dot = list()
i = 0

def add_button():
    global i
    a.append(Label(ftop, text='Node'+'%02d' % int(1+i)))
    b.append(Entry(ftop))
    a[i].grid(row=i+1, column=0, sticky=W)
    b[i].grid(row=i+1, padx=30, sticky=E)
    i += 1
def del_button():
    global i
    if len(a) != 0 and len(b) != 0:
        a[i-1].destroy()
        a.pop()
        b[i-1].destroy()
        b.pop()
        i -= 1
ftop = Frame(master).grid(row=0)
Button(ftop, text="Add Node", command=add_button).grid(row=0, sticky=W)
Button(ftop, text="Delete Node", command=del_button).grid(row=0, sticky=W, padx=70)


######################### Second Frame
a2, b2, c2 = list(), [], []
i2 = 0
def add_line():
    global i2
    a2.append(Entry(f2top,width=5))
    b2.append(Entry(f2top,width=5))
    c2.append(Entry(f2top))
    a2[i2].grid(row=i2+2, column=2, sticky=W)
    b2[i2].grid(row=i2+2, column=2, sticky=W, padx=50)
    c2[i2].grid(row=i2+2, column=2, sticky=W, padx=150)
    i2 += 1
def del_line():
    global i2
    if len(a2) != 0 and len(b2) != 0 and len(c2) != 0:
        a2[i2-1].destroy()
        a2.pop()
        b2[i2-1].destroy()
        b2.pop()
        c2[i2-1].destroy()
        c2.pop()
        i2 -= 1
f2top = Frame(master).grid(row=0 ,column=2)
Button(f2top, text="add_line", command=add_line).grid(row=0, column=2, sticky=W)
Button(f2top, text="del_line", command=del_line).grid(row=0, column=2, sticky=W, padx=60)
Label(f2top, text='Node To').grid(row=1, column=2, sticky=W)
Label(f2top, text='Node(Number)').grid(row=1, column=2, sticky=W, padx=50)
Label(f2top, text='Distance(Number)').grid(row=1, column=2, sticky=W, padx=150)

######################### Third Frame
Label(master, text='From(Number)').grid(row=0, column=3, sticky=W)
Entry(master, width=2).grid(row=0, column=3, sticky=W, padx=100)
Label(master, text='To(Number)').grid(row=0, column=3, sticky=W, padx=120)
Entry(master, width=2).grid(row=0, column=3, sticky=W, padx=200)
Button(master, text='Calculate').grid(row=0, column=3, sticky=E)
w = Canvas(master, width=400, height=400, bg='PINK')
w.grid(row=2, rowspan=1000, column=3)
master.mainloop()
