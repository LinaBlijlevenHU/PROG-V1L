# Opdracht 5:
# Schrijf een programma waarin je de gebruiker een string laat invoeren.
# Gebruik vervolgens een for-loop om de omgekeerde string te printen. - https://prnt.sc/pxh6mG2GI0-U

# Input
zin = input("Voer een string in: ")

# String om op te bouwen
omgekeerd = ""

# Voor elk karakter in de zin
for c in zin:
    omgekeerd = c + omgekeerd

print(omgekeerd)