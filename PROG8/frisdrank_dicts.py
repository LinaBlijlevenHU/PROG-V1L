def selecteer_product(producten):
    # Eerst hebben we geen product
    geldig_product = False

    # Tot we een geldig product hebben
    while not geldig_product:
        # Input van de gebruiker
        keuze = input("Kies een frisdrank: \n")

        # Voor alle producten
        for productnaam, prijs in producten.items():
            # Zoek een match voor de productkeuze
            if (productnaam == keuze):
                # We mogen nu de loop beeindigen
                geldig_product = True

                # Stel de productinformatie in
                product = {
                    'naam': productnaam,
                    'prijs': prijs
                }
            else:
                print("Dit is een ongeldige keuze.")
                print_producten(producten)

    return product


def print_producten(producten):
    print("Wij hebben de volgende producten")
    for key, value in producten.items():
        print(f"{key}: ${value}")

producten = {
    # key: value
    'Coca Cola': 1.10,
    'Fanta': 1.00,
    'Sprite': 0.90,
    'Fernandes': 1.50
}

print("Hallo! Welkom bij de frisdrankautomaat.")
print_producten(producten)
product = selecteer_product(producten)                  # Dict met naam, prijs
print(f"U heeft {product['naam']} gekozen.")
print(f"Wilt u {product['prijs']} euro inwerpen a.u.b.")

# # Lijst van keys met for-loop
# productnamen = []
# for naam in producten.keys():
#     productnamen.append(naam)
# print(productnamen)
#
# # Lijst van keys met list comprehension
# productnamen2 = [naam.lower() for naam in producten.keys()]
# print(productnamen2)