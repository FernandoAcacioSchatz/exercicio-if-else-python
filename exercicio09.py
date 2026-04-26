print("Digite três números:")

maior = 0
meio = 0
menor = 0

num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
num3 = float(input("Número 3: "))
print()

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3

if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num3 < num2 < num3:
    menor = num2
else:
    menor = num3


if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
    meio = num1
elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
    meio = num2
else:
    meio = num3


print(maior)
print(meio)
print(menor)
