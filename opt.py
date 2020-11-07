from tkinter import*
from tkinter import messagebox

class mybuttons:
    

    def __init__(self, root,a,b,cal,d,name):
        self.a,self.b,self.cal,self.d=a,b,cal,d
        self.f=Frame(root, height=600, width=850)
        self.f.propagate(0)
        self.f.pack()
        self.name = name
        self.varcheck=[]
        self.actvar = []

        #create intvar class variables
        '''self.var = IntVar()

        self.r1=Radiobutton(self.f, bg='yellow', fg='green', font=('Georgia', 20, 'underline'),
                            text='Male', variable=self.var, value=1, command=self.display)
        self.r2=Radiobutton(self.f, bg='blue', fg='black', font=('Georgia', 20, 'underline'),
                            text='Female', variable=self.var, value=2, command=self.display)


        #attach radio buttons to the frame

        self.r1.place(x=120,y=70)
        self.r2.place(x=160,y=110)'''

        self.c=Canvas(self.f, bg='cadetblue3',height=600, width=900)
        self.id=self.c.create_rectangle(120,60,400,545, width=2, fill='white', activefill='white')
        self.id=self.c.create_line(120,105,400,105, width=2, fill='black')
        self.id=self.c.create_line(120,153,400,153, width=2, fill='black')
        self.id=self.c.create_line(120,202,400,202, width=2, fill='black')
        self.id=self.c.create_line(120,252,400,252, width=2, fill='black')
        self.id=self.c.create_line(120,302,400,302, width=2, fill='black')
        self.id=self.c.create_line(120,350,400,350, width=2, fill='black')
        self.id=self.c.create_line(120,398,400,398, width=2, fill='black')
        self.id=self.c.create_line(120,445,400,445, width=2, fill='black')
        self.id=self.c.create_line(120,496,400,496, width=2, fill='black')
        #self.id=self.c.create_rectangle(620,210,740,250, width=2, fill='white', activefill='yellow')

        self.c.pack()
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        self.var7 = IntVar()
        self.var8 = IntVar()
        self.var9 = IntVar()
        self.var10 = IntVar()

        self.c1=Checkbutton(self.f, bg='white', fg='green', font=('Georgia', 18),
                            text='Bird', variable=self.var1, command=self.display)
        self.c2=Checkbutton(self.f, bg='white', fg='green', font=('Georgia', 18),
                            text='Cat',variable=self.var2, command=self.display)
        self.c3=Checkbutton(self.f, bg='white', fg='green', font=('Georgia', 18), 
                            text='Car', variable=self.var3, command=self.display)
        self.c4=Checkbutton(self.f, bg='white', fg='green', font=('Georgia', 18), 
                            text='Earth', variable=self.var4, command=self.display)
        self.c5=Checkbutton(self.f, bg='white', fg='green', font=('Georgia', 18), 
                            text='Rabbit', variable=self.var5, command=self.display)
        self.c6=Checkbutton(self.f, bg='white', fg='green', font=('Georgia', 18), 
                            text='Monkey', variable=self.var6, command=self.display)
        self.c7=Checkbutton(self.f, bg='white', fg='green', font=('Georgia', 18),
                            text='Dog', variable=self.var7, command=self.display)
        self.c8=Checkbutton(self.f, bg='white', fg='green', font=('Georgia', 18),
                            text='Truck',variable=self.var8, command=self.display)
        self.c9=Checkbutton(self.f, bg='white', fg='green', font=('Georgia', 18), 
                            text='Tiger', variable=self.var9, command=self.display)
        self.c10=Checkbutton(self.f, bg='white', fg='green', font=('Georgia', 18), 
                            text='Aeroplane', variable=self.var10, command=self.display)

        self.b1=Button(self.f,fg='black', bg='yellow', font=('Georgia', 18), #'underline')
                        activebackground='lightblue', activeforeground='red', text='Submit',command=self.check_final)


        #attach radio buttons to the frame

        self.c1.place(x=170,y=62)
        self.c2.place(x=170,y=110)
        self.c3.place(x=170,y=157)
        self.c4.place(x=170,y=207)
        self.c5.place(x=170,y=257)
        self.c6.place(x=170,y=305)
        self.c7.place(x=170,y=355)
        self.c8.place(x=170,y=400)
        self.c9.place(x=170,y=450)
        self.c10.place(x=170,y=500)
        self.b1.place(x=640,y=230)

    def check(self,num):
        print(num,'k')
        if num == 0 and self.var1.get() == 1:
            return True
        elif num == 1 and self.var2.get() == 1:
            #print ('test')
            return True
        elif num == 2 and self.var3.get() == 1:
            return True
        elif num == 3 and self.var4.get() == 1:
            #print ('test')
            return True
        elif num == 4 and self.var5.get() == 1:
            return True
        elif num == 5 and self.var6.get() == 1:
            #print ('test')
            return True
        elif num == 6 and self.var7.get() == 1:
            return True
        elif num == 7 and self.var8.get() == 1:
            #print ('test')
            return True
        elif num == 8 and self.var9.get() == 1:
            return True
        elif num == 9 and self.var10.get() == 1:
            return True
        else:
            return False

    def check_final(self):
        for i in range(10):
            if self.check(i):
                self.varcheck.append(i)
            if i != self.a and i != self.b and i!= self.cal and i != self.d:
                self.actvar.append(i)

        count_check=True

        if self.varcheck != self.actvar:
            count_check = False

        if count_check == False:
            messagebox.showinfo('sorry -'+self.name,'Better luck next time')
            print("you loose")
        else:
            messagebox.showinfo('congrats!!! -'+self.name,'Winner Winner Chicken Dinner')
            print("you win")


    def display(self):
            #retrieve the control variable
        x=self.var1.get()
        y=self.var2.get()
        z=self.var3.get()
        a=self.var4.get()
        b=self.var5.get()
        c=self.var6.get()
        p=self.var7.get()
        q=self.var8.get()
        r=self.var9.get()
        s=self.var10.get()

        

            #string is empty initially

        str=''
            #catch user choice

        if x==1:
            str+= 'you selected: bird, '
            
        if y==1:
            str+= 'you selected: cat, '
            
        if z==1:
            str+= 'you selected: car, '
            
        if a==1:
            str+= 'you selected: earth, '
            
        if b==1:
            str+= 'you selected: rabbit, '
            
        if c==1:
            str+= 'you selected: monkey, '    

        if p==1:
            str+= 'you selected: dog, '
            
        if q==1:
            str+= 'you selected: truck, '
            
        if r==1:
            str+= 'you selected: tiger, '
            
        if s==1:
            str+= 'you selected: aeroplane, ' 

        print (str)           
    

        #lbl = Label(text=str, fg='blue').place(x=50, y=150, width=200, height=20)
def main_opt(a,b,cal,d,name):           
    root=Tk()
    print(a,b,cal,d)
    
   
    mb=mybuttons(root,a,b,cal,d,name)
    root.mainloop()
#main_opt(1,3,5,7)
