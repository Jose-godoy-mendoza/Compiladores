import tkinter as tk
from tkinter import ttk 
from tkinter import filedialog as fd
from pathlib import Path
import re
import numpy as np


VentanaPrincipal = tk.Tk()
VentanaPrincipal.title("Compiladores")

# Creating a frame to contain all the upper design 
Frame = tk.Frame(VentanaPrincipal)
Frame.pack()

# ------------------- Upper design is shown as follow ------------------- #
UpperLabelFrame = tk.LabelFrame(Frame, text="Analizer")
UpperLabelFrame.grid(row=0, column=0, padx=10, pady=5)

# Coding all left side of the frame
LeftLabel = tk.Label(UpperLabelFrame, text = "Text to be analized")
LeftLabel.grid(row=0, column=0)

LeftTextbox = tk.Text(UpperLabelFrame, width=65, height=30)
LeftTextbox.grid(row=1, column=0)

#Coding all right side of the frame 
RightLabel = tk.Label(UpperLabelFrame, text = "Tokens")
RightLabel.grid(row=0, column=1)

RightTextbox = tk.Text(UpperLabelFrame, width=65, height=30)
RightTextbox.grid(row=1, column=1)

# The following code allows us to add the same padding to all the children contained in the UpperLabelFrame
for widget in UpperLabelFrame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
# ------------------- Upper design has been finished ------------------- #

# ------------------- Lower desing is shown as follow ------------------- #
LowerLabelFrame = tk.LabelFrame(Frame, text="In this section we will see the errors on compilation time")
LowerLabelFrame.grid(row=1, column=0, padx=10, pady=5)


LowerLabel = tk.Label(LowerLabelFrame, text = "Errors")
LowerLabel.grid(row=0, column=0)

LowerTextbox = tk.Text(LowerLabelFrame, width=115, height=10)
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
    f = fd.askMatrixasfile(mode='w', defaultextension=".txt")
    if f is None: 
        return
    f.write(LeftTextbox.get(1.0, 'end-1c'))
    f.close() 
# ------------------- End of file management ------------------- #

# ------------------- Compile Function ------------------- #

def Clasify_tokens(Matrix):
    #print(len(Matrix))
    print("1--------------------------------------1")
    Operators = (["(",")","=","+", "-", "/", "*" ,"[", "]", "!=", "==", "<", ">", "<=", ">=", "&&", "||","{","}"])
    Reserved_Words = (["if","else","else if","for","while","switch","private","return","void","int","string","double","float"])
    Columns = 0
    for Lines in Matrix:
        Rows = 0
        for Row in Lines:
            #If print Lines it prints the whole line as much as values in that line
            #print(Row) 
            if Row in Operators:
                Matrix[Columns][Rows] = "OP( "+Row+" )"
                #print(Matrix[Columns][Rows])    #POSITION OF THE VALUE TO BE REPLACED
                #print("Columna: ",  Columns,  "  Fila: ",  Rows)
            elif Row in Reserved_Words:
                Matrix[Columns][Rows] = "PR( "+Row+" )"
            elif Row.isdigit():
                Matrix[Columns][Rows] = "NUM( "+Row+" )"
            elif Row !="":
                Matrix[Columns][Rows] = "ID( "+Row+" )"
            Rows = Rows + 1
        RightTextbox.insert('end-1c', ",".join(Matrix[Columns]))
        RightTextbox.insert('end-1c', "\n")
        Columns = Columns + 1
    return Matrix
    #print(Matrix)

def Compile():
    Tokens =""
    Columns = 0
    Matrix = [[]]
    Operators = (["(",")","=","+", "-", "/", "*" ,"[", "]", "!=", "==", "<", ">", "<=", ">=", "&&", "||"])
    LeftText = LeftTextbox.get(1.0, 'end-1c')
    Text = LeftText.split("\n")
    for Lines in Text:
        position = 0
        Row = 0
        Delimiter = len(Lines)-1
        while position <= Delimiter:
            Iteration = Lines[position]
            if (Iteration == " " or Iteration == "\t" or position==Delimiter) and (Iteration !="(" and Iteration !=")"):
                if Iteration !=" " and Iteration !="\t":
                    Tokens = Tokens + Iteration
                if len(Tokens) >= 1: 
                    Matrix[Columns].append(Tokens) 
                    Row = Row +1 
                    Tokens = ""
            elif Iteration in Operators:
                    if(Tokens!=""):
                        Matrix[Columns].append(Tokens)
                        Row = Row +1 
                        Tokens = ""
                    temp = Lines[position-1]
                    print("*****************")
                    if temp == Iteration:
                        Matrix[Columns][Row]= Iteration + Iteration
                        Row = Row +1 
                    else:
                        Matrix[Columns].append(Iteration)
            else:
                Tokens = Tokens + Iteration
            position = position + 1
        Matrix.append([])
        #print(Matrix)
        #RightTextbox.insert('end-1c', ",".join(Matrix[Columns]))
        #RightTextbox.insert('end-1c', "\n")
        Columns = Columns + 1
    Matrix = Clasify_tokens(Matrix)
    print(Matrix)
    




     

# ------------------- End of Compile Function ------------------- #

def Menu():
    DropdownMenu = tk.Menu(VentanaPrincipal)
    VentanaPrincipal.config(menu=DropdownMenu)
    Opciones = tk.Menu(DropdownMenu)
    Opciones.add_command(label="Abrir Fichero", command=OpenFile)
    Opciones.add_command(label="Guardar Archivo", command=SaveFile)
    Opciones.add_command(label="Compilar Fichero", command=Compile)
    Opciones.add_command(label="Tabla de tokens")
    Opciones.add_separator()
    Opciones.add_command(label="Salir")
    DropdownMenu.add_cascade(label="Opciones", menu=Opciones)

Menu()
VentanaPrincipal.mainloop()





