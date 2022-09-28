# Accumulator loop pattern
# For-loop (opsommen met integer)
# Dit voorbeeld werkt ook voor floats.
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

# For-loop (opbouwen van een string)
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

# For-loop (opbouwen van een lijst)
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
# Alleen if
betaald, prijs = 100, 113
if (betaald < prijs):
    print("Je hebt niet genoeg betaald.")

# Two-way
# If + else
betaald, prijs = 150, 113
if (betaald < prijs):
    print("Je hebt niet genoeg betaald.")
else: # Impliciet: betaald >= prijs
    print("Je hebt genoeg betaald.")

# Multi-way
# If, elif (eventueel meerdere keren) én else
betaald, prijs = 113, 113
if (betaald < prijs):
    print("Je hebt niet genoeg betaald.")
elif (betaald == prijs):
    print("Je hebt precies genoeg betaald.")
else:
    print("Je hebt genoeg betaald. Je wisselgeld wordt berekend.")

# Nested if-constructie
# If-statements kunnen ook if-statements bevatten.
# Zo is het bijvoorbeeld mogelijk om een stukje informatie op te bouwen.
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
# Door de volgorde ontstaan er impliciete condities voor
# elke elif en else na een if-statement. Hierdoor krijg je
# gedrag dat je niet expliciet hebt uitgeschreven.
# Met getallen is het daarom bijvoorbeeld handiger van laag naar
# hoog of andersom te werken.
score = -50

if (score < 0):
    print("Sorry, je hebt deze toets nog niet gemaakt.")
elif (score < 50): # >=0
    print("Je hebt een onvoldoende.")
else: # >= 50
    print("Je hebt een voldoende.")

print("\n\n\n")
# Iteration loop pattern (per karakter)
# Open de file
infile = open('kaartnummers.txt')
# Lees de inhoud van de file in in een string
content = infile.read()
# Loop over elk karakter in de inhoud-string
for char in content:
    # Print het karakter (en voeg geen nieuwe regel toe)
    print(char, end='')
    # Print ook een streepje
    print('-', end='')
# Sluit de file af
infile.close()
print("\n")

# Iteration loop pattern (per regel)
# Open de file
infile = open('kaartnummers.txt')
# Lees de regels uit
lines = infile.readlines()
# Loop over de regels
for line in lines:
    # Print de regel en voeg niets toe om de regel mee te eindigen
    # (de line heeft zelf al een \n)
    print(line, end='')
# Sluit de file netjes af
infile.close()

print("\n\n\n")
# Counter loop pattern
dieren = ['kip', 'koe', 'konijn']

# For-each loop
# We hoeven niet na te denken over hoe lang de lijst is,
# of indices te gebruiken. Python doet iets vergelijkbaars met
# de loop hieronder voor je.
for dier in dieren:
    print(dier)

# For-loop met indices
for i in range(len(dieren)):
    print(dieren[i])

print("\n\n\n")
# Exercise: acronym
def acronym(zin):
    '''
    Maak een acronym van een gegeven zin.

    :param  string  Zin om een acronym van te maken:
    :return string  Acronym:
    '''
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

# Test de acronym functie
print(acronym("Be right back"))                 # BRB
print(acronym("Een aap die geen bananen eet"))  # EADGBE

# Nested loop pattern
# Je kunt binnen loops ook weer andere loops gebruiken. (let op de volgorde!)
# Je kunt het aantal iteraties van elke loop met elkaar vermenigvuldigen om
# een totaal te krijgen. Bijv: 10x een loop met een 10x loop erin betekent 100 iteraties.

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
# Open de lijst met kaartnummers (van opgave 6.2)
f = open('kaartnummers.txt')
# Lees alle regels uit het bestand in
lines = f.readlines()

# Maak een lege array aan voor de informatie
# over de personen
personen = []

# Loop over de lines uit het tekstbestand
for line in lines:
    # Strip de new line commando's
    clean_line = line.strip("\n")

    # Split de regel in een nummer en een naam
    persoon = clean_line.split(', ')

    # Sla de persoonsinformatie op
    personen.append(persoon)

# Loop over een array
for persoon in personen:
    # Selecteer informatie uit de subarrays
    naam, nummer = persoon[1], persoon[0]
    # Print de info
    print(f"{naam} heeft kaartnummer {nummer}")

# Nested loop pattern and 2-D lists
# Loop over een array
for persoon in personen:
    # Loop over alle informatie beschikbaar in de persoon-array
    for informatie in persoon:
        # Print de informatie
        print(informatie)

# Implement function pixels() that takes as input:
# • a two-dimensional list of nonnegative integer entries (representing the
# values of pixels of an image)
# and returns the number of entries that are positive (i.e., the number of pixels that are
# not dark). Your function should work on two-dimensional lists of any size.
def pixels(image):

    # Teller voor de pixels
    count = 0

    # Loop over de rijen
    for rij in image:
        # Loop over de kolommen
        for waarde in rij:
            print(f"We zitten nu op pixelwaarde {waarde}")
            # Check voor positieve waarde
            if (waarde > 0):
                # Verhoog de count
                count += 1
                print(f"Positief! Count: {count}")

    # Geef het totale aantal terug
    return count

image = [[1, 4, 5, 0], [4, 5, 3, 0], [0, 0, 3, 1], [14, 7, 9, 0]]
print(pixels(image))