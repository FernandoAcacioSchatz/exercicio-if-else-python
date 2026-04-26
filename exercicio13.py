dias = int(input("Digite o número correspondente ao dia da semana: "))
if dias < 1 or dias > 7:
    print("Valor Inválido")
else:
    if dias == 1:
        print("Domingo")
    elif dias == 2:
        print("Segunda")
    elif dias == 3:
        print("Terça")
    elif dias == 4:
        print("Quarta")
    elif dias == 5:
        print("Quinta")
    elif dias == 6:
        print("Sexta")
    elif dias == 7:
        print("Sábado")
    else:
        print("Valor Inválido")
