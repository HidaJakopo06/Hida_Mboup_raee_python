import os
def clear():
    os.system("cls")


def menù_smaltimento():
    clear()
    n = input("""
        
            Benvenuti nel menù di smaltimento del gruppo HIDA_ASSANE:
            1- Smaltire Rifiuto
            2- Smaltire Rifiuto dalla lista
    
    """)
    return n
def smaltimentoLista():
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
def sceltaRaee():
    pass

raee1 = [ "Frigoriferi" , "Condizionatori", "Congelatori" ]
raee2 = [ "Lavastoviglie" , "Lavatrici" ]
raee3 = ["Tv","Monitor"]
raee4 = ["Elettrotensili","Giocattoli","Apparrecchi di illuminazione","Dispositivi medici","Piccoli elettrodomestici"]
raee5 = ["Sorgenti luminose compatte"," Lampade fluorescenti"]


s = menù_smaltimento()
match s:
    case 1:
        pass
    case 2:
         rifiuto = smaltimentoLista()
         sceltaRaee()
