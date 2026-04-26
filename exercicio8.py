print("Digite o valor de três produtos:")

prod1 = float(input("Valor 1: "))
prod2 = float(input("Valor 2: "))
prod3 = float(input("Valor 3: "))
print()

if prod1 < prod2 and prod1 < prod3:
    print(f"O menor Valor é: {prod1} Compre esse produto")
elif prod2 < prod1 and prod3 < prod2 < prod3:
    print(f"O menor Valor é: {prod2} Compre esse produto")
else:
    print(f"O memor Valor é: {prod3} Compre esse produto")
