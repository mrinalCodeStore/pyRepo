from tkinter import *
from tkinter import messagebox
import random

choiceArr=['ROCK','SCISSOR','PAPER']
rock=choiceArr[0]
scissor=choiceArr[1]
paper=choiceArr[2]
choice=''

compScr =0
playerScr =0


#----------------------------------------------------------------------------------
#---------------------------------FUNCTIONALITY---------------------------------
#----------------------------------------------------------------------------------

def exitFunc():
    ask=messagebox.askyesno('EXIT','Do you want to QUIT')
    if ask==True:
        root.destroy()
        root.quit

def rock():
    global compScr
    global playerScr
    #choice=rock
    choice=random.choice(choiceArr)
    yourtext.delete(1.0,END)
    computertext.delete(1.0,END)
    maintext.delete(1.0,END)
    
    if choice=='ROCK':
        maintext.insert(INSERT,'\n\n\n\n')
       
        maintext.insert(INSERT,'TIE')
        computertext.insert(INSERT,choice)
        yourtext.insert(INSERT,'ROCK')
        
    elif choice=='PAPER':
       
        compScr = compScr + 1
        
        maintext.insert(INSERT,'\n\n\n\n')
           
        maintext.insert(INSERT,"Computer won")
        comptext.delete(1.0,END)
        comptext.insert(INSERT,compScr)
        computertext.insert(INSERT,choice)
        yourtext.insert(INSERT,'ROCK')
        
    else:
        playerScr = playerScr +1
        maintext.insert(INSERT,'\n\n\n\n')
           
        maintext.insert(INSERT,"You won")
        youtext.delete(1.0, END)
        youtext.insert(INSERT,playerScr)
        computertext.insert(INSERT,choice)
        yourtext.insert(INSERT,'ROCK')


def paper():
   
    global compScr
    global playerScr
    #choice=paper
    choice=random.choice(choiceArr)
    yourtext.delete(1.0,END)
    computertext.delete(1.0,END)
    maintext.delete(1.0,END)
            
    if choice=='ROCK':                                                          #The whole condition of selecting paper by user
        playerScr =playerScr + 1
        maintext.insert(INSERT,'\n\n\n\n')
      
        maintext.insert(INSERT,'You won')
        youtext.delete(1.0, END)
        youtext.insert(INSERT,playerScr)
        computertext.insert(INSERT,choice)
        yourtext.insert(INSERT,'PAPER')
    else:
        if choice=='PAPER':
            maintext.insert(INSERT,'\n\n\n\n')
          
            maintext.insert(INSERT,"TIE")
            computertext.insert(INSERT,choice)
            yourtext.insert(INSERT,'PAPER')
        else:
            compScr = compScr + 1
            maintext.insert(INSERT,'\n\n\n\n')
         
            maintext.insert(INSERT,"Computer won")
            comptext.delete(1.0,END)
            comptext.insert(INSERT,compScr)
            computertext.insert(INSERT,choice)
            yourtext.insert(INSERT,'PAPER')


def scissor():
    global compScr
    global playerScr
    #choice=scissor
    choice=random.choice(choiceArr)
    yourtext.delete(1.0,END)
    computertext.delete(1.0,END)
    maintext.delete(1.0,END)   
    maintext.insert(INSERT,'\n')    
    if choice=='ROCK':                                                        #The whole condition for selecting scissor by user
        compScr =compScr + 1 
        maintext.insert(INSERT,'\n\n\n\n')
        comptext.delete(1.0,END)
        maintext.insert(INSERT,"Computer won")
        comptext.delete(1.0,END)
        comptext.insert(INSERT,compScr)
        computertext.insert(INSERT,choice)
        yourtext.insert(INSERT,'SCISSOR')
    else:
        if choice=='PAPER':
            playerScr=playerScr+1
            maintext.insert(INSERT,'\n\n\n\n')
          
            maintext.insert(INSERT,"You won")
            youtext.delete(1.0, END)
            youtext.insert(INSERT,playerScr)
            computertext.insert(INSERT,choice)
            yourtext.insert(INSERT,'SCISSOR')
        else:
            maintext.insert(INSERT,'\n\n\n\n')
           
            maintext.insert(INSERT,"TIE")
            computertext.insert(INSERT,choice)
            yourtext.insert(INSERT,'SCISSOR')


#----------------------------------------------------------------------------------
#---------------------------------INTERFACE DESIGN---------------------------------
#----------------------------------------------------------------------------------

root=Tk()

#creating the canvas
canvas=Canvas(root, width=500,height=500,bg='black')
canvas.pack()

#creating the labels for game
game=Label(root, text='ROCK PAPER SCISSOR GAME',font=2, fg='skyblue', bg='black')
you=Label(root, text='You:', bg='black',font=2, fg='light green')
computer=Label(root, text='Comp.:', bg='black',fg='red',font=2)
select=Label(root, text='Select one',bg='black',fg='yellow',font=2)

#Creating the buttons
rock=Button(root, text='Rock', bg='orange',fg='black',width=14,command=rock)
paper=Button(root, text='Paper',bg='orange',fg='black',width=14,command=paper)
scisor=Button(root, text='Scissor',bg='orange',fg='black',width=14,command=scissor)
exit1=Button(root, text='EXIT',bg='orange',fg='black',width=14,command=exitFunc)

#creating text
maintext=Text(root, width=20,height=12.4,wrap=WORD,pady=10,padx=10)
youtext=Text(root, width=14,height=1)
comptext=Text(root, width=14,height=1)
yourtext=Text(root, width=15,height=1)
computertext=Text(root, width=15,height=1)
youtxt=canvas.create_text(100,350,text='You  choose'+":  ",fill='light green',font=1)
comptxt=canvas.create_text(100,400,text='Comp.  choose'+":  ",fill='red',font=1)

#placing the gui
game.place(x=110,y=30)
you.place(x=30,y=80)
computer.place(x=30,y=280)
rock.place(x=90,y=130)
paper.place(x=90,y=180)
scisor.place(x=90,y=230)
exit1.place(x=165,y=440)

maintext.place(x=240,y=80)
youtext.place(x=90,y=83)
comptext.place(x=90,y=280)
yourtext.place(x=240,y=340)
computertext.place(x=240,y=390)


root.title("ROCK PAPER SCISSOR GAME")
root.geometry('450x480')
root.mainloop()                                                #End of the programme
