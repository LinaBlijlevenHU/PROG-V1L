# Opdracht 5:
# Schrijf een programma waarin je de gebruiker een string laat invoeren.
# Gebruik vervolgens een for-loop om de omgekeerde string te printen. - https://prnt.sc/pxh6mG2GI0-U

# Input
zin = input("Voer een string in: ")

# String om op te bouwen
omgekeerd = ""

# Maak een lijst van indices
indices = range(0, len(zin))

# Zet de indices om naar een lijst
indices = [x for x in indices]

# Draai de volgorde van de indices om
indices.reverse()

# Loop over de indices
for i in indices:
    # Voeg toe aan de zin van achteren naar voren
    omgekeerd += zin[i]

print(omgekeerd)
