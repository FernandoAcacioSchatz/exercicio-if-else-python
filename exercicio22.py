maior = 0
menor = 0

print("Digite três números")
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Terceiro número: "))

if num1 == num2 and num1 == num3:
    print("Os três números são iguais")
else:
    if num1 > num2 and num1 > num3:
        maior = num1
    elif num2 > num1 and num2 > num3:
        maior = num2
    else:
        maior = num3

    if num1 < num2 and num1 < num3:
        menor = num1
    elif num2 < num1 and num2 < num3:
        menor = num2
    else:
        menor = num3
    print(f"O número {maior} é maior e número {menor} é o menor")
