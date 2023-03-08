Tokens =""
Texto = "Li 1\nLis 2\npru"
Text = Texto.splitlines()
print (len(Text))
Guardar = []
#PosicionGuardar = 0
for Lines in Text:
        position = 0
        delimitador = len(Lines)-1
        while position <= delimitador:
            Iteration = Lines[position]
            if Iteration == " " or Iteration == "\t" or position==delimitador:
                Tokens = Tokens + Iteration
                if len(Tokens) >= 1: 
                    Guardar.append(Tokens) 
                    Tokens = ""
            else:
                Tokens = Tokens + Iteration
            position += 1
            #PosicionGuardar += PosicionGuardar
        print(Guardar)

print("----------------------")
for a in Guardar:
     print(a)