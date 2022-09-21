# Stel een waarde voor c in
c = 2

def pythagoras(a, b):
    'Bereken de waarde van een lange zijde met de stelling van Pythagoras'

    # Tel a^2 en b^2 bij elkaar op
    a2b2 = a**2 + b**2

    # Pak daar de wortel van (tot de macht 1/2)
    c = a2b2**(1/2)

    return c

# Bereken de waarde van de lange zijde (5.0)
print(pythagoras(3, 4))

# Wat komt hieruit?
print(c)

# Loop over de getallen van 0 tot 5.
for i in range(5):
    print(i)

print(i)