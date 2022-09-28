import tkinter as tk

from tkinter import ttk

def greet():
    print( f"Hello {user_name.get() or 'World' } !" )

def okbutton():
    print( "Ok !" )


root = tk.Tk()
user_name = tk.StringVar()# Main Window

ttk.Label( root, text="Nazdar Radenko !", padding=(30,10) ).pack()

name_label = ttk.Label( root, text="Meno: " )
name_label.pack(side="left", padx=(0,10))
name_entry = ttk.Entry( root, width=15, textvariable=user_name )
name_entry.pack( side="left" )
name_entry.focus()

greet_button = ttk.Button( root, text="Pozdravujem !", command=greet )
greet_button.pack( side = "left" )

ok_button = ttk.Button( root, text="Ok", command=okbutton )
ok_button.pack( side = "left" )

quit_button = ttk.Button( root, text="Quit", command=root.destroy )
quit_button.pack( side = "left" )

root.mainloop()

