import os
os.system("cls")
dados = []
taxistas = []
op = 0

while op != 4:
    os.system("cls")
    print("Empresa LocalCerto")
    print("1 - Cadastro.")
    print("2 - Listagem.")
    print("3 - Listar dados do taxista com maior valor a receber.")
    print("4 - Sair.")
    op = int(input("Digite sua opção: "))
    match op:
        case 1:
            print()