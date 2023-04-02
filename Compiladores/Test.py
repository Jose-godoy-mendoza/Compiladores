def Clasify_tokens(Matrix):
    #print(len(Matrix))
    print("1--------------------------------------1")
    Operators = (["(",")","=","+", "-", "/", "*" ,"[", "]", "!=", "==", "<", ">", "<=", ">=", "&&", "||","{","}","!"])
    Reserved_Words = (["if","else","else if","for","while","switch","private","return","void","int","string","double","float"])
    Columns = 0
    for Lines in Matrix:
        Rows = 0
        Replace = 0
        for Row in Lines:
            #If print Lines it prints the whole line as much as values in that line
            Replace = Matrix[Columns][Rows-1]
            if Row in Operators:
                Matrix[Columns][Rows] = "OP( "+Row+" )"
                #print(Matrix[Columns][Rows])    #POSITION OF THE VALUE TO BE REPLACED
                #print("Columna: ",  Columns,  "  Fila: ",  Rows)
            elif Row in Reserved_Words:
                Matrix[Columns][Rows] = "PR( "+Row+" )"
            #elif Row.isnumeric() or (Row[0] == '-' and Row[1:].isnumeric()) or (Row.count('.') == 1 and all(c.isdigit() for c in Row.replace('.', '', 1))):
            elif Row.isnumeric() and (Replace != "OP( + )" and Replace != "OP( - )"):
                Matrix[Columns][Rows] = "NUM( "+Row+" )"
            elif Row.isnumeric() and Replace == "OP( + )":
                del Matrix[Columns][Rows]
                Matrix[Columns][Rows-1] = "NUM ( +"+Row+" )"
                #Rows = Rows -1
            elif Row.isnumeric() and Replace == "OP( - )":
                del Matrix[Columns][Rows]
                Matrix[Columns][Rows-1] = "NUM ( -"+Row+" )"
                #Rows = Rows -1
            elif Row !="":
                Matrix[Columns][Rows] = "ID( "+Row+" )"
            Rows = Rows + 1
            #tempfront = tempfront + 1
            #Replace = Replace +1
        print(Matrix[Columns])
        Columns = Columns + 1
    return Matrix
             

Tokens =""
rows = 0
Columns = 0
Operators = (["(",")","=","+", "-", "/", "*" ,"[", "]", "!=", "==", "<", ">", "<=", ">=", "&&", "||","!"])
OperatorConcat=(["<",">","!"])
Texto = "Linea if (-1 < 0) \n Linea -2(test) \n prueba 3"
Text = Texto.splitlines()
Matrix = [[]]
for Lines in Text:
        position = 0
        Row = 0
        delimitador = len(Lines)-1
        while position <= delimitador:
            Iteration = Lines[position]
            if (Iteration == " " or Iteration == "\t" or position==delimitador) and (Iteration !="(" and Iteration !=")"):
                if Iteration !=" ":
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
                tempBack = Lines[position-1]
                    #tempFront = Lines[position+1]
                if tempBack == Iteration or tempBack in OperatorConcat:
                    Row = Row +1 
                    Matrix[Columns][Row]= tempBack + Iteration
                        
                else:
                    Matrix[Columns].append(Iteration)
            else:
                Tokens = Tokens + Iteration
            position += 1
            #rows += rows
        Matrix.append([])
        print(Matrix[Columns])
        Columns = Columns + 1
Clasify_tokens(Matrix)


