from tkinter import*
import sys
import name as na

def name_open():
    global root_home
    root_home.destroy()
    na.name()


root_home=Tk()
root_home.title('Kids Memory Games')
c=Canvas(bg='white', height=600,width=850,borderwidth=5)
homepic=PhotoImage(file="logo.gif")
c.create_image(850,10,anchor=NE,image=homepic)
c.pack()

b1=Button(root_home, text='START', width=15, height=2 ,bg='lightblue', font=('Georgia', 12),
         fg='black', activebackground='lightgrey', activeforeground='blue',command=name_open)
#b2=Button(root_home, text='VIEW SCORES', width=15, height=2 ,bg='lightblue', font=('Georgia', 12),
         #fg='black', activebackground='lightgrey', activeforeground='blue')
b3=Button(root_home, text='QUIT', width=15, height=2 ,bg='lightblue', font=('Georgia', 12),
         fg='black', activebackground='lightgrey', activeforeground='blue',command=root_home.destroy)
b1.place(x=650, y=50)
#b2.place(x=650, y=150)
b3.place(x=650, y=200)

    
#b1.place(x=50, y=150)
#b2.place(x=650, y=150)
#b3.place(x=670, y=500)
l1=Label(root_home,text='KIDS',font=("times 24 bold"),bg='cadetblue3')
l2=Label(root_home,text='LEARNING ',font=("times 24 bold"),bg='cadetblue3')
l3=Label(root_home,text='GAME',font=("times 24 bold"),bg='cadetblue3')

l1.place(x=50,y=50)
l2.place(x=50,y=120)
l3.place(x=50,y=190)

root_home.mainloop()
