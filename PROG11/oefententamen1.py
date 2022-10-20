# Opdracht 1:
# Schrijf een functie isPositiefEnKleinerDan(x, y) waarin je bepaalt of gegeven getal ‘x’ een positief
# getal is, en kleiner dan getal ‘y’. De parameters x en y zijn van het type int. De functie geeft
# True terug als dat zo is, anders False. - https://prnt.sc/cN5f8Fk6kssP

def isPositief(x):
    return x >= 0

def kleinerDan(x, y):
    return y > x

def isPositiefEnKleinerDan(x, y):
    '''
    :param  int
    :param  int
    :return bool
    '''
    return (x >= 0) and (y > x)

print(isPositiefEnKleinerDan(0, 10))    # True
print(isPositiefEnKleinerDan(4, 4))     # False
print(isPositiefEnKleinerDan(-10, -15)) # False

