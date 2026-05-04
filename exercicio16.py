print("Digite o valor de A, B, C de uma equação do segundo grau: ")
a = 0
a = float(input("Digite o valor de A: "))


if a == 0:
    print("Programa encerrado")
else:
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))
    delta = b**2 - 4 * a * c
    if delta < 0:
        print("A equação não possui raízes reais")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"A equação possui uma raiz real: {x:.2f}")
    else:
        x1 = (-b + delta**0.5) / (2 * a)
        x2 = (-b - delta**0.5) / (2 * a)
        print(f"A equação possui duas raízes reais: {x1:.2f} e {x2:.2f}")
