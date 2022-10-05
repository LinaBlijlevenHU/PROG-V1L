def kies_optie():
    '''
    Laat de gebruiker een optie uit het keuzemenu kiezen.
    :return int     Gekozen optie
    '''
    # Stel een variabele voor de optie in
    optie = 0

    while optie not in range(1, 6):
        optie = int(input("Kies een optie: \n"))

        if optie not in range(1, 6):
            print("Dit is geen geldige optie. Kies opnieuw.")
            print_keuzemenu()

    return optie

def print_keuzemenu():
    print("1. Hoeveel kluizen beschikbaar?")
    print("2. Ik wil een nieuwe kluis.")
    print("3. Ik wil iets uit mijn kluis pakken.")
    print("4. Ik wil mijn kluis teruggeven.")
    print("5. Stoppen")

# Print het keuzemenu
print_keuzemenu()

# Laat de gebruiker een optie kiezen
optie = kies_optie()

if(optie == 1):
    print("1. Hoeveel kluizen beschikbaar?")
elif(optie == 2):
    print("2. Ik wil een nieuwe kluis.")
elif (optie == 3):
    print("3. Ik wil iets uit mijn kluis pakken.")
elif (optie == 4):
    print("4. Ik wil mijn kluis teruggeven.")
else:
    print("Doei!")
    exit()