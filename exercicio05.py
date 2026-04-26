print("Digite as duas notas do aluno: ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2


if media <= 9.9:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
else:
    print("Aprovado com Distinção")
