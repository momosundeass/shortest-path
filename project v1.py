from Tkinter import *
from random import *
master = Tk()
master.title('Shortest Path')
######################### Class Area

class Position:
    def __init__(self, posx, posy):
        self.x = posx
        self.y = posy
        
######################### Variable area
        
a, b = list(), []
i = 0
w_dot, w_name, w_pos = list(), [], []
a2, b2 = list(), []
i2 = 0
node1, node2 = list(), []
line, graph = list(), []
graph_dic = dict()

######################### Function area

def line_destroy():
    global line
    global graph
    global graph_dic
    if len(line) > 0:
        for d in line:
            w.delete(d)
        line = []
        graph = []
        graph_dic = dict()
        
def z(flash ,ino=0, string='', num=0):
    if ino == 0:
        flash = int(flash)
        if flash / 26 != 0 and flash != 26:
            if flash % 26 == 0:
                string += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[(flash / 26) - 2]
            else:
                string += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[(flash / 26) - 1]
        string += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[(flash % 26) - 1]
        return string
    else:
        if len(flash) == 2:
            num += ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(flash[0])+1) * 26
        num += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(flash[-1])+1
        return str(num)
    
def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def convert_list_dict(lis):
    dic = dict()
    for c in lis:
        if c[0] not in dic:
            dic[c[0]] = [c[1]]
        else:
            dic[c[0]] += [c[1]]
    return dic

def answer(ans):
    global w_pos
    root = Tk()
    root.title('Answer')
    we = Canvas(root, width=500, height=500, bg='#99FFFF')
    path = 'Path ::: ' + str(ans[0])
    for o in range(len(ans)-1):
        path = path + ' > ' + str(ans[o+1])
    Label(root, text=path).pack()
    we.pack()
    for o in range(len(w_pos)):
        we.create_rectangle(w_pos[o].x-2, w_pos[o].y-2, w_pos[o].x+2, w_pos[o].y+2, fill='BLACK')
        we.create_text(w_pos[o].x, w_pos[o].y - 10, text=z(o+1))
    for o in range(len(ans)-1):
        we.create_line(w_pos[int(z(ans[o], ino=1))-1].x, w_pos[int(z(ans[o], ino=1))-1].y,\
                        w_pos[int(z(ans[o+1], ino=1))-1].x, w_pos[int(z(ans[o+1], ino=1))-1].y)
    root.mainloop()
def updownchange():
    botup.grid(row=i+1, column=0, sticky=E, padx=20)
    botdown.grid(row=i+1, column=0, sticky=E, padx=40)
    if len(a) == 0:
        botup.grid_remove()
        botdown.grid_remove()
######################### Third Frame
def changeposmodule(event):
    if len(w_dot) != 0:
        w.move(w_dot[i-1], event.x-w_pos[i-1].x, event.y-w_pos[i-1].y)
        w.move(w_name[i-1], event.x-w_pos[i-1].x, event.y-w_pos[i-1].y)
        w_pos[i-1] = Position(event.x, event.y)
        line_destroy()
def calcu():
    global graph_dic
    temp = find_shortest_path(graph_dic, p1.get(), p2.get(), path=[])
    if temp != None:
        answer(temp)
Label(master, text='Find Shortest Path From').grid(row=0, column=3, sticky=W)
p1 = Entry(master, width=2)
p1.grid(row=0, column=3, sticky=W, padx=135)
Label(master, text='To').grid(row=0, column=3, sticky=W, padx=155)
p2 = Entry(master, width=2)
p2.grid(row=0, column=3, sticky=W, padx=175)
Button(master, text='Calculate', command=calcu).grid(row=0, column=3, sticky=E)
w = Canvas(master, width=500, height=500, bg='#99FFFF')
w.grid(row=1, rowspan=1000, column=3)
w.bind("<Button-1>", changeposmodule)

