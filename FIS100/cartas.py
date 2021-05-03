import random

cartas = {"Corazon": 0, "Trebol": 0, "Diamante10": 0, "Diamante8": 0, "Pica": 0}
lst = ["N", "O", "E", "E", "S"]

direccion = ""

for i in range(10):
    aleatorio = random.randint(0,4)
    
    if aleatorio == 0:
        direccion += lst[aleatorio]

    elif aleatorio == 1:
        direccion += lst[aleatorio]

    elif aleatorio == 2:
        direccion += lst[aleatorio]

    elif aleatorio == 3:
        direccion += lst[aleatorio]

    elif aleatorio == 4:
        direccion += lst[aleatorio]

    if aleatorio == 0:
        cartas["Corazon"] += 1

    elif aleatorio == 1:
        cartas["Trebol"] += 1

    elif aleatorio == 2:
        cartas["Diamante10"] += 1

    elif aleatorio == 3:
        cartas["Diamante8"] += 1

    elif aleatorio == 4:
        cartas["Pica"] += 1

print('Corazon:', cartas["Corazon"])
print('Trebol:', cartas["Trebol"])
print('Diamante 10:', cartas["Diamante10"])
print('Diamante 8:', cartas["Diamante8"])
print('Pica:', cartas["Pica"])
print('Rec: ' + direccion)
