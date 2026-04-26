# Faça um programa que peça dois números e imprima o maior deles
# Dica: para realizar a inserção de dados pelo usuário utilize a função input("texto para o usuario")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O maior número é {num1}")
elif num1 == num2:
    print(f"Os números são iguais: {num1} e {num2} ")
else:
    print(f"O maior número é {num2}")
