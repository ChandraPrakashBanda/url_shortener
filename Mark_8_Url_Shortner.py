import tkinter 
from tkinter import *
import pyshorteners
root=Tk()
def get_url():
    label1=Label(root,text=pyshorteners.Shortener().tinyurl.short(url.get()))
    label1.pack()
     

url=Entry(root)
url.pack()
url_button=Button(root,text="Get_url",command=get_url)
url_button.pack()
root.mainloop()
