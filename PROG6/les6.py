weekdag = "Maandag"
dag = 26
maand = "September"
jaar = 2022
uur = 14
minuut = 12

# Traditionele print
print(weekdag + ' ' + str(dag) + ' ' + maand + ' ' + str(jaar))

# Format-functie
print("{} {} {} {}".format(weekdag, dag, maand, jaar))

# f-string (literal string interpolation)
print(f"{weekdag} {dag} {maand} {jaar}")