horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora trabalhada: "))
salario_bruto = horas_trabalhadas * valor_hora
sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11
imposto_renda = 0
inss = salario_bruto * 0.10
total_desconto = imposto_renda + inss + sindicato
porcento = 0


if salario_bruto <= 900:
    porcento = 0
    imposto_renda = porcento

elif salario_bruto <= 1500:
    porcento = 0.05
    imposto_renda = salario_bruto * porcento
    porcento = porcento * 100

elif salario_bruto <= 2500:
    porcento = 0.10
    imposto_renda = salario_bruto * porcento
    porcento = porcento * 100

else:
    porcento = 0.20
    imposto_renda = salario_bruto * porcento
    porcento = porcento * 100


salario_liquido = salario_bruto - imposto_renda - inss - sindicato
total_desconto = imposto_renda + inss + sindicato


print(f"Salário Bruto ({horas_trabalhadas} * {valor_hora}): R$ {salario_bruto:.2f}")
print(f"Imposto de Renda ({porcento:.0f}%): R$ {imposto_renda:.2f}")
print(f"INSS (10%): R$ {inss:.2f}")
print(f"Sindicato: R$ {sindicato:.2f}")
print(f"FGTS (11%): R$ {fgts:.2f} Não desconta")
print(f"Total de descontos {total_desconto:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
