print("Digite o valor dos lados de um triângulo:")
lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

if ((lado1 + lado2) < lado3) or ((lado1 + lado3) < lado2) or ((lado3 + lado2) < lado1):
    print("Valores inválidos")
else:
    if lado1 == lado2 and lado1 == lado3:
        print("Triângulo Equilátero")
    elif (
        (lado1 == lado2 and lado1 != lado3)
        or (lado1 == lado3 and lado1 != lado2)
        or (lado2 == lado3 and lado2 != lado1)
    ):
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
