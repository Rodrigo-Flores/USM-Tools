import os

class grade:
    def __init__(self, requirement=0, score=0):
        self.requirement = requirement
        self.score = score

    def approve(self):
        quantity = len(list(self.score))

        if quantity == 1:
            total = self.score
        
        else:
            total = sum(self.score) / quantity

        if total >= self.requirement:
            return True

        else:
            return False

    def mean(self):
        quantity = len(list(self.score))
        print(self.score)

        if quantity == 1:
            total = self.score[0]
        
        else:
            total = sum(self.score)/quantity

        return total

class save:
    def __init__(self):
        pass

nombre = input('Nombre del ramo: ')
requisitos = int(input("Cantidad de requisitos para el ramo: "))

lista_requisitos = []
for i in range(requisitos):
    x = input("Ingrese identificacion de requisito: ")
    z = int(input('Ingrese cantidad de notas de ' + x + ': '))
    y = int(input('Ingrese porcentaje de ' + x + ' (0 - 100): '))
    y = y/100

    lista_requisitos.append([x,y,z])

lista_puntaje = []
for i in lista_requisitos:
    nota_semifinal = []
    for n in range(i[2]):
        nota = int(input('Ingrese nota para ' + i[0] + ': '))
        nota_semifinal.append(nota)

    main = grade(score=nota_semifinal)
    lista_puntaje.append(main.mean())
        
print(lista_puntaje)
print(lista_requisitos)

