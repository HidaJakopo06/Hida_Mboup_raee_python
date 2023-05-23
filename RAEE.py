import os
import time
import tkinter as tk
from datetime import datetime

def stampa(raee):
    var = 1
    for i in raee:
        text.insert(tk.END, f"Categoria di rifiuti numero {var}:\n")
        for elemento in i:
            text.insert(tk.END, f"{elemento}, ")
        text.insert(tk.END, "\n\n")
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
        raee3 = [
            "Televisori",
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
        raee5 = [
            "Sorgenti luminose compatte",
            "Lampade fluorescenti",
            "Tubi fluorescenti",
            "Led",
            "Lampade a scarica"
        ]
        raee = [raee1, raee2, raee3, raee4, raee5]

        text.delete(1.0, tk.END)
        text.insert(tk.END, "Scegli tra i seguenti rifiuti:\n\n")
        stampa(raee)

        rifiuto = entry.get().strip().capitalize()
        entry.delete(0, tk.END)

        for lista in raee:
            for elemento in lista:
                if elemento.lower() == rifiuto.lower():
                    return rifiuto

        text.insert(tk.END, "Rifiuto non esistente\n\n")

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
        raee3 = [
            "Televisori",
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
        raee5 = [
            "Sorgenti luminose compatte",
            "Lampade fluorescenti",
            "Tubi fluorescenti",
            "Led",
            "Lampade a scarica"
        ]
        raee = [raee1, raee2, raee3, raee4, raee5]

        rifiuto = leggiRifiuto()
        tmp = rifiuto.replace(" ", "")

        text.insert(tk.END, f"Il rifiuto selezionato e ': {rifiuto}\n")

        r = 0

        for lista in raee:
            r += 1
            for elemento in lista:
                elemento_2 = elemento.replace(" ", "")
                if elemento_2.lower() == tmp.lower():
                    text.insert(tk.END, "Raee Trovato...\n")
                    r = str(r)

                    scrivi = apertura(r)
                    inserimento = ora()
                    tmp = inserimento.strftime("%d-%m-%Y")
                    tmp2 = inserimento.strftime("%H:%M:%S")

                    scrivi.write(
                        f"Il rifiuto {rifiuto} e ' stato inserito il giorno: {tmp} all'ora: {tmp2}\n")

                    scrivi.close()
                    text.insert(tk.END, f"Il Raee del rifiuto e ': R{r}\n")
                    return "R"+r

def continue_program():
    global yes
    p = sceltaRaee()
    yes = tk.messagebox.askyesno("Continua", f"Il Raee del rifiuto e ': {p}\nVuoi continuare?")
    if not yes:
        root.destroy()

# Creazione della finestra principale
root = tk.Tk()
root.title("Sistema di Gestione dei Rifiuti RAEE")
root.geometry("500x400")

# Etichetta per l'input del rifiuto
label = tk.Label(root, text="Inserisci il rifiuto:")
label.pack()

# Campo di input per il rifiuto
entry = tk.Entry(root)
entry.pack()

# Bottone per confermare l'inserimento del rifiuto
button = tk.Button(root, text="Conferma", command=continue_program)
button.pack()

# Area di testo per la visualizzazione dei risultati
text = tk.Text(root)
text.pack()

# Esecuzione del programma
root.mainloop()
