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
    Filter = [[]]
    Match = []

    #Reading the Rows
    for Row_index, Row in enumerate(Matrix):

        #Reading the Columns
        for Columns_index, Columns in enumerate(Row):
            
            #print(Matrix[Row_index][Columns_index])
            if "ID" in Columns:
                #print("Coincidencia: ", Columns, " En la Linea: ", Row_index, " Token #",Columns_index)
                if "PR" in Matrix[Row_index][Columns_index-1]:
                    #Type = Matrix[Row_index][Columns_index-1].replace("PR(", "").replace(")","").replace(' ', '')
                    Type = filter_tokens(Matrix[Row_index][Columns_index-1])
                    #ID = Columns.replace("ID(", "").replace(")","").replace(' ','')
                    ID = filter_tokens(Columns)
                    #Value = Matrix[Row_index][Columns_index+2].replace("NUM(","").replace(")","").replace(' ','')
                    Value = filter_tokens(Matrix[Row_index][Columns_index+2])
                    if ID in Match:
                        #print("saber")
                        del Matrix[Row_index][Columns_index]
                    else: 
                        tree.insert("", "end", text=i, values=(Type, ID, Value, Row_index+1, Columns_index+1))
                        #Filter[i].append(Type)
                        #Filter[i].append(ID)
                        #Filter[i].append(Value)
                        #Filter.append([])
                        Match.append(ID)
                        i = i+1
    tree.pack()

    root.mainloop()
    print(Filter)
    #I could use a function to search if the token has been used before and stored in Filter Matrix, in order to substract the positions where the token is being used
    print("Variables encontradas: ", Match)
        

Tokens =""
rows = 0
Columns = 0
Operators = (["(",")","=","+", "-", "/", "*" ,"[", "]", "!=", "==", "<", ">", "<=", ">=", "&&", "||","!", ";"])
OperatorConcat=(["<",">","!"])
Texto = "int Linea = 0;\n string text = hi; \n int Linea = 3; \n string bool = True;"
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
print("------------------------------------")
print(Matrix)
#Tabla_Simbolos(Matrix)







