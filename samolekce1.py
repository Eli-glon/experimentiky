print ("Hello World")
print ("*"*10)
print ("10"+"10")
a=4.8
print(int (a))
print ( int (a) + 5)
print (3>5)

print ("*"*20)
retezec_znaku = 9.5
print(retezec_znaku)
print(type(retezec_znaku))


x = 10
while x > 0:
    x=x-1
    print ("zbývá " + str(x) + " opakování")
print ("Konec cyklu")


vstup = input ("Zadej svůj věk: ")
vek = int (vstup)

if vek >= 65: 
   
    if vek < 100: 
        print ("Tvůj věk je: " + str (vek) +" let a jsi důchodce")
    else:
        print ("Tvůj věk je: " + str (vek) +" let a jsi důchodce")

    print ("Můžeš celý den krmit hluby")
elif vek >= 18:
    print ("Tvůj věk je " + str (vek) + " let a jsi dospělí")
    print ("Můžeš chlastat a musíš pracovat aby ostatní mohli krmit holuby")
else: 
    if vek > 4 : 
       print ("Tvůj věk je " + str (vek) + " let a jsi nezletílý")
    else:
       print ("Tvůj věK je " + str (vek) + " roků a jsi nezletilý")
    print ("Nemůžeš chlastat a musíš chodit do školy")

print ("*"*10)

vstup1 = input ("Zadej první číslo: ")
vstup2 = input ("Zadej druhé číslo: ")
cislo1 = float (vstup1)
cislo2 = float (vstup2)

vstup3 = input ("Vyber si číselnou operaci: / -> dělení, * -> násobení, + -> sčítání, - -> odčítání: ")
operace = str(vstup3)
if operace == "+":
    print("Výsledek je " + str(cislo1 + cislo2))
elif operace == "-": 
    print