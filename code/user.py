from tkinter import*
from sqlite3 import*
from tkinter.ttk import*

root=Tk()
titulo=("LOGUEO DE USUARIO")
root.geometry("500x400")

def getvals():
    print("ACEPTADO")

Label(root, text="BIENVENIDOS", font=("arial black", 20)).grid(row=0, column=1)

#CUADROS DE TEXTO
nombre=Label(root, text="NOMBRE")
apellido=Label(root, text="APELLIDO")
correo=Label(root,text="CORREO")
telefono=Label(root,text="TELEFONO")

#POSICIONAMIENTO
nombre.grid(row=1, column=1)
apellido.grid(row=2, column=1)
correo.grid(row=3, column=1)
telefono.grid(row=4, column=1)

nombrevalue=StringVar
apellidovalue=StringVar
correovalue=StringVar
telefonovalue=StringVar

checkvalue=IntVar

nombre_entry=Entry(root, textvariable=nombrevalue)
apellido_entry=Entry(root, textvariable=apellidovalue)
correo_entry=Entry(root, textvariable=correovalue)
telefono_entry=Entry(root, textvariable=telefonovalue)

nombre_entry.grid(row=1, column=3)
apellido_entry.grid(row=2, column=3)
correo_entry.grid(row=3, column=3)
telefono_entry.grid(row=4, column=3)


chek_boton=Checkbutton(text="RECUERDAME", variable=checkvalue)
chek_boton.grid(row=6, column=3)


boton=Button(text="INGRESAR!", command=getvals).grid(row=7, column=3)

root.mainloop()