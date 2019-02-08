from tkinter import *
import mysql.connector



root= Tk()

lbl0=Label(root,text="PLEASE ENTER YOUR CREDENTIALS")
lbl1=Label(root, text="name")
lbl2=Label(root, text="password")

nmVal=Entry(root)
passVal=Entry(root)
userQry=Entry(root)
def login1():
    dbNm=nmVal.get()
    dbPass=passVal.get()
    mydb = mysql.connector.connect(host="localhost",user=dbNm, passwd=dbPass, database="db1")
    mycursor=mydb.cursor()
    mycursor.execute(userQry.get())
    result=mycursor.fetchall()

    for i in result:
        print(i)



b=Button(root,text='Execute', command=login1)


lbl0.grid(columnspan=2,sticky='')
lbl1.grid(row='1',column=0,sticky='E')
lbl2.grid(row='2',column=0,sticky='E')

nmVal.grid(row='1',column=1,sticky='W')
passVal.grid(row='2',column=1,sticky='W')
userQry.grid(row='3',columnspan='2')
b.grid(columnspan=2,sticky='')



root.mainloop()
