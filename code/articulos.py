from optparse import Option
import os
import sys
import sqlite3

opcion=0
def agregar_producto():
    os.system("cls")
    print("AGREGAR PRODUCTO: ")
    print("")

    nombre= input("DIGITE EL NOMBRE DEL PRODUCTO: ")
    precio=input("DIGITE EL PRECIO DEL PRODUCTO: ")

    con= sqlite3.connect("articulos.s3db")
    cursor= con.cursor()
    cursor.execute("insert into articulos(nombre,precio) values('"+nombre+"', '"+precio+"')")
    con.close()

    print("PRODUCTO AGREGADO")
    print("")
    print("[m] VOLVER AL MENU")
    print("[s] SALIR")

    if opcion=="m":
        menu()
    elif opcion=="s":
          sys.exit()  

def ver_producto():
    os.system("cls")
    print("VER PRODUCTO: ")
    print("")

    nombre= input("DIGITE EL NOMBRE DEL PRODUCTO: ")
    precio=input("DIGITE EL PRECIO DEL PRODUCTO: ")

    con= sqlite3.connect("articulos.s3db")
    cursor= con.cursor()
    cursor.execute("insert into articulos(nombre,precio) values('"+nombre+"', '"+precio+"')")
    con.close()

    print("PRODUCTO VISIBLE")
    print("")
    print("[m] VOLVER AL MENU")
    print("[s] SALIR")

    if opcion=="m":
        menu()
    elif opcion=="s":
          sys.exit() 

def modificar_producto() :
    os.system("cls")
    print("MODIFICAR PRODUCTO: ")
    print("")

    nombre= input("DIGITE EL NOMBRE DEL PRODUCTO: ")
    precio=input("DIGITE EL PRECIO DEL PRODUCTO: ")

    con= sqlite3.connect("articulos.s3db")
    cursor= con.cursor()
    cursor.execute("insert into articulos(nombre,precio) values('"+nombre+"', '"+precio+"')")
    con.close()

    print("PRODUCTO MODIFICADO")
    print("")
    print("[m] VOLVER AL MENU")
    print("[s] SALIR")

    if opcion=="m":
        menu()
    elif opcion=="s":
          sys.exit()  

def  eliminar_producto():
    os.system("cls")
    print("ELIMINAR PRODUCTO: ")
    print("")

    nombre= input("DIGITE EL NOMBRE DEL PRODUCTO: ")
    precio=input("DIGITE EL PRECIO DEL PRODUCTO: ")

    con= sqlite3.connect("articulos.s3db")
    cursor= con.cursor()
    cursor.execute("insert into articulos(nombre,precio) values('"+nombre+"', '"+precio+"')")
    con.close()

    print("PRODUCTO ELIMINADO")
    print("")
    print("[m] VOLVER AL MENU")
    print("[s] SALIR")

    if opcion=="m":
        menu()
    elif opcion=="s":
          sys.exit()                                

def menu():
    os.system("cls")
    print("INFORMACION DE PRODUCTO")
    print("***********************")
    print("1-AGREGAR PRODUCTO")
    print("2-VER PRODUCTO")
    print("3-MODIFICAR PRODUCTO")
    print("4-ELIMINAR PRODUCTO")
    print("SALIR")

    opcion= input("DIGITE UNA OPCION POR FAVOR: ")

    if opcion=="1":
        agregar_producto()
    
    elif opcion=="2":
        ver_producto()
    
    elif opcion=="3":
        modificar_producto()
    
    elif opcion=="4":
        eliminar_producto()  

    elif opcion=="SALIR":
        sys.exit()

    else:
        opcion= input("DIGITE UNA OPCION VALIDA: ")
        menu(opcion)


menu()







