import math
#
# Si scriva un programma in Python che in base alla scelta dell’utente permetta di calcolare il perimetro di diverse
# figure geometriche (scegliete pure quelle che volete voi). Per la risoluzione dell’esercizio abbiamo scelto:
#
# ● Quadrato (perimetro = lato*4).
# ● Cerchio (circonferenza = 2*pi greco*r).
# ● Rettangolo (perimetro= base*2 + altezza*2).
# #

#DEFINIZIONE FUNZIONI

def perimetroQuadrato(lato_quadrato):
    return lato_quadrato*4

def calcoloCirconferenza(raggio_circonferenza):
    return (2*math.pi)*raggio_circonferenza

def perimetroRettangolo(base_rettangolo, altezza_rettangolo):
    return (base_rettangolo * 2) + (altezza_rettangolo * 2)

def perimetroTriangolo(lato_1_triangolo, lato_2_triangolo, lato_3_triangolo):
    return lato_1_triangolo + lato_2_triangolo + lato_3_triangolo


#CORPO DEL PROGRAMMA

#MENU DEL PROGRAMMA
print("***CALCOLO PERIMETRO***\nScegli la figura di cui vuoi che ti calcoli il perimetro:\n1. Quadrato\n2. Cerchio\n3. Rettangolo\n4. Triangolo")
figura_scelta = int (input("Digita il numero corrispondente alla figura scelta: "))

#CONTROLLO SULL'INPUT DELL'UTENTE
if(figura_scelta == 1):
    print("\nCALCOLO PERIMETRO DEL QUADRATO")
    lato_quadrato = float (input("Digita misura del lato del quadrato in cm: "))
    print(f"Il perimetro del quadrato di lato {lato_quadrato} è: ", perimetroQuadrato(lato_quadrato))
elif(figura_scelta == 2):
    print("\nCALCOLO PERIMETRO DELLA CIRCONFERENZA")
    raggio_circonferenza = float (input("Digita misura del raggio della circonferenza in cm: "))
    print(f"Il perimetro della circonferenza di raggio {raggio_circonferenza} è: ", calcoloCirconferenza(raggio_circonferenza))
elif(figura_scelta == 3):
    print("\nCALCOLO PERIMETRO DEL RETTANGOLO")
    base_rettangolo = float (input("inserisci la misura della base del rettangolo in cm: "))
    altezza_rettangolo = float (input("inserisci la misura dell'altezza del rettangolo in cm: "))
    print(f"Il perimetro del rettangolo di base {base_rettangolo} e altezza {altezza_rettangolo} è: ", perimetroRettangolo(base_rettangolo, altezza_rettangolo))
elif(figura_scelta == 4):
    print("\nCALCOLO PERIMETRO DEL TRIANGOLO")
    lato_1_triangolo = float (input("inserisci la misura del primo lato del triangolo in cm: "))
    lato_2_triangolo = float (input("inserisci la misura del secondo lato del triangolo in cm: "))
    lato_3_triangolo = float (input("inserisci la misura del terzo lato del triangolo in cm: "))
    #Effettuo un controllo sulla lunghezza dei lati per definire il tipo di triangolo
    if(lato_1_triangolo != lato_2_triangolo and lato_1_triangolo != lato_3_triangolo and lato_2_triangolo != lato_3_triangolo):
        print("Si tratta di un triangolo scaleno.")
    elif((lato_1_triangolo == lato_2_triangolo and lato_1_triangolo != lato_3_triangolo) or (lato_2_triangolo == lato_1_triangolo and lato_2_triangolo != lato_3_triangolo) or (lato_3_triangolo == lato_1_triangolo and lato_3_triangolo != lato_2_triangolo) or (lato_1_triangolo != lato_2_triangolo and lato_2_triangolo == lato_3_triangolo)):
        print("Si tratta di un triangolo isoscele.")
    elif(lato_1_triangolo == lato_2_triangolo and lato_2_triangolo == lato_3_triangolo):
        print("Si tratta di un triangolo equilatero.")
    print(f"Il perimetro del triangolo con i lati rispettivamente di lunghezza {lato_1_triangolo}, {lato_2_triangolo} e {lato_3_triangolo} è: ", perimetroTriangolo(lato_1_triangolo, lato_2_triangolo, lato_3_triangolo))
else:
    print("\nScelta non presente!!")


