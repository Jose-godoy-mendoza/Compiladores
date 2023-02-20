import tkinter as tk
from tkinter import ttk 

VentanaPrincipal = tk.Tk()
#VentanaPrincipal.geometry("900x700")
VentanaPrincipal.title("Compiladores")

def Menu():
    DropdownMenu = tk.Menu(VentanaPrincipal)
    VentanaPrincipal.config(menu=DropdownMenu)
    Opciones = tk.Menu(DropdownMenu)
    Opciones.add_command(label="Abrir Fichero")
    Opciones.add_command(label="Compilar Fichero")
    Opciones.add_command(label="Tabla de tokens")
    Opciones.add_separator()
    Opciones.add_command(label="Salir")
    DropdownMenu.add_cascade(label="Opciones", menu=Opciones)

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

Menu()
#myentry = tk.Entry(root)
#myentry.pack()
VentanaPrincipal.mainloop()


# ------------------- Lets obtain the text from the left TextBox ------------------- #

def GetLeftText():
    LeftText = LeftTextbox.get()
    


