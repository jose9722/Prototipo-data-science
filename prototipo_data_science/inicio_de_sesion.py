import tkinter
from tkinter import*
from tkinter import messagebox
from pymysql import*

def pantalla_sesion():
    global pantalla
    pantalla = Tk()
    pantalla.geometry("300x380")
    pantalla.title("Bienvenido")
    pantalla.iconbitmap("")

    image=PhotoImage(file="")
    image=image.subsample(2,2)
    label=Label(image=image)
    label.pack()

    Label(text="Acceso al Sistema", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesion", height="3", width="30", command=pantalla_principal).pack()
    Label(text="").pack()

    pantalla.mainloop()

def pantalla_principal():
    global pantalla1
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de Sesion")
    pantalla1.iconbitmap("")

    Label(pantalla1, text="Por favor ingrese su usuario y contraseña:").pack()
    Label(pantalla1, text="").pack()

    global nombreusuario_verify
    global contrasenausuario_verify

    nombreusuario_verify=StringVar()
    contrasenausuario_verify=StringVar()

    global nombre_usuario_entry
    global contrasena_usuario_entry

    Label(pantalla1, text="Usuario").pack()
    nombre_usuario_entry = Entry(pantalla1, textvariable=nombreusuario_verify)
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña").pack()
    contrasena_usuario_entry = Entry(pantalla1, textvariable=contrasenausuario_verify)
    contrasena_usuario_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text="Iniciar Sesion").pack()


pantalla_sesion()