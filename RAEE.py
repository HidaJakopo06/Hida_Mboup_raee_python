import os,time

from datetime import datetime

def apertura(raee):
    percorso = f"File/R{raee}.txt"
    file = open(percorso,"a")
    return file

def ora():
    now = datetime.now()
    return now
  
def clear():
    os.system("cls")

def leggiRifiuto():
    while True:
        raee1 = ["Frigoriferi", "Condizionatori", "Congelatori","Deumidificatori","Pompe di calore","Radiatori a olio","Asciugatrici"]
        raee2 = ["Lavastoviglie", "Lavatrici","Apparecchi di cottura","Stufe elettriche","Piastre riscaldanti elettriche"]
        raee3 = ["Televisori", "Monitor","Schermi","Cornici digitali LCD","Laptop","Notebook"]
        raee4 = ["Elettroutensili", "Giocattoli", "Apparrecchi di illuminazione","Dispositivi medici", "Piccoli elettrodomestici"]
        raee5 = ["Sorgenti luminose compatte", " Lampade fluorescenti","Tubi fluorescenti","Led","Lamapade a scarica"]
        raee = [raee1, raee2, raee3, raee4, raee5]

        time.sleep(1.5)
        rifiuto = input("Inserisci il rifiuto : ").capitalize()

        for lista in raee:
            for elemento in lista:
                if elemento == rifiuto:
                    return rifiuto
                
        print("Rifiuto non esistente")
            


def sceltaRaee():
    while True:
        raee1 = ["Frigoriferi", "Condizionatori", "Congelatori","Deumidificatori","Pompe di calore","Radiatori a olio","Asciugatrici"]
        raee2 = ["Lavastoviglie", "Lavatrici","Apparecchi di cottura","Stufe elettriche","Piastre riscaldanti elettriche"]
        raee3 = ["Televisori", "Monitor","Schermi","Cornici digitali LCD","Laptop","Notebook"]
        raee4 = ["Elettroutensili", "Giocattoli", "Apparrecchi di illuminazione","Dispositivi medici", "Piccoli elettrodomestici"]
        raee5 = ["Sorgenti luminose compatte", " Lampade fluorescenti","Tubi fluorescenti","Led","Lampade a scarica"]
        raee = [raee1, raee2, raee3, raee4, raee5]
        
        rifiuto = leggiRifiuto()
        tmp = rifiuto.replace(" ","")
        
        print(rifiuto)
        
        r = 0
       
        for lista in raee:
            r += 1 
            for elemento in lista:
                elemento_2 = elemento.replace(" ","")
                
                if elemento_2 == tmp:
                    
                   
                    print("Raee Trovato...")
                    r = str(r)
                    
                    scrivi=apertura(r)
                    inserimento = ora()
                    tmp =inserimento.strftime("%d-%m-%Y")
                    tmp2 = inserimento.strftime("%H:%M:%S")
                    
                    scrivi.write(f"Il rifiuto {rifiuto} e' stato inserito il giorno :{tmp} all'ora: {tmp2}\n") 
                    
                    
                    scrivi.close()
                    return "R"+r  


yes = True

while yes:
    
    p = sceltaRaee()
    print("Il Raee del rifiuto è :",p)
    time.sleep(1.5)
    yes = input("Y per continuare - N per terminare: ").upper()
    if yes == "N":
        yes = False
    clear()

    