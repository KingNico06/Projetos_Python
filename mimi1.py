import os
from tkinter import *
c=os.path.dirname(__file__)
nomearq = c +"\\banco.txt"

def gravardados():
    arquivo = open(nomearq, "a")
    arquivo.write("\nNome:%s"% vnome.get())
    arquivo.write("\nCPF:%s"% vcpf.get())
    arquivo.write("\nEmail:%s"% vemail.get())
    arquivo.write("\nObservação:%s"% vobs.get(1.0, END))
    arquivo.write("--"*50)
    arquivo.write("\n\n")
    arquivo.close()
    vnome.delete(0, END)
    vcpf.delete(0, END)
    vemail.delete(0, END)
    vobs.delete("1.0", END)

pw = Tk()

pw.geometry("800x700")
pw.title("Projeto: Let's Go!")
pw.configure(background="#dde")

Label(pw, text="Nome", background="#dde", foreground="#000", anchor=W).place(x=10, y=10, width=250, height=30)
vnome=Entry(pw)
vnome.place(x=10, y=30, width=250, height=30)

Label(pw, text="CPF", background="#dde", foreground="#000", anchor=W).place(x=10, y=90, width=150, height=30)
vcpf=Entry(pw)
vcpf.place(x=10, y=110, width=150, height=30)

Label(pw, text="Email", background="#dde", foreground="#000", anchor=W).place(x=10, y=170, width=200, height=30)
vemail=Entry(pw)
vemail.place(x=10, y=190, width=200, height=30)

Label(pw, text="Observações", background="#dde", foreground="#000", anchor=W).place(x=10, y=250, width=300, height=30)
vobs=Text(pw)
vobs.place(x=10, y=270, width=300, height=200)



Button(pw,text="Gravar", command=gravardados).place(x=10,y=500,width=200,height=20)



pw.mainloop()