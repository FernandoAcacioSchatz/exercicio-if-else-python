maior = 0
menor = 0

print("Digite dois números")
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))

if num1 > num2:
    maior = num1
    memor = num2
else:
    maior = num2
    menor = num1
print(f"{maior} é maior que {menor}")
