import os,time

def clear():
    os.system("cls")


def menu():

    print("""
        Scegliere il rifiuto da inserire:
        
        -Frigoriferi;
        -Condizionatori;
        -Congelatori;
        -Lavastoviglie;
        -Lavatrici;
        -Tv;
        -Elettroutensili;
        -Giocattoli;
        -Apparecchi di illuminazione;
        -Dispositivi medici
        -Piccoli elettrodomestici
        -Sorgenti luminose compatte
        -Lampade fluorescenti
        """)



def leggiRifiuto():
    while True:
        raee1 = ["Frigoriferi", "Condizionatori", "Congelatori"]
        raee2 = ["Lavastoviglie", "Lavatrici"]
        raee3 = ["Tv", "Monitor"]
        raee4 = ["Elettroutensili", "Giocattoli", "Apparrecchi di illuminazione",
                "Dispositivi medici", "Piccoli elettrodomestici"]
        raee5 = ["Sorgenti luminose compatte", " Lampade fluorescenti"]
        raee = [raee1, raee2, raee3, raee4, raee5]

        clear()
        menu()
        rifiuto = input("Inserisci il rifiuto : ").capitalize()
        for lista in raee:
            for elemento in lista:
                if elemento == rifiuto:
                    return rifiuto
                else:
                    print("Rifiuto di merda !!!")
            


def sceltaRaee():
    while True:
        raee1 = ["Frigoriferi", "Condizionatori", "Congelatori"]
        raee2 = ["Lavastoviglie", "Lavatrici"]
        raee3 = ["Tv", "Monitor"]
        raee4 = ["Elettroutensili", "Giocattoli", "Apparrecchi di illuminazione",
                "Dispositivi medici", "Piccoli elettrodomestici"]
        raee5 = ["Sorgenti luminose compatte", "Lampade fluorescenti"]
        raee = [raee1, raee2, raee3, raee4, raee5]
        rifiuto = leggiRifiuto()
        clear()
        r = 0
        for lista in raee:
            r += 1 
            for elemento in lista:
                if elemento == rifiuto:
                    print("Raee Trovato...")
                    r = str(r)
                    return "R"+r  


yes = True

while yes:
    
    r = sceltaRaee()
    print("Il Raee del rifiuto è :",r)
    time.sleep(2.5)
    yes = input("Y per continuare - N per terminare: ").upper()
    if yes == "N":
        yes = False
    clear()

    