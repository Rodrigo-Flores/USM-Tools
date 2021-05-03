import math
import os

class Distancia:
    def __init__(self,numero):
        self.numero = numero

    # Metros
    def cm_to_m(self):
        metros = self.numero/100
        return metros

class Tiempo:
    def __init__(self,distancia):
        self.distancia = distancia

    def calcular_tiempo(self):
        tiempo = math.sqrt(((2*self.distancia)/9.81))
        return tiempo

tipo_distancia = input("¿Su distancia esta en metros o cemtimetros? m/c: ")

if tipo_distancia=="c":
    dato = float(input("Ingrese dato: "))
    distancia = Distancia(dato)
    final = distancia.cm_to_m()

elif tipo_distancia=="m":
    final = float(input("Ingrese dato: "))

else:
    os.system("exit")

resultado = Tiempo(final)
tiempo_final = round(resultado.calcular_tiempo(),2)
print(tiempo_final,"[s]")
