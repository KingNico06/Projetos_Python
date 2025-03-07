if sal_min == 800:
    print()
    if turno == 'MATUTINO' or turno == 'VERSPETINO'or turno == 'NOTURNO':
        print()

        if categoria == 'GERENTE' or categoria == 'OPERÁRIO':
            
            if ht >0:
                if turno == 'MATUTINO':
                    coef = sal_min * 0.1
                else:
                    if turno == 'NOTURNO':
                        coef = sal_min * 0.15
                    else:
                        coef = sal_min * 0.12
            else:
                print("Valor inválido!")
        else:
            print("Valor inválido!")
    else:
        print("Valor inválido!")
else:
    print("Valor inválido!")
sal_bruto = ht * coef
if categoria == 'OPERÁRIO':
    if sal_bruto >= 300:
        imp = sal_bruto * 0.05
    else:
        imp = sal_bruto * 0.03
else:
    if sal_bruto >= 400:
        imp = sal_bruto * 0.06
    else:
        imp = sal_bruto * 0.04
if turno == 'NOTURNO' and ht >80:
    grat = 50
else:
    grat = 30
if categoria == 'OPERÁRIO' or coef <= 25:
    aux = 50
else:
    aux = 30
sal_liq = sal_bruto - imp + aux
os.system("cls")


if sal_liq < 350:
    print(f"Mal-remunerado, você recebe R${sal_liq:.2f} por ano.")
elif sal_liq > 600:
    print(f"Bem remunerado, você recebe R${sal_liq:.2f} por ano.")
else:
    print(f"Normal, você recebe R${sal_liq:.2f} por ano.")