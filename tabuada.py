import os
os.system("cls")

cont = 1
resp = 'S'

op = input("Deseja continuar(S/N)?: ").upper()
while op == 'S':
    num = float(input("Digite um número: "))
    if num <1 or num >10:
        num = float(input("Por favor, digite um número de 1 a 10: "))
    else:
            cont +=1
            tab = num * cont
            print(tab)
