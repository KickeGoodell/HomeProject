import mysql.connector
import tkinter  as tk 
from tkinter import * 



my_w = tk.Tk()
my_w.geometry("400x250") 
my_connect = mysql.connector.connect(
  host="10.2.2.195",
  user="root", 
  passwd="Root4l1fe",
  database="Highscores"
)

my_conn = my_connect.cursor()
####### end of connection ####
my_conn.execute("SELECT * FROM Attemps limit 0,10")
i=0 
for Attemps in my_conn: 
    for j in range(len(Attemps)):
        e = Entry(my_w, width=10, fg='blue') 
        e.grid(row=i, column=j) 
        e.insert(END, Attemps[j])
    i=i+1
my_w.mainloop()