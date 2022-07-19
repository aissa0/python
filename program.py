from cProfile import label
from tkinter import *

root = Tk()
def myclick():
    
    
        myLabel= Label(root, text="Holle ayham!")
        
        myLabel.pack()

myButton= Button(root, text="click me", padx=50, command=myclick)
myButton.pack()

root.mainloop()
