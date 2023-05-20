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

# ------------------- ERROR HANDLING ----------------- #
def filter_tokens(variable):
    return variable.replace("PR(", "").replace("ID(","").replace("NUM(","").replace("OP(","").replace(")","").replace(' ', '')

def ErrorMSG_NotDeclared(LineCount):
    Message = "VARIABLE AUN NO DECLARADA, ERROR EN LA LINEA: ", LineCount
    LowerTextbox.insert('end-1c', Message)
    LowerTextbox.insert('end-1c', "\n")



def ErrorHandling(Line, Match, LineCount):
    print("--------------------------------ERROR HANDLING--------------------------------")
    Operators = ["OP( = )", "OP( != )", "OP( == )", "OP( < )", "OP( <= )", "OP( > )", "OP( >= )", "OP( / )", "OP( \ )","OP( + )", "OP( - )", "OP( * )"]
    IgnoreSymbols = ["{", "}","(",")"]
    InvalidSymbols = ["$", "@"]
    Count = 0
    Position = len(Line)-1
    
    if "PR( if )" in Line:
        #if(x!=0)
        #position = len(Line)-1
        print("1: ", Line[1], "2: ", Line[2], " 3: ", Line[3], " ", Line[Position])
        #if Line[Position] == ";":
            #Count = 1
        if "OP( ( )" in Line[1] and "ID" in Line[2] and Line[3] in Operators and ("OP( ) )" in Line[Position] or "OP( ) )" in Line[Position-1]):
            Line[2] = filter_tokens(Line[2])
            print(Line[2])
            if Line[2] in Match:
                print("Asignacion correcta")
            else:
                ErrorMSG_NotDeclared(LineCount)
        else:
            Message = "IF MAL DECLARADO EN LA LINEA: ", LineCount
            LowerTextbox.insert('end-1c', Message)
            LowerTextbox.insert('end-1c', "\n")
    elif "PR( for )" in Line:
        if "OP( ( )" in Line[1] and (("int" in Line[2] and "ID" in Line[3] and "OP" in Line[4] and "NUM" in Line[5] and ";" in Line[6] and "ID" in Line[7] and "OP" in Line[8] and "NUM" in Line[9] and ";" in Line[10] and "ID" in Line[11] and "OP" in Line[12]) or "ID" in Line[2] in Line[3] and ";" in Line[4] and "ID" in Line[5] and "OP" in Line[6]):
            if "ID" in Line[3]:
                Line[3] = filter_tokens(Line[3])
            else:
                Line[2] = filter_tokens(Line[2])
            if Line[2] in Match or Line[3] in Match:
                print("Asignacion Correcta")
            breakpoint
    elif "ID" in Line[0] and "=" in Line[1] and (("ID" or "NUM "in Line[2] and "OP" in Line[3] and "ID" or "NUM" in Line[4])):
        Line[0] = filter_tokens(Line[0])
        if Line[0] in Match:
            breakpoint
        ##############################
    elif Line[Position] not in IgnoreSymbols:
        breakpoint
    else:
        Message = "Falta el ; al final de la linea", LineCount
        LowerTextbox.insert('end-1c', Message)
        LowerTextbox.insert('end-1c', "\n")


# ------------------- Symbols Table ------------------- #

