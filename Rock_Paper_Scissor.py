from cProfile import label
from tkinter import *
import random
from tkinter import font
from unittest import result


root = Tk()                         # create window 

root.geometry('400x400')
root.resizable(0, 0)
root.title('Rock, Paper, Scissors')
root.config(bg='seashell3')         # background color


Label(root, text='Rock, Paper, Scissors', font='Arial 20 bold', bg='seashell2').pack()


user_take=StringVar()


Label(root, text= 'Choose your call from: Rock, Paper, Scissors', font= 'arial 15 bold',  bg='seashell2') .place(x=20, y=70)
Entry(root, font='arial 15', textvariable= user_take, bg='antiquewhite2') .place(x=90, y=130)



# Computer's choise

comp_pick = random.randint(1, 3)
if comp_pick == 1:
    comp_pick= 'rock'
elif comp_pick == 2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'


    
# game function

Result = StringVar()

def play():
    user_pick =user_take.get()
    if user_pick == comp_pick:
        Result.set('TIE!!!, Try again')
    elif user_pick == 'rock' and comp_pick=='paper':
        Result.set('You Lose!!! Computer choose Paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you win!!! Computer choose scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you loose!!! Computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win!!! Computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you loose!!! Computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('you win!!! Computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')



#Function reset

def Reset():
    Result.set("")
    user_take.set("")



#Exit Function

def Exit():
    root.destroy()



#Define Buttons

Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='antiquewhite2',width = 50,).place(x=25, y = 250)
Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play).place(x=150,y=190)
Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = Reset).place(x=70,y=310)
Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=230,y=310)

root.mainloop()