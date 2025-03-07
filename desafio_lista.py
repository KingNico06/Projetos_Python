import os
import time
os.system("cls")

print("A Companhia de Taxi LocalCerto armazena os dados de seus motoristas (codigo,nome, número do taxi e Kper). Elabore um programa capaz de ler os dados de n (máximo de 20) motoristas (utilizar uma lista de lista).")
print("Em seguida, o programa deve imprimir um relatório conforme o modelo abaixo.")
print("Nome Motorista  Nº Taxi    Valor a Receber")
print("XXX              XXXX           XXX")
print("O valor a receber é calculado multiplicando-se a quantidade Kper (Kilometro percorrido) por R$ 1,20.")
print("Ao final o programa deve também exibir todos os dados do motorista com maior valor a receber.")
print("-"*50)

agenda = [] 
dados = [] 
op = 0 
while op != 6: 
    print("1 - Cadastrar") 
    print("2 - Listar") 
    print("3 - Listar determinado amigo") 
    print("4 - Alterar por nome") 
    print("5 - Excluir por nome") 
    print("6 - Sair") 
    
    op = int(input("Digite sua opção: "))
    os.system("cls")
    match op: 
        case 1: 
            dados.append(input(f"Digite o nome do motorista: ")) 
            dados.append(input(f"Digite o número do táxi: ")) 
            distper = dados.append(float(input(f"Digite a distância percorrida (em Km): "))) 
            agenda.append(dados[:])
            dados.clear()
            os.system("cls")
        case 2: 
            for e in agenda: 
                print("Nome do motorista: ",e[0]) 
                print(f"Nº Táxi: {e[1]}") 
                print(f"Distância percorrida: {e[2]} km.")
                print("--"*50)
        case 3:
            x = 0
            pesq = input("Digite o nome que deseja pesquisar: ")
            os.system("cls")
            for e in agenda:
                if pesq == e[0]:
                    x = 1
                    print(f"O nº do carro de {e[0]} é {e[1]} e seu email é: {distper:.2f}.")
            if x == 0:
                print("Nome não cadastrado!")
        case 4:
            achou = 0
            pesq = input("Digite o nome para alterar: ").upper()
            for e in agenda:
                achou = 1
                print("1 - Alterar nº táxi\n2 - Alterar distância percorrida\n3 - Alterar tudo")
                opcao = int(input("Digite sua opção: "))
                if opcao == 1:
                    e[1] = input("Digite o novo nº táxi: ")
                    print("--"*50)
                    print(f"O novo nº táxi do motorista {e[0]} é: {e[1]}")
                    input("Digite Enter para voltar ao Menu!")
                elif opcao == 2:
                    e[2] = input("Digite a nova distância percorrida: ")
                    print("--"*50)
                    print(f"A nova distância percorrida  do motorista {e[0]}é: {e[2]}")
                    input("Digite Enter para voltar ao Menu!")
                else:
                    e[1] = input("Digite o novo nº táxi: ")
                    os.system("cls")
                    e[2] = input("Digite a nova distância percorrida: ")
                    os.system("cls")
                    
                    print("--"*50)
                    print(f"O novo número táxi do motorista {e[0]} é {e[1]}, e a nova distância percorrida é: {e[2]} quilômetros rodados.")
                    input("Digite Enter para voltar ao Menu!")
        case 5:
            achou = 0
            pesq = input("Digite o nome para excluir: ").upper()
            for e in agenda:
                achou = 1
                esc = input("Deseja realmente excluir?(S/N): ").upper()
                if esc == "S":
                    agenda.remove(e)
                    print("Dados removidos com sucesso!")
            input("Digite Enter para voltar ao Menu!")
print("--"*50)
print("\n")
print("Obrigado por utilizar nosso programa!\n\t(: !!VOLTE SEMPRE!! :)")
print("\n")
print("--"*50)