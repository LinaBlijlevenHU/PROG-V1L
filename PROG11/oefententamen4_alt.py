# Opdracht 4:
# Schrijf een programma waarin een gebruiker getallen moet invoeren. Dit gaat door totdat de gebruiker ‘stop’
# intoetst. De getallen moeten met elkaar vermenigvuldigd worden. Print het resultaat. - https://prnt.sc/xkYL5YKbrfSO
import math

# Houd het product bij
prod_lijst = 1

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
        prod_lijst = prod_lijst * int(getal)     # prod_lijst *= int(getal)

print(f"Je getallen zijn ingevoerd. Het product is {prod_lijst}")