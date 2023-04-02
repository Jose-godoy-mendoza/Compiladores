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
    f = fd.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: 
        return
    f.write(LeftTextbox.get(1.0, 'end-1c'))
    f.close() 
# ------------------- End of file management ------------------- #

# ------------------- Compile Function ------------------- #

def Clasify_tokens(Token):
    #print(len(Matrix))
    Operators = (["(",")","=","+", "-", "/", "*" ,"[", "]", "!=", "==", "<", ">", "<=", ">=", "&&", "||","{","}","!"])
    Reserved_Words = (["if","else","else if","for","while","switch","private","return","void","int","string","double","float"])
    
    if Token in Reserved_Words:
        Token = "PR( "+Token+" )"
        return Token
    elif Token in Operators:
        Token = "OP( "+Token+" )"
        return Token
    #with the following validation I can check if it has a . so I can store float or double variables
    elif Token.isnumeric() or (Token == '-' and Token[1:].isnumeric()) or (Token.count('.') == 1 and all(c.isdigit() for c in Token.replace('.', '', 1))):
        Token = "NUM( "+Token+" )"
        return Token
    elif Token !="":
        Token = "ID( "+Token+" )"
        return Token
    #RightTextbox.insert('end-1c', ",".join(Token))
    #RightTextbox.insert('end-1c', "\n")


def Compile():
    Tokens =""
    Columns = 0
    Matrix = [[]]
    #if I want to split a variable that is joined with a , or . or whichever symbol I want to split I just add that symbol on the next array
    Operators = (["(",")","=","+", "-", "/", "*" ,"[", "]", "!=", "==", "<", ">", "<=", ">=", "&&", "||","!"])
    OperatorConcat=(["<",">","!"])
    LeftText = LeftTextbox.get(1.0, 'end-1c')
    Text = LeftText.split("\n")
    for Lines in Text:
        position = 0
        Row = 0
        Delimiter = len(Lines)-1
        while position <= Delimiter:
            Iteration = Lines[position]
            #Validating there´s no () in the line in order to split them into tokens
            if (Iteration == " " or Iteration == "\t" or position==Delimiter) and (Iteration !="(" and Iteration !=")"):
                if Iteration !=" " and Iteration !="\t":
                    Tokens = Tokens + Iteration
                    #if there´s something stored in Tokens then concat the current value in in iteration
                if len(Tokens) >= 1: 
                    
                    Matrix[Columns].append(Clasify_tokens(Tokens)) 
                    Row = Row +1 
                    Tokens = ""
                    #Validating that there´s match with the current iteration with Operators in order to split the operators if they are joined with othe variable
            elif Iteration in Operators:
                    if(Tokens!=""):
                        Matrix[Columns].append(Clasify_tokens(Tokens)) 
                        Row = Row +1 
                        Tokens = ""
                    tempBack = Lines[position-1]
                    #tempFront = Lines[position+1]
                    #Checking if the previous token is equal to =, <, > or ! to join the current token to the previous one
                    if tempBack == Iteration or tempBack in OperatorConcat:
                        Row = Row +1 
                        temp = tempBack + Iteration
                        Matrix[Columns][Row]= Clasify_tokens(temp)
                        
                    else:
                        Matrix[Columns].append(Clasify_tokens(Iteration)) 
            else:
                Tokens = Tokens + Iteration
            
            position = position + 1
        Matrix.append([])
        RightTextbox.insert('end-1c',", ".join(Matrix[Columns]))
        Columns = Columns + 1
        RightTextbox.insert('end-1c', "\n")
    #Matrix = Clasify_tokens(Matrix)
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





