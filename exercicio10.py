turno = input(
    "Digite o turno que você estuda. M matutino, V verpertino, N noturno: "
).lower()
if turno == "m":
    print("Bom dia")
elif turno == "v":
    print("Boa tarde")
elif turno == "n":
    print("Boa noite")
else:
    print("Valor inválido")
