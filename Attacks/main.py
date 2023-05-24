from tkinter import *
import os
 
def dictionary():
    os.system('python dictionary.py')

def encrypt():
    os.system('python ecrypt.py')

def decrypt():
    os.system('python decrypt.py')

def brute():
    os.system('python brute.py')
    
def flood():
    os.system('python flood.py')

win = Tk()

b1=Button(win,text='Dictionary', command=dictionary,bg='orange')
b1.place(x=10,y=20)

b2=Button(win,text='Ransomware encrypt', command=encrypt,bg='orange')
b2.place(x=10,y=60)

b3=Button(win,text='Ransomware decrypt', command=decrypt,bg='orange')
b3.place(x=10,y=100)

b4=Button(win,text='Brute-force', command=brute,bg='orange')
b4.place(x=10,y=140)


win.title("SSI Tool Group 10")
win.geometry("200x180")
win.configure(bg='green')
win.mainloop()
