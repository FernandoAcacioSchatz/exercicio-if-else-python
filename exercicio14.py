nota1 = float(input("Digite a primeira nota: "))
if nota1 < 0 or nota1 > 10:
    print("Valor Inválido")
nota2 = float(input("Digite a segunda nota: "))
if nota2 < 0 or nota2 > 10:
    print("Valor Inválido")
media = (nota1 + nota2) / 2

if media >= 9 and media <= 10:
    conceito = "A"
elif media >= 7.5 and media < 9:
    conceito = "B"
elif media >= 6 and media < 7.5:
    conceito = "C"
elif media >= 4 and media < 6:
    conceito = "D"
else:
    conceito = "E"
print()
print(f"Média de aproveitamento")
print(f"Entre {nota1:.1f} e {nota2:.1f}")
print(f"Média: {media:.1f}")
print(f"Conceito: {conceito}")
