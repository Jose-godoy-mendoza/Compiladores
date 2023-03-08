import tkinter as tk
from tkinter import ttk 
from tkinter import filedialog as fd
from pathlib import Path
import re

VentanaPrincipal = tk.Tk()
VentanaPrincipal.title("Compiladores")

# Creating a frame to contain all the upper design 
Frame = tk.Frame(VentanaPrincipal)
Frame.pack()

# ------------------- Upper design is shown as follow ------------------- #
UpperLabelFrame = tk.LabelFrame(Frame, text="Label para frame superior")
UpperLabelFrame.grid(row=0, column=0, padx=10, pady=5)

# Coding all left side of the frame
LeftLabel = tk.Label(UpperLabelFrame, text = "Aun no definido")
LeftLabel.grid(row=0, column=0)

LeftTextbox = tk.Text(UpperLabelFrame, width=40, height=30)
LeftTextbox.grid(row=1, column=0)

#Coding all right side of the frame 
RightLabel = tk.Label(UpperLabelFrame, text = "tampoco está definido")
RightLabel.grid(row=0, column=1)

RightTextbox = tk.Text(UpperLabelFrame, width=65, height=30)
RightTextbox.grid(row=1, column=1)

# The following code allows us to add the same padding to all the children contained in the UpperLabelFrame
for widget in UpperLabelFrame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
# ------------------- Upper design has been finished ------------------- #

# ------------------- Lower desing is shown as follow ------------------- #
LowerLabelFrame = tk.LabelFrame(Frame, text="Label para frame inferior")
LowerLabelFrame.grid(row=1, column=0, padx=10, pady=5)


LowerLabel = tk.Label(LowerLabelFrame, text = "Titulo por defecto")
LowerLabel.grid(row=0, column=0)

LowerTextbox = tk.Text(LowerLabelFrame, width=105, height=10)
LowerTextbox.grid(row=1, column=0)

# The following code allows us to add the same padding to all the children contained in the LowerLabelFrame
for widget in LowerLabelFrame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
# ------------------- Lower desing has been finished ------------------- #


# ------------------- Creating methods to manage files ------------------- #
def OpenFile():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # show the open file dialog
    File = fd.askopenfile(filetypes=filetypes)
    # read the text file and show its content on the Text
    LeftTextbox.insert('1.0', File.read())
    return File.name

def SaveFile():
    f = fd.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: 
        return
    f.write(LeftTextbox.get(1.0, 'end-1c'))
    f.close() 
# ------------------- End of file management ------------------- #

# ------------------- Compile Function ------------------- #
def Compile():
    Tokens =""
    LeftText = LeftTextbox.get(1.0, 'end-1c')
    Text = LeftText.split("\n")
    #RightTextbox.delete()
    RightTextbox.insert("end-1c", len(Text))
    Guardar = []
    for Lines in Text:
        position = 0
        Delimiter = len(Lines)-1
        while position <= Delimiter:
            Iteration = Lines[position]
            if Iteration == " " or Iteration == "\t" or position==Delimiter:
                Tokens = Tokens + Iteration
                if len(Tokens) >= 1: 
                    Guardar.append(Tokens)  
                    Tokens = ""
            else:
                Tokens = Tokens + Iteration
            position = position + 1
        print(Guardar)
    print("----------------------")
    for a in Guardar:
        print(a)        

# ------------------- End of Compile Function ------------------- #

def Menu():
    DropdownMenu = tk.Menu(VentanaPrincipal)
    VentanaPrincipal.config(menu=DropdownMenu)
    Opciones = tk.Menu(DropdownMenu)
    Opciones.add_command(label="Abrir Fichero", command=OpenFile)
    Opciones.add_command(label="Guardar", command=SaveFile)
    Opciones.add_command(label="Compilar Fichero", command=Compile)
    Opciones.add_command(label="Tabla de tokens")
    Opciones.add_separator()
    Opciones.add_command(label="Salir")
    DropdownMenu.add_cascade(label="Opciones", menu=Opciones)

Menu()
VentanaPrincipal.mainloop()


# ------------------- Lets obtain the text from the left TextBox ------------------- #
def GetLeftText():
    LeftText = LeftTextbox.get(1.0, 'end-1c')
    Text = LeftText.split("\n")
    #RightLabel.config(text=LeftText)
    RightTextbox.insert("end-1c", len(Text))
    
# ------------------- Lets set the text from the rifht TextBox ------------------- #
def SetRightText():
    RightTextbox.delete(1.0, "end-1c")
    RightTextbox.insert("end-1c","wenas")



