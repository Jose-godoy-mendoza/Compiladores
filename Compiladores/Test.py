def clasify_tokens(Matrix):
    #print(len(Matrix))
    Operators = (["(",")"])
    print("1--------------------------------------1")
    Columns = 0
    for Lines in Matrix:
        Rows = 0
        for Row in Lines:
            #If print Lines it prints the whole line as much as values in that line
            #print(Row) 
            if Row in Operators:
                Matrix[Columns][Rows] = "OP"+Row
                print(Matrix[Columns][Rows])    #POSITION OF THE VALUE TO REPLACE
                print("Columna: ",  Columns,  "  Fila: ",  Rows)
            if Row == "if" or Row =="else" or Row == "while" or Row == "for" or Row =="switch":
                 Matrix[Columns][Rows] = "OP"+Row
            Rows = Rows + 1
        Columns = Columns + 1
    print(Matrix)
             

Tokens =""
rows = 0
columns = 0
Texto = "col 1\n Linea 2(test) \n prueba 3"
Text = Texto.splitlines()
Guardar = [[]]
for Lines in Text:
        position = 0
        #rows = 0
        #columns = 0
        delimitador = len(Lines)-1
        while position <= delimitador:
            Iteration = Lines[position]
            if (Iteration == " " or Iteration == "\t" or position==delimitador) and (Iteration !="(" and Iteration !=")"):
                if Iteration !=" ":
                    Tokens = Tokens + Iteration
                if len(Tokens) >= 1: 
                    Guardar[columns].append(Tokens) 
                    Tokens = ""
            elif Iteration == "(" or Iteration == ")":
                    Guardar[columns].append(Tokens)
                    Tokens = ""
                    Guardar[columns].append(Iteration)
            else:
                Tokens = Tokens + Iteration
            position += 1
            #rows += rows
        Guardar.append([])
        columns = columns + 1
            #PosicionGuardar += PosicionGuardar
clasify_tokens(Guardar)


