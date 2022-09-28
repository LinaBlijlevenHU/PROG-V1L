# Accumulator loop pattern
# For-loop (opsommen met integer)
def opsommen(lijst):

    # We beginnen met tellen op 0
    som = 0

    # Voor elk getal in de lijst
    for getal in lijst:
        # Tel op bij de som
        som += getal            # som = som + getal

    # Geef de hele som terug
    return som

lijst = [1, 2, 3, 4, 5]
print(opsommen(lijst))                  # 15

# For-loop (toevoegen string)
def imploderen(lijst):

    # We beginnen met een lege string
    res = ''

    # Voor elke string in de gegeven lijst
    for s in lijst:
        # Voeg de huidige string toe aan de resultaat string (dit heet concatenation)
        res += s

    # Geef het resultaat terug
    return res

letterlijst = ['a', 'b', 'c', 'd']
print(imploderen(letterlijst))          # abcd

# For-loop (operatie op een lijst)
def kwadratenlijst(lijst):

    # Lege lijst voor het resultaat
    res = []

    # Loop over alle getallen in de lijst
    for getal in lijst:
        # Bereken het kwadraat
        kwadraat = getal**2

        # Voeg het kwadraat toe aan de lijst (append)
        res.append(kwadraat)

    # Geef de nieuwe lijst terug
    return res

lijst = [1, 2, 3, 4, 5]
print(kwadratenlijst(lijst))            # [1, 4, 9, 16, 25]

# One-way if-statement
betaald, prijs = 100, 113
if (betaald < prijs):
    print("Je hebt niet genoeg betaald.")

# Two-way
betaald, prijs = 150, 113
if (betaald < prijs):
    print("Je hebt niet genoeg betaald.")
else: # Impliciet: betaald >= prijs
    print("Je hebt genoeg betaald.")

# Multi-way
betaald, prijs = 113, 113
if (betaald < prijs):
    print("Je hebt niet genoeg betaald.")
elif (betaald == prijs):
    print("Je hebt precies genoeg betaald.")
else:
    print("Je hebt genoeg betaald. Je wisselgeld wordt berekend.")

# Nested if-constructie
betaald, prijs = 120, 113
if (betaald < prijs):
    print("Je hebt niet genoeg betaald.")
else: # betaald >= prijs
    print("Bedankt voor uw aankoop!")
    if (betaald == prijs):
        print("U heeft gepast betaald, u ontvangt geen wisselgeld.")
    else: # betaald > prijs
        print("Uw wisselgeld wordt nu berekend.")

print("\n\n\n")
# Volgorde van condities
score = -50

if (score < 0):
    print("Sorry, je hebt deze toets nog niet gemaakt.")
elif (score < 50): # >=0
    print("Je hebt een onvoldoende.")
else: # >= 50
    print("Je hebt een voldoende.")

print("\n\n\n")
# Iteration loop pattern (per karakter)
infile = open('kaartnummers.txt')
content = infile.read()
for char in content:
    print(char, end='')
    print('-', end='')
infile.close()
print("\n")

# Iteration loop pattern (per regel)
infile = open('kaartnummers.txt')
lines = infile.readlines()
for line in lines:
    print(line, end='')
infile.close()

print("\n\n\n")
# Counter loop pattern
dieren = ['kip', 'koe', 'konijn']

# For-each loop
for dier in dieren:
    print(dier)

# For-loop met indices
for i in range(len(dieren)):
    print(dieren[i])

print("\n\n\n")
# Write function acronym() that:
# • takes a phrase (i.e., a string) as input
# • returns the acronym for the phrase
def acronym(zin):

    # Zet de zin om naar hoofdletters
    upper_zin = zin.upper()

    # Splits de zin in woorden
    woorden = upper_zin.split()

    # Sla het acronym op
    ac = ''

    # Loop over de woorden
    for woord in woorden:
        ac += woord[0]

    # Geef het acronym terug
    return ac

print(acronym("Be right back"))                 # BRB
print(acronym("Een aap die geen bananen eet"))  # EADGBE

# Nested loop pattern

# 1A, 1B, 1C, 1D, 2A, 2B...
for i in range(1, 5):
    for j in ['A', 'B', 'C', 'D']:
        print(f"Klas {i}{j}")

# 1A, 2A, 3A, 4A, 1B, 2B...
for klas_letter in ['A', 'B', 'C', 'D']:
    for klas_nummer in range(1, 5):
        print(f"Klas {klas_nummer}{klas_letter}")

print("\n\n\n")
# Two-dimensional lists
f = open('kaartnummers.txt')
lines = f.readlines()

personen = []

# Loop over de lines uit het tekstbestand
for line in lines:
    # Strip de new line commando's
    clean_line = line.strip("\n")

    # Split de regel in een nummer en een naam
    persoon = clean_line.split(', ')

    # Sla de persoonsinformatie op
    personen.append(persoon)

for persoon in personen:
    naam, nummer = persoon[1], persoon[0]
    print(f"{naam} heeft kaartnummer {nummer}")

# Nested loop pattern and 2-D lists
for persoon in personen:
    for informatie in persoon:
        print(informatie)

# Implement function pixels() that takes as input:
# • a two-dimensional list of nonnegative integer entries (representing the
# values of pixels of an image)
# and returns the number of entries that are positive (i.e., the number of pixels that are
# not dark). Your function should work on two-dimensional lists of any size.
def pixels(image):

    return

image = [[1, 4, 5, 0], [4, 5, 3, 0], [0, 0, 3, 1], [14, 7, 9, 0]]
print(pixels(image))