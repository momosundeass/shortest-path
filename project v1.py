from Tkinter import *
master = Tk()
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
node1, node2 = list(), []
line, graph = list(), []
graph_dic = dict()
i2 = 0
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
            
######################### Third Frame
def changeposmodule(event):
    if len(w_dot) != 0:
        w.move(w_dot[i-1], event.x-w_pos[i-1].x, event.y-w_pos[i-1].y)
        w.move(w_name[i-1], event.x-w_pos[i-1].x, event.y-w_pos[i-1].y)
        w_pos[i-1] = Position(event.x, event.y)
        line_destroy()
def calcu():
    global graph_dic
    print graph_dic
    print p1.get()
    print p2.get()
    temp = find_shortest_path(graph_dic, p1.get(), p2.get(), path=[])
    Label(master, text=str(temp)).grid(column=3,row=3)
Label(master, text='From(Number)').grid(row=0, column=3, sticky=W)
p1 = Entry(master, width=2)
p1.grid(row=0, column=3, sticky=W, padx=100)
Label(master, text='To(Number)').grid(row=0, column=3, sticky=W, padx=120)
p2 = Entry(master, width=2)
p2.grid(row=0, column=3, sticky=W, padx=200)
Button(master, text='Calculate', command=calcu).grid(row=0, column=3, sticky=E)
w = Canvas(master, width=600, height=600, bg='PINK')
w.grid(row=2, rowspan=1000, column=3)
w.bind("<Button-1>", changeposmodule)

######################### First Frame
def add_button():
    global i
    a.append(Label(ftop, text='Node'+'%02d' % int(1+i)))
    b.append(Entry(ftop))
    w_pos.append(Position(300, 300))
    w_dot.append(w.create_rectangle(w_pos[i].x-2, w_pos[i].y-2, w_pos[i].x+2, w_pos[i].y+2, fill='BLACK'))
    w_name.append(w.create_text(300, 290, text=str(i+1)))
    a[i].grid(row=i+1, column=0, sticky=W)
    b[i].grid(row=i+1, padx=30, sticky=E)
    line_destroy()
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
        line_destroy()
        i -= 1
ftop = Frame(master).grid(row=0)
Button(ftop, text="Add Node", command=add_button).grid(row=0, sticky=W)
Button(ftop, text="Delete Node", command=del_button).grid(row=0, sticky=W, padx=70)


######################### Second Frame
def add_line():
    global i2
    a2.append(Entry(f2top,width=5))
    b2.append(Entry(f2top,width=5))
    a2[i2].grid(row=i2+2, column=2, sticky=W)
    b2[i2].grid(row=i2+2, column=2, sticky=W, padx=50)
    line_destroy()
    i2 += 1
def del_line():
    global i2
    if len(a2) != 0 and len(b2) != 0:
        line_destroy()
        a2[i2-1].destroy()
        a2.pop()
        b2[i2-1].destroy()
        b2.pop()
        i2 -= 1
def line_c():
    global graph
    global graph_dic
    if len(a) >= 2:
        for j in range(len(a2)):
            line.append(w.create_line(w_pos[int(a2[j].get())-1].x, w_pos[int(a2[j].get())-1].y, w_pos[int(b2[j].get())-1].x, w_pos[int(b2[j].get())-1].y))
            graph.append([a2[j].get(), b2[j].get()])
            graph.append([b2[j].get(), a2[j].get()])
        graph_dic = convert_list_dict(graph)
    print graph_dic
f2top = Frame(master).grid(row=0 ,column=2)
Button(f2top, text="add_line", command=add_line).grid(row=0, column=2, sticky=W)
Button(f2top, text="del_line", command=del_line).grid(row=0, column=2, sticky=W, padx=60)
Label(f2top, text='Node To').grid(row=1, column=2, sticky=W)
Label(f2top, text='Node').grid(row=1, column=2, sticky=W, padx=50)
Button(f2top, text='create line', command=line_c).grid(row=0, column=2, sticky=W, padx=115)

master.mainloop()
