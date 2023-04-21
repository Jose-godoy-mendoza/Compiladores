import tkinter as tk
from tkinter import ttk

root = tk.Tk()

tree = tk.ttk.Treeview(root, columns=("Type", "Name", "Value"))
tree.heading("Type", text="Type")
tree.heading("Name", text="Name")
tree.heading("Value", text="Value")


tree.insert("", "end", text=1, values=("int", "i","0"))
tree.insert("", "end", text=2, values=("String", "text","test"))
tree.insert("", "end", text=3, values=("Boolean", "boolean","True"))

tree.pack()

root.mainloop()
