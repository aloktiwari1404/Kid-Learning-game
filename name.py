from tkinter import *
import pics as pi

def pics():
    # global root_name
    global e9,root_name 
    temp = Entry.get(e9)
    root_name.destroy()
    pi.main(temp)


def name():
    global root_name,e9
    root_name=Tk()
    root_name.title('Kids Memory Games')
    x=Canvas(bg='cadetblue3', height=600,width=850,borderwidth=5)
    base=PhotoImage(file="cut.png")
    x.create_image(650,300,anchor=NE,image=base)
    x.pack()
    l9=Label(root_name,text='Enter your name : ',font=("times 24 bold"),bg='cadetblue3')
    e9=Entry(root_name,borderwidth=2)
    b9=Button(root_name, text='Submit',bg='cadetblue3',command=pics)    

    l9.place(x=200,y=220)
    e9.place(x=480,y=232)
    b9.place(x=500,y=282)
    root_name.mainloop()

#def collect():
    #e8=e9
