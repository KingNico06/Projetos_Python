#Lucas Fernandes Ultramari Machado - RGM: 11241105269
#Nícolas Birche Ferri Barbosa      - RGM: 11241103616

import os
os.system("cls")
print("--"*50)
print("\n\t\tCroud de livros.\n")
print("__"*50)
print("Nome do Livro    Código      Volume      Autor")
print("XXXXXXXXXXXXX    XXXXXX      XXXXXX      XXXXX")
print("--"*50)

lista = []
info = []
opcao = 0

while opcao != 6:
    print("         MENU")
    print("1 - Cadastrar livro.")
    print("2 - Listar.")
    print("3 - Listar determinado livro.")
    print("4 - Alterar por nome do livro.")
    print("5 - Excluir por nome do livro.")
    print("6 - Sair")
    print("--"*50)
    opcao = int(input("Digite sua opção: "))
    os.system("cls")
    match opcao:
        case 1:
            info.append(input(f"Digite o nome do livro: ")) 
            info.append(input(f"Digite o código do livro: ")) 
            info.append(input(f"Digite o volume do livro: "))
            info.append(input(f"Digite o nome do autor do livro: "))
            lista.append(info[:])
            info.clear()
            os.system("cls")
        case 2:
            for e in lista:
                print("Nome do livro: ", e[0])
                print("Código do livro: ", e[1])
                print("Volume do livro: ", e[2])
                print("Autor do livro: ", e[3])
                print("--"*50)
            input("Aperte Enter para voltar ao menu!")
            os.system("cls")
        case 3:
            l = 0
            pesq = input("Digite o nome do livro que deseja pesquisar: ")
            os.system("cls")
            for e in lista:
                if pesq == e[0]:
                    l = 1
                    print(f"O código do livro {e[0]} é {e[1]} e o autor é: {e[3]}.")
            if l == 0:
                print("Nome não cadastrado!")
            input("Aperte Enter para voltar ao menu!")
            os.system("cls")
        case 4:
            achou = 0
            pesq = input("Digite o nome para alterar: ").upper()
            for e in lista:
                achou = 1
                print("1 - Alterar código\n2 - Alterar volume\n3 - Alterar autor\n4 - Alterar tudo")
                opcao = int(input("Digite sua opção: "))
                if opcao == 1:
                    e[1] = input("Digite o novo código: ")
                    print("--"*50)
                    print(f"O novo código do livro {e[0]} é: {e[1]}")
                    input("Digite Enter para voltar ao Menu!")
                elif opcao == 2:
                    e[2] = input("Digite o novo volume: ")
                    print("--"*50)
                    print(f"O novo volume do livro {e[0]}é: {e[2]}")
                    input("Digite Enter para voltar ao Menu!")
                elif opcao == 3:
                    e[3] = input("Digite o novo autor: ")
                    print("--"*50)
                    print(f"O novo autor do livro {e[0]} é: {e[3]}")
                    input("Digite Enter para voltar ao Menu!")
                else:
                    e[1] = input("Digite o novo código: ")
                    os.system("cls")
                    e[2] = input("Digite o novo volume: ")
                    os.system("cls")
                    e[3] = input("Digite o novo autor: ")
                    
                    print("--"*50)
                    print(f"O novo código do livro {e[0]} é {e[1]}, o novo volume do livro é: {e[2]}º volume. E seu novo autor é:{e[3]}.")
                    input("Digite Enter para voltar ao Menu!")
        case 5:
            achou = 0
            pesq = input("Digite o nome para excluir: ").upper()
            for e in lista:
                achou = 1
                esc = input("Deseja realmente excluir?(S/N): ").upper()
                if esc == "S":
                    lista.remove(e)
            input("Digite Enter para voltar ao Menu!")
print("--"*50)
print("\n\n")