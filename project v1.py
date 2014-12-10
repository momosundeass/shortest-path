from Tkinter import *
master = Tk()
######################### Class Area
class Position:
    def __init__(self, posx, posy):
        self.x = posx
        self.y = posy
class Line:
    def __init__(self, node1, node2, distance):
        self.node1 = node1
        self.node2 = node2
        self.dis = distance
    
######################### Variable area
a, b = list(), []
i = 0
w_dot, w_name, w_pos = list(), [], []
a2, b2, c2, d2 = list(), [], [], []
i2 = 0
######################### Third Frame
def changeposmodule(event):
    if len(w_dot) != 0:
        w.move(w_dot[i-1], event.x-w_pos[i-1].x, event.y-w_pos[i-1].y)
        w.move(w_name[i-1], event.x-w_pos[i-1].x, event.y-w_pos[i-1].y)
        w_pos[i-1] = Position(event.x, event.y)
        
Label(master, text='From(Number)').grid(row=0, column=3, sticky=W)
Entry(master, width=2).grid(row=0, column=3, sticky=W, padx=100)
Label(master, text='To(Number)').grid(row=0, column=3, sticky=W, padx=120)
Entry(master, width=2).grid(row=0, column=3, sticky=W, padx=200)
Button(master, text='Calculate').grid(row=0, column=3, sticky=E)
w = Canvas(master, width=400, height=400, bg='PINK')
w.grid(row=2, rowspan=1000, column=3)
w.bind("<Button-1>", changeposmodule)

######################### First Frame
def add_button():
    global i
    a.append(Label(ftop, text='Node'+'%02d' % int(1+i)))
    b.append(Entry(ftop))
    w_pos.append(Position(200, 200))
    w_dot.append(w.create_rectangle(w_pos[i].x-2, w_pos[i].y-2, w_pos[i].x+2, w_pos[i].y+2, fill='BLACK'))
    w_name.append(w.create_text(200, 190, text=str(i+1)))
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
        w.delete(w_dot[i-1])
        w_dot.pop()
        w.delete(w_name[i-1])
        w_name.pop()
        w_pos.pop()
        i -= 1
ftop = Frame(master).grid(row=0)
Button(ftop, text="Add Node", command=add_button).grid(row=0, sticky=W)
Button(ftop, text="Delete Node", command=del_button).grid(row=0, sticky=W, padx=70)


######################### Second Frame
def add_line():
    global i2
    a2.append(Entry(f2top,width=5))
    b2.append(Entry(f2top,width=5))
    c2.append(Entry(f2top,width=7))
    d2.append(Button(f2top, text='create line'))
    a2[i2].grid(row=i2+2, column=2, sticky=W)
    b2[i2].grid(row=i2+2, column=2, sticky=W, padx=50)
    c2[i2].grid(row=i2+2, column=2, sticky=W, padx=90)
    d2[i2].grid(row=i2+2, column=2, sticky=W, padx=140)
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
        d2[i2-1].destroy()
        d2.pop()
        i2 -= 1
f2top = Frame(master).grid(row=0 ,column=2)
Button(f2top, text="add_line", command=add_line).grid(row=0, column=2, sticky=W)
Button(f2top, text="del_line", command=del_line).grid(row=0, column=2, sticky=W, padx=60)
Label(f2top, text='Node To').grid(row=1, column=2, sticky=W)
Label(f2top, text='Node').grid(row=1, column=2, sticky=W, padx=50)
Label(f2top, text='Distance(Number)').grid(row=1, column=2, sticky=W, padx=90)

master.mainloop()
