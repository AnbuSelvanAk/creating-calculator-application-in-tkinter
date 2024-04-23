from tkinter import *
class file:
    def __init__(self,c):
        selfl1=Label(c,text-'first number')
        self.l2=Label(c,text='second number')
        self.l3=Label(c,text='result')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.b1=Button(c,text='add')
        self.b2=Button(c,text='subtract')
        self.l1.place(x=100,y=50)
        self.t1.place(x=200,y=50)
        self.l2.place(x=100,y=100)
        self.t2.place(x=200,y=100)
        self.b1=BUtton(c,text='add',command=self.add)
        self.b2=Button(c,text='subtract')
        self.b2.bind('<Button-1>',self.sub)
        self.b1.place(x=100,y=150)
        self.b2.place(x=200,y=150)
        self.l3.place(x=100,y=200)
        self.t3.place(x=200,y=200)
    def add(self):
        self.t3.delete(0,'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END,str(result))
    def sub(self,event):
        self.t3.delete(0,'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END,str(result))
a=Tk()
s=file
a.title('calculator')
a.mainloop()