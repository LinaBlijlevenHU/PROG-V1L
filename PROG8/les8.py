# Import num(erical)py(thon) voor het werken met NaN (not a number)
import numpy as np

#########
# While #
#########

# Wisselgeld met operatoren
wisselgeld = 212

aantal50 = 212 // 50                # math.floor(212 / 50)
rest = 212 % 50

print(f"{wisselgeld} kunnen we uitbetalen met {aantal50} muntjes met een rest van {rest}")

# Wisselgeld met while
wisselgeld = 212
aantal50 = 0

# Zo lang we nog tenminste 50 cent hebben
while wisselgeld >= 50:
    # A. Het aantal muntjes verhogen
    aantal50 += 1

    # B. Restbedrag bijwerken
    wisselgeld -= 50

    # Print voor het tussenstapje
    print(f"We hebben totaal {aantal50} muntjes uitbetaald, er is nu nog {wisselgeld} cent uit te betalen.")

print("\n\n")

####################
# Break & continue #
####################

namen = ["Thijs", "Tim", "Abe", "Gillian"]

# Break
for naam in namen:
    print(f"Hallo {naam}")

    if (naam == "Abe"):
        break

print("\n\n")
# Continue
for naam in namen:
    if (naam == "Tim"):
        continue

    print(f"Hallo {naam}")

# Continue met NaN
cijfers = [8, 3, 3, 5, np.NaN, 5]
for cijfer in cijfers:
    if (np.isnan(cijfer)):
        print("Dit is geen cijfer")
        continue

    print(f"Het kwadraat van {cijfer} is {cijfer*cijfer}")

###############################
# Tafels met continue & break #
###############################

for i in range(1, 11):
    # Sla de tafel van 7 over
    if (i == 7):
        break

    for j in range(1, 11):

        # Sla 6xi over in de tafel van i
        if (j == 6):
            continue

        if (j == 9):
            break

        print(f"{i} * {j} = {i * j}")

print("\n\n")

#########################
# Frequenties met dicts #
#########################

def frequency(item_list):
    '''
    Frequenties voor elk item in de lijst.

    :param  list
    :return dict
    '''
    counters = {}

    # We lopen door de lijst heen
    for item in item_list:
        # Hebben we dit element eerder gezien?
        if item in counters:
            # Verhoog de teller
            counters[item] += 1

            print(f"We hebben {item} nu {counters[item]} keer gezien.")
        # Nieuw element
        else:
            # Maak een teller aan
            counters[item] = 1

            print(f"We zien {item} nu voor het eerst.")
    return counters

freqs = frequency([1, 1, 1, 1, 4, 2, 5, 6])
print(freqs)

# Check of iets in de lijst staat
if (3 in freqs.keys()):
    print(f"Het getal 3 staat {freqs[3]} keer in de lijst")
else:
    print(f"Het getal 3 staat niet in de lijst.")

# Loop over de getallen
for i in range(1, 7):

    # Vraag het aantal keer dat we een item hebben gezien op,
    # gebruik 0 als deze niet in de dictionary staat.
    aantal = freqs.get(i, 0)

    print(f"Het getal {i} komt {aantal} keer voor in de lijst.")