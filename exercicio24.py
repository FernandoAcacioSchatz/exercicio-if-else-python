import math

print("Calculo do Diâmetro, Circunferência e Área de um Círculo")
raio = float(input("Digite o raio do círculo: "))

diametro = raio * 2
comprimento = 2 * math.pi * raio
area = math.pi * (raio**2)

print(f"\nDiâmetro de uma circunferência de raio {raio} é de {diametro:.2f}")
print(f"Comprimento de uma circunferência de raio {raio} é de {comprimento:.2f}")
print(f"Área de uma cricunferência de raio {raio} é de {area:.2f}")