######################### First Frame
def add_button():
    global i
    if len(a) != 0:
        a[i-1].config(fg='BLACK')
    i = len(a)
    a.append(Label(ftop, text=z(i+1)))
    b.append(Entry(ftop))
    pos = Position(randrange(50, 450), randrange(50, 450))
    w_pos.append(Position(pos.x, pos.y))
    w_dot.append(w.create_rectangle(w_pos[i].x-2, w_pos[i].y-2, w_pos[i].x+2, w_pos[i].y+2, fill='BLACK'))
    w_name.append(w.create_text(pos.x, pos.y - 10, text=z(i+1) ))
    a[i].grid(row=i+2, column=0, sticky=W)
    b[i].grid(row=i+2, padx=30, sticky=W)
    botup.grid_remove()
    botdown.grid_remove()
    botup.grid(row=i+2, column=0, sticky=E, padx=20)
    botdown.grid(row=i+2, column=0, sticky=E, padx=40)
    a[i].config(fg='RED')
    if len(a) > 1:
        a[i-1].config(fg='BLACK')
    line_destroy()
    i += 1
def del_button():
    global i
    if len(a) != 0 and len(b) != 0:
        a[i-1].config(fg='BLACK')
        i = len(a)
        a[i-1].destroy()
        a.pop()
        b[i-1].destroy()
        b.pop()
        w.delete(w_dot[i-1])
        w_dot.pop()
        w.delete(w_name[i-1])
        w_name.pop()
        w_pos.pop()
        botup.grid_remove()
        botdown.grid_remove()
        botup.grid(row=i, column=0, sticky=E, padx=20)
        botdown.grid(row=i, column=0, sticky=E, padx=40)
        if len(a) == 0:
            botup.grid_remove()
            botdown.grid_remove()
        line_destroy()
        i -= 1
        if len(a) > 0:
            a[i-1].config(fg='RED')
def i_change_up():
    global i
    if i > 1 and i <= len(a):  
        i -= 1
        a[i].config(fg='BLACK')
        a[i-1].config(fg='RED')
        updownchange()
def i_change_down():
    global i
    if i > -1 and i < len(a):
        a[i-1].config(fg='BLACK')
        i += 1
        a[i-1].config(fg='RED')
        updownchange()
ftop = Frame(master).grid(row=0)
Label(ftop, text='Comment').grid(row=1)
Button(ftop, text="Add Node", command=add_button).grid(row=0, sticky=W)
Button(ftop, text="Delete Node", command=del_button).grid(row=0, sticky=W, padx=70)
botup = Button(ftop, text='^', command=i_change_up)
botdown = Button(ftop, text='v', command=i_change_down)

######################### Second Frame
def add_line():
    global i2
    global d
    a2.append(Entry(f2top,width=5))
    b2.append(Entry(f2top,width=5))
    a2[i2].grid(row=i2+2, column=2, sticky=W)
    b2[i2].grid(row=i2+2, column=2, sticky=W, padx=50)
    line_destroy()
    d.grid_remove()
    d.grid(row=i2+2, column=2, sticky=E)
    i2 += 1
def del_line():
    global i2
    if len(a2) != 0 and len(b2) != 0:
        line_destroy()
        a2[i2-1].destroy()
        a2.pop()
        b2[i2-1].destroy()
        b2.pop()
        d.grid_remove()
        d.grid(row=i2, column=2, sticky=E)
        if len(a2) == 0:
            d.grid_remove()
        i2 -= 1
def line_c():
    global graph
    global graph_dic
    global line
    global warning_flag
    if len(a) >= 2:
        for j in line:
            w.delete(j)
        line = []
        
        for j in range(len(a2)):
            if a2[j].get() == '' or b2[j].get() == '':
                break
            line.append(w.create_line(w_pos[int(z(a2[j].get(), ino=1))-1].x, w_pos[int(z(a2[j].get(), ino=1))-1].y,\
                                      w_pos[int(z(b2[j].get(), ino=1))-1].x, w_pos[int(z(b2[j].get(), ino=1))-1].y))
            graph.append([a2[j].get(), b2[j].get()])
            graph.append([b2[j].get(), a2[j].get()])
        graph_dic = convert_list_dict(graph)
f2top = Frame(master).grid(row=0 ,column=2)
Button(f2top, text="add_line", command=add_line).grid(row=0, column=2, sticky=W)
Button(f2top, text="del_line", command=del_line).grid(row=0, column=2, sticky=W, padx=60)
Label(f2top, text='Node To').grid(row=1, column=2, sticky=W)
Label(f2top, text='Node').grid(row=1, column=2, sticky=W, padx=50)
d = Button(f2top, text='create line', command=line_c)

master.mainloop()
