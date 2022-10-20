# Opdracht 4:
# Schrijf een programma waarin een gebruiker getallen moet invoeren. Dit gaat door totdat de gebruiker ‘stop’
# intoetst. De getallen moeten met elkaar vermenigvuldigd worden. Print het resultaat. - https://prnt.sc/xkYL5YKbrfSO
import math

# Lege lijst voor de getallen
getallenlijst = []

# In het begin vragen we altijd een getal
vraag_getal = True

while vraag_getal:
    # Vraag input van de gebruiker
    getal = input("Voer een getal in, of 'stop' om te stoppen: ")

    # Moeten we al stoppen?
    if (getal == "stop"):
        vraag_getal = False
    # We hebben een getal
    else:
        getallenlijst.append(int(getal))

print(f"Je getallen zijn ingevoerd. {getallenlijst}")

# Aanpak met math
print(math.prod(getallenlijst))

# Houd het product bij
prod_lijst = 1

# Loopen over de getallen
for getal in getallenlijst:
    prod_lijst = prod_lijst * getal     # prod_lijst *= getal

print(f"Het product van de lijst is {prod_lijst}")