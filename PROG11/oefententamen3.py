# Opdracht 3:
# De afstand tussen twee coördinaten kan je uitrekenen met de volgende formule:
# https://prnt.sc/z-KlTT_Ksvgb
import math

# Let op: worteltrekken doe je met math.sqrt() of machtsverheffen met exponent 0.5!
# Schrijf een programma waarin de gebruiker twee coördinaten moet invoeren.
# Print de afstand (afgerond op 4 decimalen). - https://prnt.sc/n1C2mVrHzuw4

x1 = int(input("x van coord1: "))
y1 = int(input("y van coord1: "))
x2 = int(input("x van coord2: "))
y2 = int(input("y van coord2: "))

# Formule opgesplitst
x_diff = (x2 - x1)**2
y_diff = (y2 - y1)**2
ans = math.sqrt(x_diff + y_diff)

# Hele formule in een keer
ans2 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Vergeet niet af te ronden!
print(f"De afstand is {round(ans, 4)}")