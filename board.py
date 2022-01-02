#from tkinter import *
import random as rand
from tkinter import *
from  elfern import Elfern
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from functools import partial
import copy


class ToolTip(object):
    
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

def buttonPress():
    pass
def make_turn(position,arr):
    if k.player_turn:
        #arr.pop(position)
        k.make_turn(position)
        print(len(arr))
        arr[position].destroy()
        update(arr)
        k1 = copy.deepcopy(k)
        #a, b, c = k1.minimax(1, -1000, 1000, False)
        #c = rand.randint(0, (len(k.ai_hand)-1))
        k.make_turn(0)
        update(arr)
    if not k.player_turn:
        k1 = copy.deepcopy(k)
        a, b, c = k1.minimax(1, -1000, 1000, False)
        #c = rand.randint(0, (len(k.ai_hand)-1))
        k.make_turn(c)
        update(arr)



def update(arr):
    delete_buttons(copy.copy(arr))
    draw_player_hand(k.player_hand)
    board.configure(text=str(len(k.board)))
    button = Button(root,text=str(len(k.ai_hand)),command=buttonPress, height= 5, width=5)
    button.place(x = 45, y = 10)
    current_board.configure(text=  '')
    current_board.configure(text= str(((k.current_board[0]))) if k.current_board else '')
    root.update()
    return arr

def delete_buttons(arr):
    for i in arr:
        i.destroy()
    root.update()

def draw_player_hand(arr):


    buttons = []
    for i in range(len(arr)):
        button = Button(root,text=arr[i],command=partial(make_turn,i,buttons), height= 5, width=4)
        button.place(x = 45+i*250/(len(arr)), y = 210)
        #CreateToolTip(button, text = arr[i])
        buttons.append(button)  


    root.update()
    

# root window
k = Elfern()
root = tk.Tk()
root.geometry('330x300')
root.resizable(False, False)
root.title('Elfern game')

#sli1.pack()


arr1 = draw_player_hand(k.player_hand)

arr= []
'''
button = Button(root,text='3',command=partial(make_turn,0,arr), height= 2, width=4)
button.place(x = 45, y = 120)
arr.append(button)
button = Button(root,text='3',command=partial(make_turn,1,arr), height= 2, width=4)
button.place(x = 85, y = 120)
arr.append(button)
button = Button(root,text='3',command=partial(make_turn,2,arr), height= 2, width=4)
button.place(x = 125, y = 120)
arr.append(button)
button = Button(root,text='3',command=partial(make_turn,3,arr), height= 2, width=4)
button.place(x = 165, y = 120)
arr.append(button)
button = Button(root,text='3',command=partial(make_turn,4,arr), height= 2, width=4)
button.place(x = 205, y = 120)
arr.append(button)
button = Button(root,text='3',command=partial(make_turn,5,arr), height= 2, width=4)
button.place(x = 245, y = 120)
arr.append(button) '''

board = Button(root,text=str(len(k.board)),command=buttonPress, height= 6, width=5)
board.place(x = 110, y = 100)
arr.append(board) 


current_board = Button(root,text= (str((k.current_board[0]))) if k.current_board else '',command=buttonPress, height= 6, width=5)
current_board.place(x = 180, y = 100)
arr.append(current_board) 

button = Button(root,text=str(len(k.ai_hand)),command=buttonPress, height= 5, width=5)
button.place(x = 45, y = 10)
arr.append(button)
button = Button(root,text='',command=buttonPress, height= 5, width=5)
button.place(x = 85, y = 10)
arr.append(button)
button = Button(root,text='',command=buttonPress, height= 5, width=5)
button.place(x = 125, y = 10)
arr.append(button)
button = Button(root,text='',command=buttonPress, height= 5, width=5)
button.place(x = 165, y = 10)
arr.append(button)
button = Button(root,text='',command=buttonPress, height= 5, width=5)
button.place(x = 205, y = 10)
arr.append(button)
button = Button(root,text='',command=buttonPress, height= 5, width=5)
button.place(x = 245, y = 10)
arr.append(button)

''' button = Button(root,text='0',command=buttonPress, height= 6, width=5)
button.place(x = 0, y = 60)
arr.append(button) '''

#arr = update(arr)

root.mainloop()



