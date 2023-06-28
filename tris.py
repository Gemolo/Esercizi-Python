import random

# Funzione per stampare la scacchiera
def stampa_scacchiera(scacchiera):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(scacchiera[i * 3 + j], "|", end=" ")
        print("\n-------------")

# Funzione per controllare se c'è una vittoria
def controlla_vittoria(scacchiera, simbolo):
    righe_vittoriose = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Righe
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonne
        [0, 4, 8], [2, 4, 6]               # Diagonali
    ]
    for riga in righe_vittoriose:
        if scacchiera[riga[0]] == scacchiera[riga[1]] == scacchiera[riga[2]] == simbolo:
            return True
    return False

# Funzione per giocare
def gioca():
    scacchiera = [" " for _ in range(9)]
    giocatore = "X"
    fine_partita = False

    # Loop principale del gioco
    while not fine_partita:
        stampa_scacchiera(scacchiera)

        if giocatore == "X":
            # Turno del giocatore umano
            mossa = int(input("Inserisci la tua mossa (0-8): "))
            if scacchiera[mossa] == " ":
                scacchiera[mossa] = giocatore
                if controlla_vittoria(scacchiera, giocatore):
                    print("Hai vinto!")
                    fine_partita = True
                giocatore = "O"
            else:
                print("Mossa non valida. Riprova.")

        else:
            # Turno del giocatore computer
            mossa = random.randint(0, 8)
            if scacchiera[mossa] == " ":
                scacchiera[mossa] = giocatore
                if controlla_vittoria(scacchiera, giocatore):
                    print("Hai perso!")
                    fine_partita = True
                giocatore = "X"

        if " " not in scacchiera:
            print("La partita è finita in pareggio!")
            fine_partita = True

    stampa_scacchiera(scacchiera)

# Esecuzione del gioco
gioca()
