import tkinter as tk
from tkinter import ttk




def Clasify_tokens(Token):
    Operators = (["(",")","=","+", "-", "/", "*" ,"[", "]", "!=", "==", "<", ">", "<=", ">=", "&&", "||","{","}","!"])
    Reserved_Words = (["if","else","else if","for","while","switch","private","return","void","int","string","double","float", ";"])
    
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

def filter_tokens(variable):
    return variable.replace("PR(", "").replace("ID(","").replace("NUM(","").replace(")","").replace(' ', '')


def Tabla_Simbolos(Matrix):
    #seen = set()
    root = tk.Tk()

    tree = tk.ttk.Treeview(root, columns=("Type", "Name", "Value", "Line", "Token #"))
    tree.heading("Type", text="Type")
    tree.heading("Name", text="Name")
    tree.heading("Value", text="Value")
    tree.heading("Line", text="Line")
    tree.heading("Token #", text="Column")
    i = 0
    temp = []
    Match = []

    #Reading the Rows
    for Row_index, Row in enumerate(Matrix):
        
        #Reading the Columns
        for Columns_index, Columns in enumerate(Row):
            temp.append(Columns)
            #print(Matrix[Row_index][Columns_index])
        if len(temp)==5:
                
                if "ID" in temp[1] and "NUM" or "ID" or "double" or "float" or "boolean" in temp[3] and ";" in temp[4] or "PR" in temp[0]:
                    #Validate that the type of the variable is the correct for its value
                    if ("int" in temp[0] and "NUM" in temp[3]) or ("double" in temp[0] and "NUM" in temp[3]) or ("string" in temp[0] and "ID" in temp[3]):
                        #print("CONFIRMANDO: ", temp[0]," .. ", temp[3]) 
                        Type = filter_tokens(temp[0])
                        ID = filter_tokens(temp[1])
                        Value = filter_tokens(temp[3])
                    #Here I validate if the variable is not the type it was declared
                    else:
                        ID = ""
                        Type = ""
                        Value = ""
                    #Here I validate if the variable hasn´t been declared, if so It won´t appear again in the table
                    if ID in Match:
                        print("VARIABLE YA DECLARADA")
                        del Matrix[Row_index][Columns_index]
                        #score + 1
                    #If the value doesn´t match with the type here we show the error
                    elif len(ID) == 0 and len(Type) == 0 and len(Value)==0:
                        Message = "Mala asignacion al tipo de variable en la linea:", Row_index+1

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
        elif len(temp)>1:
            if "PR" in temp[0]:
                if "ID" in temp[1] and len(temp)>2: 
                    if "OP" in temp[2] and len(temp) != 5:
                        print("ERROR ERROR: ", temp)

        
        temp = []
            

    tree.pack()
    root.mainloop()
    print("Variables encontradas: ", Match)
        

Tokens =""
rows = 0
Columns = 0
Operators = (["(",")","=","+", "-", "/", "*" ,"[", "]", "!=", "==", "<", ">", "<=", ">=", "&&", "||","!", ";"])
OperatorConcat=(["<",">","!"])
Texto = "int Linea = hola;\n string text = hi; \n int Linea = 3; \n string bool = True;"
Text = Texto.splitlines()
Matrix = [[]]
Comparison = [[]]
for Lines in Text:
        position = 0
        Row = 0
        delimitador = len(Lines)-1
        while position <= delimitador:
            Iteration = Lines[position]
            if (Iteration == " " or Iteration == "\t" or position==delimitador) and (Iteration !="(" and Iteration !=")"):
                if Iteration !=" " and Iteration !=";":
                    Tokens = Tokens + Iteration
                if len(Tokens) >= 1: 
                    Matrix[Columns].append(Clasify_tokens(Tokens))
                    Row = Row +1
                    Tokens = ""
                if Iteration == ";":
                    Matrix[Columns].append(Clasify_tokens(Iteration))
            elif Iteration in Operators:
                if(Tokens!=""):
                    Matrix[Columns].append(Clasify_tokens(Tokens))
                    
                    Row = Row +1 
                    Tokens = ""
                tempBack = Lines[position-1]
                    #tempFront = Lines[position+1]
                if tempBack == Iteration or tempBack in OperatorConcat:
                    Row = Row +1 
                    temp = tempBack + Iteration
                    Matrix[Columns][Row]= Clasify_tokens(temp)
                        
                else:
                    Matrix[Columns].append(Clasify_tokens(Iteration))
            else:
                Tokens = Tokens + Iteration
            position += 1
            #rows += rows
        Matrix.append([])
        #Comparison[Columns].append(Tabla_Simbolos(Matrix[Columns], Comparison))
        #Comparison.append([])
        #print(Matrix[Columns])
        Columns = Columns + 1
Tabla_Simbolos(Matrix)







