vstup1 = input ("Zadej první číslo: ")
vstup2 = input ("Zadej druhé číslo: ")
cislo1 = float (vstup1)
cislo2 = float (vstup2)

vstup3 = input ("Vyber si číselnou operaci: / -> dělení, * -> násobení, + -> sčítání, - -> odčítání: ")
operace = str(vstup3)
if operace == "+":
    print("Výsledek je " + str(cislo1 + cislo2) + ".")
elif operace == "-": 
    print("Výsledek je " + str(cislo1 - cislo2) + ".")
elif operace == "/": 
    print("Výsledek je " + str(cislo1 / cislo2) + ".")
else:
    print("Výsledek je " + str(cislo1 * cislo2) + ".")


    


    