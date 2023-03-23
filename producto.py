from tkinter import*
from PIL import ImageTk,Image
root= Tk()
#root.geometry("400x400")

ventanaPrincipal=Frame(root, bg="gray77")
ventanaPrincipal.grid()
valor=StringVar()

img=Image.open("pro.ico")
imagen=img.resize((100,70))
imag=ImageTk.PhotoImage(imagen)
miTitulo=Label(ventanaPrincipal,image=imag)
miTitulo.grid(row=2,column=0,padx=10,pady=20,columnspan=2,rowspan=2)
titulo=Label(ventanaPrincipal,text="Registro Productos",font=("Roboto",20)).grid(row=1,column=0,columnspan=2)


textnombre=Entry(ventanaPrincipal,font=("Roboto",15)).grid(row=4,column=1,padx=10,pady=10)
textnombre=Entry(ventanaPrincipal,font=("Roboto",15)).grid(row=5,column=1,padx=10,pady=20)
opciones=['CANELITAS','TRIKI TRAKETS','ZENSO']
opcion=OptionMenu(ventanaPrincipal,valor,*opciones).grid(row=8,column=1,padx=40,pady=40)

titulo=Label(ventanaPrincipal,text="PRODUCTO:",font=("Roboto",10)).grid(row=4,column=0)
titulo=Label(ventanaPrincipal,text="SKU:",font=("Roboto",10)).grid(row=5,column=0)
titulo=Label(ventanaPrincipal,text="DEPTO:",font=("Roboto",10)).grid(row=6,column=0)
titulo=Label(ventanaPrincipal,text="PROVEEDOR:",font=("Roboto",10)).grid(row=8,column=0,padx=20,pady=10)
titulo=Label(ventanaPrincipal,text="IDIOMA:",font=("Roboto",10)).grid(row=9,column=0)

control=IntVar()
preserve=Checkbutton(ventanaPrincipal,text="A",variable=control,font=("Roboto",10))
preserve.grid(row=7,column=0,pady=20,padx=10)
control2=IntVar()
preserve=Checkbutton(ventanaPrincipal,text="B",variable=control2,font=("Roboto",10))
preserve.grid(row=7,column=1,pady=20,padx=10)
control3=IntVar()
preserve=Checkbutton(ventanaPrincipal,text="C",variable=control3,font=("Roboto",10))
preserve.grid(row=7,column=2,pady=20,padx=10)
control4=IntVar()
preserve=Checkbutton(ventanaPrincipal,text="EN",variable=control4,font=("Roboto",10))
preserve.grid(row=9,column=1,pady=20)
control5=IntVar()
preserve=Checkbutton(ventanaPrincipal,text="SP",variable=control5,font=("Roboto",10))
preserve.grid(row=9,column=2,pady=20)

botonCerrar=Button(ventanaPrincipal,text="REGISTRAR",command=root.destroy,width=20,height=2).grid(row=11 , column=0,padx=10,pady=10,columnspan=2)

root.mainloop()