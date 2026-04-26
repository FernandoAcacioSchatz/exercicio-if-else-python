print("Detetive")
s = 0
n = 0
print("Responda somente com S para SIM ou N para NÂO")

telefonou = input("Você telefonou pra vítima?  ").lower()
if telefonou == "s" or telefonou == "n":
    if telefonou == "s":
        s = telefonou.count("s")
    else:
        telefonou = "n"
        n = telefonou.count("n")
    esteve = input("Você esteve no local? ").lower()
    if esteve == "s" or esteve == "n":
        if esteve == "s":
            s += esteve.count("s")
        else:
            esteve = "n"
            n += esteve.count("n")
        mora = input("Você mora perto vítima?  ").lower()
        if mora == "s" or mora == "n":
            if mora == "s":
                s += mora.count("s")
            else:
                mora = "n"
                n += mora.count("n")
            devia = input("Você tinha alguma divida com a vítima?  ").lower()
            if devia == "s" or devia == "n":
                if devia == "s":
                    s += devia.count("s")
                else:
                    devia = "n"
                    n += devia.count("n")
                trab = input("Você já trabalho com a vítima?  ").lower()
                if trab == "s" or trab == "n":
                    if trab == "s":
                        s += trab.count("s")
                    else:
                        trab = "n"
                        n += trab.count("n")
                if s == 2 or n == 3:
                    print("\nSUSPEITO")
                elif s == 3 or s == 4 or n == 2 or n == 1:
                    print("CÚMPLICE")
                elif s == 5 or n == 0:
                    print("ASSASSINO")
                else:
                    print("INOCENTE")
else:
    print("Responda somente com 's' ou 'n'")
