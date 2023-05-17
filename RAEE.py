import os

def clear():
    os.system("cls")
def menu():
    print("""
        - Grandi elettrodomestici;
        - Piccoli elettrodomestici;
        - Apparecchiature informatiche e per telecomunicazioni;
        - Apparecchiature di consumo e pannelli fotovoltaici;
        - Apparecchiature di illuminazione;
        - Utensili elettrici ed elettronici;
        - Giocattoli e apparecchiature per il tempo libero e lo sport;
        - Dispositivi medici (ad eccezione di tutti i prodotti impiantati ed infettati;
        - Strumenti di monitoraggio e di controllo;
        - Distributori automatici.
        """)

def menù_smaltimento():
    clear()
    n = int(input("""
        
            Benvenuti nel menù di smaltimento del gruppo HIDA_ASSANE:
            1- Smaltire Rifiuto
            2- Smaltire Rifiuto dalla lista
    
    """))
    clear()
    return n
def smaltimentoLista():
    
    clear()
    n = int(input("""
        1. Grandi elettrodomestici;
        2. Piccoli elettrodomestici;
        3. Apparecchiature informatiche e per telecomunicazioni;
        4. Apparecchiature di consumo e pannelli fotovoltaici;
        5. Apparecchiature di illuminazione;
        6. Utensili elettrici ed elettronici;
        7. Giocattoli e apparecchiature per il tempo libero e lo sport;
        8. Dispositivi medici (ad eccezione di tutti i prodotti impiantati ed infettati;
        9. Strumenti di monitoraggio e di controllo;
        10. Distributori automatici.
    
    """))
def leggiRifiuto():
    clear()
    menu()
    rifiuto  = input("Inserisci il rifiuto : ")

def sceltaRaee():
    
    raee1 = [ "Frigoriferi" , "Condizionatori", "Congelatori" ]
    raee2 = [ "Lavastoviglie" , "Lavatrici" ]
    raee3 = ["Tv","Monitor"]
    raee4 = ["Elettrotensili","Giocattoli","Apparrecchi di illuminazione","Dispositivi medici","Piccoli elettrodomestici"]
    raee5 = ["Sorgenti luminose compatte"," Lampade fluorescenti"]
    raee =  [raee1,raee2,raee3,raee4,raee5]
    rifiuto = leggiRifiuto()
    clear()
    for i in range(1,6):
        
        for x in raee:
           for y in x:
                
            if y == rifiuto:
                print(y)
    pass



s = menù_smaltimento()

match s:
    case 1:
        pass
    case 2:
         rifiuto = smaltimentoLista()
         sceltaRaee()
