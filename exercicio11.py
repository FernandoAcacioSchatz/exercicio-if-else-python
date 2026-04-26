salario = float(input("Digite o salário do colaborador: "))
reajuste = 0
percentual = 0
salario_reajustado = 0
if salario <= 280:
    percentual = 0.20
    reajuste = salario * percentual
    salario_reajustado = salario + reajuste
elif salario <= 700:
    percentual = 0.15
    reajuste = salario * percentual
    salario_reajustado = salario + reajuste
elif salario <= 1500:
    percentual = 0.10
    reajuste = salario * percentual
    salario_reajustado = salario + reajuste
else:
    percentual = 0.05
    reajuste = salario * percentual
    salario_reajustado = salario + reajuste

print(f"Salário antes do reajuste: R${salario:.2f}")
print(f"Percentual de reajuste: {percentual * 100:.0f} %")
print(f"Reajuste: R${reajuste:.2f}")
print(f"Salário após o reajuste: R${salario_reajustado:.2f}")
