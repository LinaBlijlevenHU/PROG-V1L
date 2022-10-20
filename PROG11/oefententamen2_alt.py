# Vraag om drie getallen
a = int(input("Eerste getal: "))
b = int(input("Tweede getal: "))
c = int(input("Derde getal: "))

# Getallen in een lijst
lijst = [a, b, c]

def max_lijst(lijst):
    # Stel in op een van de getallen
    max_getal = a

    # We loopen over de getallen
    for getal in lijst:
        # Is het huidige getal groter dan de huidige max?
        if getal > max_getal:
            # Werk het hoogste getal (tot nu toe) bij.
            max_getal = getal

    return max_getal

def min_lijst(lijst):

    # Stel in op een van de getallen
    min_getal = a

    for getal in lijst:
        if getal < min_getal:
            min_getal = getal

    return min_getal

max_getal = max_lijst(lijst)
min_getal = min_lijst(lijst)

if (a != max_getal and a != min_getal):
    print(f"Het middelste getal is {a}")
elif (b != max_getal and b != min_getal):
    print(f"Het middelste getal is {b}")
else:
    print(f"Het middelste getal is {c}")