def SymbolsTable(Matrix):
    floating_window = tk.Toplevel(VentanaPrincipal)
    floating_window.geometry("800x400+100+200")  # Width x Height + X + Y
    floating_window.wm_attributes("-topmost", True)

    tree = tk.ttk.Treeview(floating_window, columns=("Type", "Name", "Value", "Line", "Token #"))
    tree.heading("Type", text="Type")
    tree.heading("Name", text="Name")
    tree.heading("Value", text="Value")
    tree.heading("Line", text="Line")
    tree.heading("Token #", text="Column")
    i = 0 
    linea = 0
    temp = []
    Match = []
    del Matrix[-1]
    #Reading the Rows
    for Row_index, Row in enumerate(Matrix):
        linea = linea +1
        #Reading the Columns
        
        for Columns_index, Columns in enumerate(Row):
            temp.append(Columns)
            #print(Matrix[Row_index][Columns_index])
        #print("********************************")
        #print(temp)

        
        if len(temp)==5:
                
                if "ID" in temp[1] and "NUM" or "ID" or "double" or "float" or "boolean" in temp[3] and ";" in temp[4] or "PR" in temp[0]:
                    #Validate that the type of the variable is the correct for its value
                    if ("int" in temp[0] and "NUM" in temp[3]) or ("double" in temp[0] and "NUM" in temp[3]) or ("string" in temp[0] and "ID" in temp[3]):
                        #print("CONFIRMANDO: ", temp[0]," .. ", temp[3]) 
                        Type = filter_tokens(temp[0])
                        ID = filter_tokens(temp[1])
                        Value = filter_tokens(temp[3])
                    #Here I validate if the variable is not the type it was declared
                    elif "PR( if )" in temp[0]:

                        ID = "ERROR"
                        Type = ""
                        Value = ""
                    #elif "" VALIDATE IF THERE´S A SYMBOL BEDORE THE ID TO SHOW THE ERROR
                    else:
                        ID = ""
                        Type = ""
                        Value = ""
                    #Here I validate if the variable hasn´t been declared, if so It won´t appear again in the table
                    if ID in Match:
                        Message = "Variable ya declarada anteriormente, error linea: ", Row_index+1
                        LowerTextbox.insert('end-1c', Message)
                        LowerTextbox.insert('end-1c', "\n")
                        print("VARIABLE YA DECLARADA")
                        del Matrix[Row_index][Columns_index]
                        #score + 1
                    #If the value doesn´t match with the type here we show the error
                    elif len(ID) == 0 and len(Type) == 0 and len(Value)==0:
                        Message = "Mala asignacion al tipo de variable en la linea:", Row_index+1
                        LowerTextbox.insert('end-1c', Message)
                        LowerTextbox.insert('end-1c', "\n")
                        print("Mala declaracion de variable en la linea: ", Row_index+1)
                    #If the variable hasn´t been declared and its value matches its type we are going to show it
                    else: 
                        tree.insert("", "end", text=i, values=(Type, ID, Value, Row_index+1, Columns_index+1))
                        Match.append(ID)
                        #temp = []
                        i = i+1
                    #temp = []
                else:
                    print("ERROR DE DECLARACION EN: ",Row_index+1, Columns_index+1)
                    if "PR" in  temp[0] and "ID" in temp[1] and "NUM" or "ID" in temp[2]:
                        print("ERROR DE ASIGNACION, FALTA EL SIMBOLO =")
                    if ";" != temp[4]:
                        print("FALTA EL ; al final")
                    #temp = []
        elif "PR" in temp[0] and len(temp)>1:
            if "ID" in temp[1] and len(temp)>2: 
                if "OP" in temp[2] and len(temp) != 5:
                    Message = "Error de Declaracion en la linea: ", Row_index+1
                    LowerTextbox.insert('end-1c', Message)
                    LowerTextbox.insert('end-1c', "\n")
        ErrorHandling(temp, Match,  Row_index+1)
        temp = []


    tree.pack()
    print("Variables encontradas: ", Match)

    
# ------------------- End Of Symbols Table ------------------- #

# ------------------- Compile Function ------------------- #

def Clasify_tokens(Token):
    #print(len(Matrix))
    Operators = (["(",")","=","+", "-", "/", "*" ,"[", "]", "!=", "==", "<", ">", "<=", ">=", "&&", "||","{","}","!"])
    Reserved_Words = (["if","else","else if","for","while","switch","private","return","void","int","string","double","float", "boolean" ,";"])
    
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
    RightTextbox.delete("1.0", tk.END)
    LowerTextbox.delete("1.0", tk.END)
    Tokens =""
    Columns = 0
    Matrix = [[]]
    #if I want to split a variable that is joined with a , or . or whichever symbol I want to split I just add that symbol on the next array
    Operators = (["(", ")", "=", "+", "-", "/", "*" ,"[", "]", "!=", "==", "<", ">", "<=", ">=", "&&", "||", "!", ";"])
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
                if Iteration !=" " and Iteration !="\t" and Iteration !=";":
                    Tokens = Tokens + Iteration
                    #if there´s something stored in Tokens then concat the current value in in iteration
                if len(Tokens) >= 1: 
                    
                    Matrix[Columns].append(Clasify_tokens(Tokens)) 
                    Row = Row +1 
                    Tokens = ""
                if Iteration == ";":
                    Matrix[Columns].append(Clasify_tokens(Iteration))
                    #Validating that there´s match with the current iteration with Operators in order to split the operators if they are joined with othe variable
            elif Iteration in Operators:
                    if(Tokens!=""):
                        Matrix[Columns].append(Clasify_tokens(Tokens)) 
                        Row = Row +1 
                        Tokens = ""
                    tempBack = Lines[position-1]
                    #Checking if the previous token stored in the Matrix is equal to =, <, > or ! to join the current token to the previous one
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
    
    SymbolsTable(Matrix)





# ------------------- End of Compile Function ------------------- #

def Menu():
    DropdownMenu = tk.Menu(VentanaPrincipal)
    VentanaPrincipal.config(menu=DropdownMenu)
    Opciones = tk.Menu(DropdownMenu)
    Opciones.add_command(label="Abrir Fichero", command=OpenFile)
    Opciones.add_command(label="Guardar Archivo", command=SaveFile)
    Opciones.add_command(label="Compilar Fichero", command=Compile)
    Opciones.add_command(label="Tabla de Simbolos", command=SymbolsTable)
    Opciones.add_separator()
    Opciones.add_command(label="Salir")
    DropdownMenu.add_cascade(label="Opciones", menu=Opciones)

Menu()
VentanaPrincipal.mainloop()





