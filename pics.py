from tkinter import*
import random
import time
import opt as op

def select_opt():
    global a,b,c,d,root123,name_in
    print('#',a,b,c,d,'#')
    root123.destroy()
    op.main_opt(a,b,c,d,name_in)

def ran():
    print('inside ran')
    global a,b,c,d
    a = random.randint(0,9)
    b= random.randint(0,9)
    while b == a:
        b= random.randint(0,9)
    c= random.randint(0,9)
    while c == a or c == b:   
        c= random.randint(0,9)
    d= random.randint(0,9) 
    while d == a or d == b or d == c:   
        d= random.randint(0,9)
 
def coord():
    global x1,y1,count
    if count == 1:
        x1,y1=250,90
    if count == 2:
        x1,y1=500,90
    if count == 3:
        x1,y1=740,90
    if count == 4:
        x1,y1=280,250
    if count == 5:
        x1,y1=530,250
    if count == 6:
        x1,y1=780,250

def refresh():
    global root123
    root123.destroy()
    main(name_in)
    
def main(name):
    global x1,y1,count,a,b,c,d,root123,name_in
    name_in=name
    name = 'welcome ' + name
    root123=Tk()    
    a,b,c,d= 0,0,0,0
    x1,y1,count= 0,0,0
    ran()
    print (a,b,c,d)
    root123.title(name)
    c1=Canvas(root123, bg='grey',height=600, width=900)
    id=c1.create_rectangle(50,40,850,560, width=2, fill='lightgrey')
    
    file1=PhotoImage(file="brd.gif")
    file2=PhotoImage(file="cat-icon.gif")
    file3=PhotoImage(file="car2.gif")
    file4=PhotoImage(file="earth.gif")
    file5=PhotoImage(file="rabbit.gif")
    file6=PhotoImage(file="MONKEY1.gif")
    file7=PhotoImage(file="dog.gif")
    file8=PhotoImage(file="truck1.gif")
    file9=PhotoImage(file="lion.gif")
    file10=PhotoImage(file="plane.gif")

    for i in range(10):
        if i is not a and i is not b and i is not c and i is not d:
            print(i)
            if i == 0:
                count+=1
                coord()
                c1.create_image(x1,y1,anchor=NE, image=file1, activeimage=file1)
            if i == 1:
                count+=1
                coord()
                c1.create_image(x1,y1,anchor=NE, image=file2, activeimage=file2)
            if i == 2:
                count+=1
                coord()
                c1.create_image(x1,y1,anchor=NE, image=file3, activeimage=file3)
            if i == 3:
                count+=1
                coord()
                c1.create_image(x1,y1,anchor=NE, image=file4, activeimage=file4)
            if i == 4:
                count+=1
                coord()
                c1.create_image(x1,y1,anchor=NE, image=file5, activeimage=file5)
            if i == 5:
                count+=1
                coord()
                c1.create_image(x1,y1,anchor=NE, image=file6, activeimage=file6)
            if i == 6:
                count+=1
                coord()
                c1.create_image(x1,y1,anchor=NE, image=file7, activeimage=file7)
            if i == 7:
                count+=1
                coord()
                c1.create_image(x1,y1,anchor=NE, image=file8, activeimage=file8)
            if i == 8:
                count+=1
                coord()
                c1.create_image(x1,y1,anchor=NE, image=file9, activeimage=file9)
            if i == 9:
                count+=1
                coord()
                c1.create_image(x1,y1,anchor=NE, image=file10, activeimage=file10)
    c1.pack()
    b1=Button(root123, text='OK', width=15, height=2 ,bg='white', font=('Georgia', 12),
         fg='black', activebackground='lightgrey', activeforeground='blue',command=select_opt)
    b2=Button(root123, text='Refresh', width=15, height=2 ,bg='white', font=('Georgia', 12),
         fg='black', activebackground='lightgrey', activeforeground='blue',command=refresh) 
    b1.place(x=500, y=450)
    b2.place(x=300, y=450)
    #root123.geometry('400x300')
    root123.mainloop()
