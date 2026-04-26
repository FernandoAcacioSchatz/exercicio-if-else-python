print("Informe sua data de aniversario. Ex. dd/mm/aaa")
dia = int(input("Dia: "))
if dia < 1 or dia > 31:
    print("Dia invalido, recomeçe")
else:
    mes = int(input("Mês: "))
    if mes < 1 or mes > 12:
        print("Mês invalido, recomeçe")
    else:
        if (
            (mes == 1 and dia > 31)
            or (mes == 2 and dia > 28)
            or (mes == 3 and dia > 31)
            or (mes == 4 and dia > 30)
            or (mes == 5 and dia > 31)
            or (mes == 6 and dia > 30)
            or (mes == 7 and dia > 31)
            or (mes == 8 and dia > 31)
            or (mes == 9 and dia > 30)
            or (mes == 10 and dia > 31)
            or (mes == 11 and dia > 30)
            or (mes == 12 and dia > 31)
        ):
            print("Dia invalido para o mês digitado, recomeçe")
        else:
            ano = int(input("Ano: "))
            if ano > 2013:
                print("Ano invalido, recomeçe")
            else:
                print(f"Data de aniversario: {dia}/{mes}/{ano} é válida")
                print(f"Em 2013 voê tinha {2013 - ano} anos")
