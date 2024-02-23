# MACALUSO ALESSANDRO 4^C INF. 16/02/2024
import random

# Costanti per lista.
QUANTITA = 0
PUNTI = 1

PAROLE_FILE = (open("280000_parole_italiane.txt", "r").read()).split("\n")  # Lista ottenuta facendo lo split del file
# con il carattere "\n"

# Dizionario contenente le lettere con la propria quantità e il proprio punteggio.
dizionario = {
    "a": [14, 1],
    "b": [3, 5],
    "c": [6, 2],
    "d": [3, 5],
    "e": [11, 1],
    "f": [3, 5],
    "g": [2, 8],
    "h": [2, 8],
    "i": [12, 1],
    "l": [5, 3],
    "m": [5, 3],
    "n": [5, 3],
    "o": [15, 1],
    "p": [3, 5],
    "q": [1, 10],
    "r": [6, 2],
    "s": [6, 2],
    "t": [6, 2],
    "u": [5, 3],
    "v": [3, 5],
    "z": [2, 8]
}


# Verifico l'utente abbia utilizzato almeno due lettere tra quelle a disposizione.
def verifica_input_utente(lettere_disponibili, utente):
    presenze = 0

    for carattere_utente in utente:
        if carattere_utente in lettere_disponibili:
            presenze += 1
            if presenze == 2:
                return True

    return False


# Calcolo punteggio della parola
def calcolo_punteggio(utente):
    punteggio = 0

    for char in utente:
        punteggio += dizionario[char][PUNTI]
    return punteggio


lettere_complete = []  # Tutte le lettere del gioco presenti per la loro quantità.
lettere_disposizione = []  # Lettere a disposizione dell'utente
punteggio_totale = 0
errore = False  # Serve per controllare se l'utente ha inserito una parola corretta o meno.

# Forma la lista contenente le lettere ripetute per la loro quantità.
for lettera in dizionario:
    for i in range(dizionario[lettera][QUANTITA]):
        lettere_complete.append(lettera)

while len(lettere_complete) >= 8:
    # Sceglie 8 lettere casuali tra tutte le lettere disponibili solo se l'utente non ha commesso errore.
    if not errore:
        for i in range(8):
            lettera_casuale = random.choice(lettere_complete)
            lettere_disposizione.append(lettera_casuale)
            lettere_complete.remove(lettera_casuale)

    # Stampa delle lettere a disposizione dell'utente e input parola.
    print(f"Lettere a disposizione per formare una parola: {lettere_disposizione}")
    input_utente = input("Parola da formare con le lettere date: ").lower()

    # Verifico che l'utente abbia utilizzato almeno due lettere tra quelle a disposizione e che l'input utente sia
    # Contenuto nel file (lista contenente tutte le parole del file)
    if verifica_input_utente(lettere_disposizione, input_utente) and input_utente in PAROLE_FILE:
        print(f"La parola {input_utente} è presente nel file.")
        print(f"Punteggio: {calcolo_punteggio(input_utente)}")
        punteggio_totale += calcolo_punteggio(input_utente)
        lettere_disposizione.clear()
        errore = False
    else:
        print(f"La parola {input_utente} non è presente nel file o fa un uso scorretto dei caratteri dati.")
        errore = True

print(f"Punteggio totale: {punteggio_totale}")
