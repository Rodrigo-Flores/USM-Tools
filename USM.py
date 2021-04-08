from colorama import Fore, Back

def horas_clases(clases):
    minutos_semana = clases * 70
    minutos_total = minutos_semana * 19
    horas_clases = round(minutos_total/60,1)

    return horas_clases

class horas_cronologicas:
    def __init__(self,total,ramo):
         self.total=total
         self.ramo=ramo

    def personal(self):
        personal = self.total - self.ramo
        return personal

def FIS100():
    clases = float(input("Ingrese la cantidad de clases por semana que tiene de FIS100: "))
    fisica_total=float(input("Introduzca horas totales de FIS100: "))
    fisica=horas_cronologicas(fisica_total,horas_clases(clases))
    horas_semanales=round((fisica.personal())/19,1)

    mensaje1 = "\nLa cantidad de horas que debes dedicar por tu cuenta es: "
    mensaje2 = "\nAdemas, por semana tienes que dedicarle: "

    print(mensaje1,fisica.personal(), "[Hrs]")
    print(mensaje2,horas_semanales, "[Hrs]")

def EFI100():
    clases = float(input("Ingrese la cantidad de clases por semana que tiene de EFI100: "))
    deporte_total=float(input("Introduzca horas totales de EFI100: "))
    deporte=horas_cronologicas(deporte_total,horas_clases(clases))
    horas_semanales=round((deporte.personal())/19,1)

    mensaje1 = "\nLa cantidad de horas que debes dedicar por tu cuenta es: "
    mensaje2 = "\nAdemas, por semana tienes que dedicarle: "

    print(mensaje1,deporte.personal(), "[Hrs]")
    print(mensaje2,horas_semanales, "[Hrs]")

def HRW133():
    clases = float(input("Ingrese la cantidad de clases por semana que tiene de HRW133: "))
    etica_total=float(input("Introduzca horas totales de HRW133: "))
    etica=horas_cronologicas(etica_total,horas_clases(clases))
    horas_semanales=round((etica.personal())/19,1)

    mensaje1 = "\nLa cantidad de horas que debes dedicar por tu cuenta es: "
    mensaje2 = "\nAdemas, por semana tienes que dedicarle: "

    print(mensaje1,etica.personal(), "[Hrs]")
    print(mensaje2,horas_semanales, "[Hrs]")

def IWI131():
    clases = float(input("Ingrese la cantidad de clases por semana que tiene de IWI131: "))
    programacion_total=float(input("Introduzca horas totales de IWI131: "))
    programacion=horas_cronologicas(programacion_total,horas_clases(clases))
    horas_semanales=round((programacion.personal())/19,1)

    mensaje1 = "\nLa cantidad de horas que debes dedicar por tu cuenta es: "
    mensaje2 = "\nAdemas, por semana tienes que dedicarle: "

    print(mensaje1,programacion.personal(), "[Hrs]")
    print(mensaje2,horas_semanales, "[Hrs]")

def MAT021():
    clases = float(input("Ingrese la cantidad de clases por semana que tiene de MAT021: "))
    matematica_total=float(input("Introduzca horas totales de MAT021: "))
    matematica=horas_cronologicas(matematica_total,horas_clases(clases))
    horas_semanales=round((matematica.personal())/19,1)

    mensaje1 = "\nLa cantidad de horas que debes dedicar por tu cuenta es: "
    mensaje2 = "\nAdemas, por semana tienes que dedicarle: "

    print(mensaje1,matematica.personal(), "[Hrs]")
    print(mensaje2,horas_semanales, "[Hrs]")

print(Fore.GREEN + "Bienvenido/a a la Calculadora de Tiempo Dedicado.\nPor favor, elije una opcion.\n")

elec=1
while elec!=0:
    print("0. Salir")
    print("1. FIS100")
    print("2. EFI100")
    print("3. HRW133")
    print("4. IWI131")
    print("5. MAT021")

    try:
        elec=int(input("\nIngresa una opcion: "))
    except ValueError:
        elec=int(input("\nIngresa un valor dentro de las opciones: "))

    if elec==1:
        FIS100()
    elif elec==2:
        EFI100()
    elif elec==3:
        HRW133()
    elif elec==4:
        IWI131()
    elif elec==5:
        MAT021()
    elif elec==0:
        print("Saliendo...")
    else:
        print("\nEsa opcion no existe. Intenta nuevamente...\n")
