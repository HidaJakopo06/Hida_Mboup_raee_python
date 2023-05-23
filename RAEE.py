import os
import time
import tkinter

from datetime import datetime

def stampa (raee):
    var = 1
    for i in raee:
        print(f"Categoria di rifiuti numero {var}: \n")
        for elemento in i:
            print(elemento,end=", ")
        print("\n")
        var += 1

        
def apertura(raee):
    percorso = f"File/R{raee}.txt"
    file = open(percorso, "a")
    return file


def ora():
    now = datetime.now()
    return now


def clear():
    os.system("cls")


def leggiRifiuto():
    while True:
        raee1 = [
                 "Congelatori",
                 "Frigoriferi a doppia porta",
                 "Frigoriferi side-by-side",
                 "Frigoriferi con dispenser di acqua/ghiaccio",
                 "Congelatori a cassetti",
                 "Frigoriferi commerciali",
                 "Congelatori commerciali",
                 "Armadi frigoriferi industriali"
        ]
        raee2 = [
            "Lavatrici",
            "Lavastoviglie",
            "Lavatrici a carica frontale",
            "Lavatrici a carica dall'alto",
            "Lavastoviglie a libera installazione",
            "Lavastoviglie da incasso",
            "Lavastoviglie compatte",
            "Lavastoviglie ad alta capacità"
        ]
        raee3 = ["Televisori",
                 "Monitor",
                 "Schermi",
                 "Cornici digitali LCD",
                 "Laptop",
                 "Notebook"
        ]
        raee4 = [
            "Telefoni cellulari",
            "Tablet",
            "Computer desktop",
            "Laptop",
            "Stampanti",
            "Scanner",
            "Televisori",
            "Fotocamere digitali",
            "Videocamere",
            "Console di gioco",
            "Forni a microonde",
            "Robot da cucina",
            "Tostapane",
            "Aspirapolvere",
            "Lampadine a risparmio energetico",
            "Lampade fluorescenti",
            "Dispositivi medici"
        ]

        raee5 = ["Sorgenti luminose compatte",
                 "Lampade fluorescenti",
                 "Tubi fluorescenti",
                 "Led",
                 "Lampade a scarica"
        ]
        raee = [raee1, raee2, raee3, raee4, raee5]
        
        print(f"""
    Scegliere tra i seguenti rifiuti :
        """)
        stampa(raee)  
        
        
        rifiuto = input("Inserisci il rifiuto : ").capitalize()
        clear()
        for lista in raee:
            for elemento in lista:
                if elemento == rifiuto:
                    return rifiuto

        print("Rifiuto non esistente")


def sceltaRaee():
    while True:
        raee1 = [
                 "Congelatori",
                 "Frigoriferi a doppia porta",
                 "Frigoriferi side-by-side",
                 "Frigoriferi con dispenser di acqua/ghiaccio",
                 "Congelatori a cassetti",
                 "Frigoriferi commerciali",
                 "Congelatori commerciali",
                 "Armadi frigoriferi industriali"
        ]
        raee2 = [
            "Lavatrici",
            "Lavastoviglie",
            "Lavatrici a carica frontale",
            "Lavatrici a carica dall'alto",
            "Lavastoviglie a libera installazione",
            "Lavastoviglie da incasso",
            "Lavastoviglie compatte",
            "Lavastoviglie ad alta capacità"
        ]
        raee3 = ["Televisori",
                 "Monitor",
                 "Schermi",
                 "Cornici digitali LCD",
                 "Laptop",
                 "Notebook"
                 "Mouse"
                 "Tastiera"
        ]
        raee4 = [
            "Telefoni cellulari",
            "Tablet",
            "Computer desktop",
            "Laptop",
            "Stampanti",
            "Scanner",
            "Televisori",
            "Fotocamere digitali",
            "Videocamere",
            "Console di gioco",
            "Forni a microonde",
            "Robot da cucina",
            "Tostapane",
            "Aspirapolvere",
            "Lampadine a risparmio energetico",
            "Lampade fluorescenti",
            "Dispositivi medici"
        ]

        raee5 = ["Sorgenti luminose compatte",
                 " Lampade fluorescenti",
                 "Tubi fluorescenti",
                 "Led",
                 "Lampade a scarica"
                 
        ]
        raee = [raee1, raee2, raee3, raee4, raee5]

        rifiuto = leggiRifiuto()
        tmp = rifiuto.replace(" ", "")

        print(rifiuto)

        r = 0

        for lista in raee:
            r += 1
            for elemento in lista:
                elemento_2 = elemento.replace(" ", "")
                if elemento_2 == tmp:
                    print("Raee Trovato...")
                    r = str(r)

                    scrivi = apertura(r)
                    inserimento = ora()
                    tmp = inserimento.strftime("%d-%m-%Y")
                    tmp2 = inserimento.strftime("%H:%M:%S")

                    scrivi.write(
                        f"Il rifiuto {rifiuto} e' stato inserito il giorno :{tmp} all'ora: {tmp2}\n")

                    scrivi.close()
                    return "R"+r


yes = True

while yes:

    p = sceltaRaee()
    print("Il Raee del rifiuto è :", p)
    time.sleep(1.5)
    yes = input("Y per continuare - N per terminare: ").upper()
    if yes == "N":
        yes = False
    clear()
