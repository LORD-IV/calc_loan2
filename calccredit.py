from tkinter import *

     

def calccounter():
    winWindow = Tk()
    winWindow.geometry('300x100')
    winWindow.title('Every moths your will pay(annuitet)')
    SummaCre = int(SummaText.get('1.0',END))
    SrokLe = int(SrokText.get('1.0',END))*12
    ProcGo = int(ProcText.get('1.0',END))/12/100
    
    K1 = ((1+ProcGo)**SrokLe)-1
    
    K2 = ProcGo*((1+ProcGo)**SrokLe)
    K3=K2/K1
    A = round(K3*SummaCre,2)
    
    winLabe = Label(winWindow, text = A)
    winLabe.pack()
    winWindow.mainloop()

settings = Tk()
settings.title('Enter parameters of loan')
settings.geometry('250x150')

SummaText = Text(settings,width = 10, height = 1)
SummaText.insert('1.0', '1000000')
SummaText.place(x=75,y=5)

SummaLabe = Label(settings,height = 1, text='Sum of loan')
SummaLabe.place(x=5,y=5)

SrokText = Text(settings,width = 10, height = 1)
SrokText.insert('1.0', '3')
SrokText.place(x=75,y=30)

SrokLabe = Label(settings,height = 1, text='Year of loan')
SrokLabe.place(x=5,y=30)

ProcText = Text(settings,width = 10, height = 1)
ProcText.insert('1.0', '10')
ProcText.place(x=75,y=55)

ProcLabe = Label(settings,height = 1, text='% year')
ProcLabe.place(x=5,y=55)

mineBut = Button(settings, text = 'Calc',
                 command = calccounter)
mineBut.place(x=70,y=90)


settings.mainloop()
