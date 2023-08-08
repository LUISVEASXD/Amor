from  tkinter import font, messagebox
from  tkinter import *
from PIL import ImageTk, Image


def enviar_declaracion1():
    respuesta = "Sí" 
    messagebox.showinfo(message="Claro pues si soy todo lo que necesitas",title="(●'◡'●)")
    messagebox.showinfo("Respuesta", f"Tu respuesta es: {respuesta}")
    messagebox.showinfo(message="Ya podemos ser novios",title="(づ￣ 3￣)づ")
    imagen = "imagenes/abrazo.png"
    set_images1(imagen)
    
    
def enviar_declaracion2():
    respuesta = "No?" 
    messagebox.showinfo(message="Creo que precionaste mal", title=("(* ￣︿￣)"))
    messagebox.showinfo("Respuesta", f"Tu respuesta es: {respuesta}")
    messagebox.showinfo(message="Intentemos otra vez", title=("( ˘︹˘ )"))
    imagen = "imagenes/enojado.png"
 
    set_images2(imagen)   


def set_images1(imagenen_Si):
    global imagen
    imagen = Image.open(imagenen_Si)
    imagen = imagen.resize((200, 200))
    imagen = ImageTk.PhotoImage(imagen)
    imagen_label = Label(image=imagen)
    imagen_label.config(image=imagen)
    imagen_label.image = imagen
    imagen_label.place(x=90, y=350)
    
    
def set_images2(imagenen_No):
    global imagen
    imagen = Image.open(imagenen_No)
    imagen = imagen.resize((200, 200))
    imagen = ImageTk.PhotoImage(imagen)
    imagen_label = Label(image=imagen)
    imagen_label.config(image=imagen)
    imagen_label.image = imagen
    imagen_label.place(x=90, y=350)   

    

    
root = Tk()
#root.geometry("500x400")
root.iconbitmap("imagenes/heart.ico")
root.configure(background='#FE5ECB')
root.title('Amor')


titulo_0 = Label(root, text="¿Quieres ser mi novia?",bg="#000000",fg="white", width=0, font=('Times New Roman', 30))
titulo_0.pack(pady=20)

respuesta_var = BooleanVar()
respuesta_var.set(False)
respuesta_label = Label(root, text="Selecciona tu respuesta:", font=("Helvetica", 14,),background='#FE5ECB')
respuesta_label.pack(pady=30)




button_Si = Button(root, text="SI", width=4, height=1, font=('Times New Roman', 25), bg="#ff4141", fg="white", border=5, command = enviar_declaracion1, )#Variable=respuesta_var, value=True,) 
button_Si.place(x=40, y=220)


button_No = Button(root, text="NO", width=4, height=1, font=('Times New Roman', 25), bg="#ff4141", fg="white",border=5, command = enviar_declaracion2, )#Variable=respuesta_var, value=False) 
button_No.place(x=250, y=220)

titulo_2 = Label(root, text="MDAG <3",font=('Times New Roman', 15),bg="#FE5ECB")
titulo_2.pack(pady=200)

#def imagen0(n):
    #imagen0 = "C:/Users/Lveas/Desktop/Amor/imagenes/tilina.png"
    #imagen0 = Image.open(n)
    #imagen0 = ImageTk.PhotoImage(imagen0)
    #imagen0 = imagen.resize((200, 200))
    #imagen0_label = Label(image=imagen0)
    #imagen0_label.config(image=imagen0)
    #imagen0_label.image = imagen
    #imagen0_label.pack(pady=40)











#imagen0_label = Label(root)
#imagen0_label.pack()

imagen_label = Label(root)
imagen_label.pack()

root.mainloop()

