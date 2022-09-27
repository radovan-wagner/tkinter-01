import tkinter as tk

from tkinter import ttk

def greet():
    print( "Hello World !" )

root = tk.Tk()              # Main Window


ttk.Label( root, text="Nazdar Radenko !", padding=(30,10) ).pack()

greet_button = ttk.Button( root, text="Pozdravujem !", command=greet, padding=(30,10) )
greet_button.pack()

root.mainloop()

