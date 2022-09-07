'''
les2.py

Bevat een aantal voorbeelden rondom lijsten en tuples.
'''

###########
# Lijsten #
###########

# Maak een lijst van studenten aan
studenten = ['Alex', 'Rino', 'Bertram', 'Mike', 'Gillian', 'Richard', 'Jens']
studenten2 = ['Viktor', 'Jiemie', 'Michel', 'Abe', 'Eray']

# Checken of Viktor in de lijst staat
print('Viktor' in studenten)

# Checken of Mike niet in de lijst staat
print('Mike' not in studenten)

# Samenvoegen van lijsten (concatenation)
alle_studenten = studenten + studenten2
print(alle_studenten)

# Lijsten vermenigvuldigen
print(3 * alle_studenten)

# Selecteer Richard uit de lijst met alle studenten
print(alle_studenten[5])

# Tel het aantal studenten
print(len(alle_studenten))

# Selecteer de student met de naam vooraan het alfabet en
# de student met de naam achteraan het alfabet
print(min(alle_studenten))
print(max(alle_studenten))

# Bereken de som van een aantal getallen
# Dit kan dus niet met strings.
print(sum([1, 2, 3, 4, 5, 6]))

# Selecteer een element en pas een element aan
# Lijsten zijn mutable -> aanpasbaar.
alle_studenten[5]
alle_studenten[5] = 'Jessey'
print(alle_studenten)

# Definieer een string en probeer een letter aan te passen
# dit kan niet: strings zijn namelijk immutable
naam = 'Kosta'
print(naam[1])
#naam[1] = 'a'          # Werkt niet!

# Toepassingen van de len()
# Functie met argument (bijv. lijst/string)
print(len(alle_studenten))
print(len('Koen'))

# Toevoegen van elementen aan een lijst (append)
alle_studenten.append('Misael')
print(alle_studenten)

# Tel alle keren dat een naam voorkomt
print(alle_studenten.count('Jens'))
print(alle_studenten.count('Raven'))

# Check op welke index de naam Michel voorkomt
# Hiervoor moet de naam dus wel in de lijst staan
print(alle_studenten.index('Michel'))
#print(alle_studenten.index('Raven'))       # Error

# Verwijder de laatste student van de lijst
print(alle_studenten.pop())
print(alle_studenten)

# Verwijder een specifieke student uit de lijst
alle_studenten.remove('Rino')
print(alle_studenten)

# Sorteer onze lijst van studenten
alle_studenten.sort()
print(alle_studenten)

# Sorteer onze lijst van studenten in omgekeerde volgorde
alle_studenten.reverse()
print(alle_studenten)

######################
# Lijsten vs. tuples #
######################

# Maak een lijst en een tuple
lst = ['a', 'b', 'c', 'd']          # mutable/aanpasbaar
tup = (1, 2, 3, 4)                  # immutable/niet aanpasbaar

# Vraag een waarde op
print(lst[1])
print(tup[1])

# Pas een lijst aan
lst[1] = 'e'
print(lst)

# Tuples zijn niet aanpasbaar
#tup[1] = 5                         # ERROR

# Voorbeeldfunctie: wanneer gebruik je een tuple?
# In de praktijk weinig
def statistieken(lst):
    gem = sum(lst)/len(lst)
    # hier zouden we bijv. de mediaan en standaardafwijking berekenen

    return (gem, 0, 0)

(gem, med, stda) = statistieken([1, 2, 3, 4, 5])
print(f"Het gemiddelde is {gem}")
print(f"De mediaan is {med}")

