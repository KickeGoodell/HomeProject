from tkinter import *



def mainMessage():
    root = Tk()
    message = "Do you want to save your highscore or try again?"
    Label(root,text=message).pack()
    Button(root, text='Yes', command=messageWindow).pack()
    Button(root, text='No', command=root.destroy).pack()
    Button(root, text='Play Again', command=root.destroy).pack()
    root.mainloop()

def messageWindow():
    win = Toplevel()
    win.title('Save Highscore')
    message = "Put in your initials (three letters)"
    Label(win, text=message).pack()
    Button(win, text='Save', command=win.destroy).pack()

mainMessage()