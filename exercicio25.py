print("Verificação de um possível doador de sangue")
idade = int(input("Digite sua idade: "))
if idade < 18 or idade > 67:
    print("Não é possível doar sangue")
    if idade < 18:
        print("Não alcançou a idade mínina")
    elif idade > 67:
        print("Ultrapassou a idade máxima")
else:
    print(f"Com {idade} anos é possível doar sangue")
