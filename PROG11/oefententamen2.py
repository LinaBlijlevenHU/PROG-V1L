# Opdracht 2
# Schrijf een programma waarin de gebruiker drie getallen kan invullen.
# Print vervolgens het middelste (qua grootte) getal. - https://prnt.sc/FoVpjW0Vdjby

# Vraag om drie getallen
a = int(input("Eerste getal: "))
b = int(input("Tweede getal: "))
c = int(input("Derde getal: "))

# Getallen in een lijst
lijst = [a, b, c]

# Sorteer de lijst
lijst.sort()

# Print het middelste getal
print(lijst[1])