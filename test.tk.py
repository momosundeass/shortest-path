from Tkinter import *
root = Tk()
lis, line = list(), list()
listt = list()
click = 0
v = StringVar()
w = Canvas(root, width=400, height=400)
w.create_line(10, 10, 10, 390)
w.create_line(10, 10, 390, 10)
w.create_line(390, 10, 390, 390)
w.create_line(390, 390, 10, 390)
text = Label(root, textvariable=v)
def callback(event):
    global click
    if event.x >= 10 and event.x <= 390 and event.y  >= 10 and event.x <= 390:
        listt.append([event.x, event.y])
        lis.append(w.create_rectangle(event.x-1, event.y-1, event.x+1, event.y+1))
        if len(lis) > 1:
            line.append(w.create_line(listt[click-1][0], listt[click-1][1], event.x, event.y))
        click += 1
def delete():
    global click
    if len(lis) != 0: 
        w.delete(lis[-1])
        if len(line) != 0:
            w.delete(line[-1])
        w.delete(listt[-1])
        listt.pop()
        if len(line) != 0:
            line.pop()
        lis.pop()
        click -= 1
        print lis, line, listt
def check():
    v.set('dot  => ' + str(len(lis)) + '  :  :  ' + 'line => ' + str(len(line)))
def delete2():
    global click
    for i in range(len(lis)):
        w.delete(lis[(i+1)*-1])
    for _ in range(len(lis)):
        lis.pop()
    for i in range(len(line)):
        w.delete(line[(i+1)*-1])
    for _ in range(len(line)):
        line.pop()
    for i in range(len(listt)):
        w.delete(listt[(i+1)*-1])
    for _ in range(len(listt)):
        listt.pop()
    click = 0
w.bind("<Button-1>", callback)
b = Button(root, text="delete", command=delete)
b2 = Button(root, text="delete all", command=delete2)
bc = Button(root, text='check', command=check)
w.pack()
b.pack(side=LEFT)
b2.pack(side=LEFT)
bc.pack(side=RIGHT)
text.pack()
root.mainloop()
