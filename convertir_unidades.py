from time import *

class Distancia:
    def __init__(self,numero):
        self.numero = numero

    # Metros
    def cm_to_m(self):
        metros = self.numero/100
        return metros

    def km_to_m(self):
        metros = self.numero*1000
        return metros

    # Cemtimetros
    def m_to_cm(self):
        cemtimetros = self.numero*100
        return cemtimetros

    def km_to_cm(self):
        cemtimetros = self.numero*100000
        return cemtimetros

    # Kilometros
    def cm_to_km(self):
        kilometros = self.numero/100000
        return kilometros

    def m_to_km(self):
        kilometros = self.numero/1000
        return kilometros

# Metros
def CMTOM():
    dato = float(input("Ingrese dato a convertir: "))
    distancia = Distancia(dato)
    convertido = distancia.cm_to_m()
    print(dato,"[cm] <=>",convertido,"[m]\n")
    sleep(2)

def KMTOM():
    dato = float(input("Ingrese dato a convertir: "))
    distancia = Distancia(dato)
    convertido = distancia.km_to_m()
    print(dato,"[Km] <=>",convertido,"[m]\n")
    sleep(2)

# Cemtimetros
def MTOCM():
    dato = float(input("Ingrese dato a convertir: "))
    distancia = Distancia(dato)
    convertido = distancia.m_to_cm()
    print(dato,"[m] <=>",convertido,"[cm]\n")
    sleep(2)

def KMTOCM():
    dato = float(input("Ingrese dato a convertir: "))
    distancia = Distancia(dato)
    convertido = distancia.km_to_cm()
    print(dato,"[Km] <=>",convertido,"[cm]\n")
    sleep(2)

# Kilometros
def CMTOKM():
    dato = float(input("Ingrese dato a convertir: "))
    distancia = Distancia(dato)
    convertido = distancia.cm_to_km()
    print(dato,"[cm] <=>",convertido,"[Km]\n")
    sleep(2)

def MTOKM():
    dato = float(input("Ingrese dato a convertir: "))
    distancia = Distancia(dato)
    convertido = distancia.m_to_km()
    print(dato,"[m] <=>",convertido,"[Km]\n")
    sleep(2)

# Inicio del Programa

print("Bienvenido/a al Convertidor de Unidades. \n")
elec=1
while elec!=0:
    print("0. Salir")
    print("1. cm -> m")
    print("2. km -> m")
    print("3. m -> cm")
    print("4. km -> cm")
    print("5. cm -> km")
    print("6. m -> km")

    try:
        elec=int(input("\nIntroduce una opcion para convetir unidades: "))
    except:
        elec=int(input("\nIngresa un valor dentro de las opciones: "))

    if elec==1:
        CMTOM()
    elif elec==2:
        KMTOM()
    elif elec==3:
        MTOCM()
    elif elec==4:
        KMTOCM()
    elif elec==5:
        CMTOKM()
    elif elec==6:
        MTOKM()
    elif elec==0:
        print("Saliendo...")
        sleep(1)
    else:
        print("\nEsa opcion no existe. Intenta nuevamente...\n")
