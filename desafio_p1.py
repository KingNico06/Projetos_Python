from tkinter import *
import os
os.system("cls")

caminho =os.path.dirname(__file__)
nomearq = caminho + "\\salario.txt"


rh= Tk()
rh.geometry("800x700")
rh.title("Projeto: Let's Go!")
rh.configure(background="#dde")

def gravardados():
    arquivo = open(nomearq, "a")
    arquivo.write("__"*50)
    arquivo.write("\nSalário mínimo:%s"% sal_min.get())
    arquivo.write("\nTurno:%s"% turno.get())
    arquivo.write("\nCategoria:%s"% categoria.get())
    arquivo.write("\nHoras trabalhadas:%s"% ht.get())
    arquivo.write("--"*50)
    arquivo.write("\n\n")
    arquivo.close()
    sal_min.delete(0, END)
    turno.delete(0, END)
    categoria.delete(0, END)
    ht.delete(0, END)

Label(rh, text="""Programa que recebe o valor de um salário, o turno de trabalho, a categoria,
\no número de horas trabalhadas, calcula e mostra os resultados.
\nBem-vindo(a)!""", background="#fff", foreground="#000", anchor=W).place(x=10, y=10, width=500, height=90)


Label(rh, text="R$", background="#fff", foreground="#000", anchor=W).place(x=10, y=150, width=250, height=30)
Label(rh, text="Digite o valor do salário mínimo: ", background="#dde", foreground="#000", anchor=W).place(x=10, y=120, width=250, height=30)
sal_min=Entry(rh)
sal_min.place(x=30, y=150, width=250, height=30)

Label(rh, text="Digite seu turno: ", background="#dde", foreground="#000", anchor=W).place(x=10, y=290, width=250, height=30)
turno=Entry(rh)
turno.place(x=10, y=320, width=250, height=30)

Label(rh, text="""Períodos:
    \n ->Matutino
     ->Verspetino
     ->Noturno""", background="#fff", foreground="#000", anchor=W).place(x=10, y=200, width=500, height=80)

Label(rh, text="""Categorias disponíveis:
              Gerente
              Operário""", background="#fff", foreground="#000", anchor=W).place(x=550, y=10, width=200, height=90)

Label(rh, text="Digite sua categoria: ", background="#dde", foreground="#000", anchor=W).place(x=550, y=110, width=200, height=30)
categoria=Entry(rh)
categoria.place(x=550, y=140, width=200, height=30)

Label(rh, text="Horas trabalhadas: ", background="#dde", foreground="#000", anchor=W).place(x=550, y=170, width=200, height=30)
ht=Entry(rh)
ht.place(x=550, y=200, width=200, height=30)

Button(rh,text="Gravar", command= gravardados).place(x=10,y=500,width=200,height=20)
Button(rh,text="Avançar").place(x=220,y=500,width=200,height=20)
Button(rh,text="Fechar", command= rh.quit).place(x=10,y=580,width=200,height=20)


rh.mainloop()
