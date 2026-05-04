result = 0
num1 = float(input("Digite um número: "))
operador = input("Digite a operação desejada. Ex: + - * /: ")
if operador == "+" or operador == "-" or operador == "*" or operador == "/":
    num2 = float(input("Digite um nuúmero: "))
    if operador == "+":
        result = num1 + num2
        print(f"A soma de {num1} + {num2} = {result}")
    elif operador == "-":
        result = num1 - num2
        print(f"A subtração de {num1} - {num2} = {result}")
    elif operador == "*":
        result = num1 * num2
        print(f"A multiplicação entre {num1} * {num2} = {result}")
    elif operador == "/":
        result = num1 / num2
        print(f"A divisão entre {num1} / {num2} = {result}")
else:
    print("Operadr invalido, tente novamente")

if result % 2 == 0:
    print(f"O resultado {result} é par")
else:
    print(f"O resultado {result} é impar")

if result >= 0:
    print(f"O resultado {result} é positivo")
else:
    print(f"O resultado {result} é negativo")
