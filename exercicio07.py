print("Digite três números:")

num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
num3 = float(input("Número 3: "))
print()
if num1 > num2 and num1 > num3:
    print(f"O maior número é: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"O maior número é: {num2}")
else:
    print(f"O maior número é: {num3}")

if num1 < num2 and num1 < num3:
    print(f"O menor número é: {num1}")
elif num2 < num1 and num3 < num2 < num3:
    print(f"O menor número é: {num2}")
else:
    print(f"O memor número é: {num3}")
