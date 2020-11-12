from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import Layout as L

window = Tk()

player1 = 0
player2 = 0
done1 = 1
done2 = 1
done3 = 0

L.makeWindow(window,"Prisoner's dilemma",400,400)

def Choice1(choice):
    global done1
    global player1
    if(done1 == 0):
        player1 = choice
        done1 = 1

def Choice2(choice):
    global done2
    global player2
    if(done2 == 0):
        player2 = choice
        done2 = 1

#0 => Cooperate
#1 => Dominate

play1 = []
play2 = []

iterate = 0
#LAYOUT

def PlayRound():
    global iterate
    global done1
    global done2
    global player1
    global player2
    global done3

    if(done1 == 1 & done2 == 1):
        iterate = iterate + 1

        done1 = 0
        done2 = 0

        L.makeLabel(window,0,1,"Round "+str(iterate)+":")
        L.makeLabel(window,0,2,"Player 1:")

        L.makeButton(window,0,3,"Cooperate",lambda: Choice1(0))
        L.makeButton(window,1,3,"Defect",lambda: Choice1(1))

        L.makeLabel(window,0,4,"Player 2:")

        L.makeButton(window,0,5,"Cooperate",lambda: Choice2(0))
        L.makeButton(window,1,5,"Defect",lambda: Choice2(1))

        if(iterate!=1):
            results = matchup(player1,player2)
            play1.append(results[0])
            play2.append(results[1])


        L.makeLabel(window,0,6,str(player1)+"   "+str(player2))
        L.makeLabel(window,0,7,"Player 1 History: "+str(play1))
        L.makeLabel(window,0,8,"Player 2 History: "+str(play2))

        L.makeLabel(window,0,9,"Player 1 Points: "+str(sum(play1)))
        L.makeLabel(window,0,10,"Player 2 Points: "+str(sum(play2)))

L.makeButton(window,0,0,"Start Next Round",lambda: PlayRound())

def matchup(P1,P2):
    if(P1==0):
        if(P2==0):
            return [2,2]
        if(P2==1):
            return [0,3]
    if(P1==1):
        if(P2==0):
            return [3,0]
        if(P2==1):
            return [1,1]


    
mainloop()