import os 
os.system("cls") 
print("Agenda") 

agenda = [] 
dados = [] 
op = 0 
while op != 6: 
    print("1 Cadastrar") 
    print("2 - Listar") 
    print("3 - Listar determinado amigo") 
    print("4 - Alterar por nome") 
    print("5 - Excluir por nome") 
    print("6 - Sair") 
    
    op = int(input("Digite sua opção: "))
    os.system("cls")
    match op: 
        case 1: 
            dados.append(input(f"Digite o nome: ")) 
            dados.append(input(f"Digite o email: ")) 
            dados.append(input(f"Digite o celular: ")) 
            agenda.append(dados[:]) 
            dados.clear()
            os.system("cls")
        case 2: 
            for e in agenda: 
                print("Nome : ",e[0]) 
                print(f"Email: {e[1]}") 
                print(f"Celular: {e[2]}")
                print("--"*50)
        case 3:
            x = 0
            pesq = input("Digite o nome que deseja pesquisar: ")
            os.system("cls")
            for e in agenda:
                if pesq == e[0]:
                    x = 1
                    print(f"O celular de {e[0]} é {e[2]} e seu email é: {e[1]}.")
            if x == 0:
                print("Nome não cadastrado!")
        case 4:
            achou = 0
            pesq = input("Digite o nome para alterar: ").upper()
            for e in agenda:
                achou = 1
                print("1 - Alterar e-mail\n2 - Alterar celular")
                opcao = int(input("Digite sua opção: "))
                if opcao == 1:
                    e[1] = input("Digite o novo e-mail: ")
                else:
                    e[2] = input("Digite o novo celular: ")
                print(f"o novo celular de {e[0]} é {e[2]}, e seu novo e-mail é:{e[1]}.")
        case 5:
            print()