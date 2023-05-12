import random

def generaUnNumeroIntero():
    return random.randint(0, 100)

def indovinaNumero():
    numeroSegreto = generaUnNumeroIntero()
    risposta = -1
    while(risposta != numeroSegreto):
        risposta = int(input("Prova ad indovinare il numero: "))
        if risposta == numeroSegreto:
            print("Hai vinto!")
        if risposta < numeroSegreto:
            print("Alza")
        if risposta > numeroSegreto:
            print("Abbassa")
indovinaNumero()
