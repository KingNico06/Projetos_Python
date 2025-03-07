from tkinter import *
import os 

def semcomando():
    print()


pw = Tk()
pw.geometry("500x400")
pw.title("Projeto: Let's Go!")
pw.configure(background="#dde")

barra_menus = Menu(pw)
menucontato = Menu(barra_menus, tearoff=0)
menucontato.add_command(label="Novo", command = semcomando)
menucontato.add_command(label="Pesquisar", command = semcomando)
menucontato.add_command(label="Deletar", command = semcomando)
menucontato.add_separator()
menucontato.add_command(label="Fechar", command = pw.quit)
barra_menus.add_cascade(label="Contatos", menu = menucontato)

menuman=Menu(barra_menus, tearoff=0)
menuman.add_command(label="Banco de Dados", command = semcomando)
barra_menus.add_cascade(label="Manutenção", menu = menuman)

menusobre=Menu(barra_menus, tearoff=0)
menusobre.add_command(label="Ajuda", command = semcomando)
barra_menus.add_cascade(label="Sobre", menu = menusobre)


pw.config(menu=barra_menus)
pw.mainloop()