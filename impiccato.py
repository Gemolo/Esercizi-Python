import random

dizionario = ["casa", 
            #   "ciao", "macchina", "lampada", "luce",
            #   "finestra", "tastiera", "mouse", "moto", "monitor", "motore"
              ]

def parolaIndovinataReset(parolaSegreta):
    ret = ""
    for c in parolaSegreta:
        ret = ret + "_"
    return ret

def pickRandomWord():
    numero = random.randint(0, len(dizionario) - 1)
    return dizionario[numero]

def stringContainsChar(stringa, carattere):
    ret = []
    for i in range(len(stringa)):
        if stringa[i] == carattere:
            ret.append(i)
    return ret

def printaVite(vite):
    switch = {
        0: '''
             _______
             |     |
             |     O
             |    /|\\
             |    / \\
            _|_''',
        1: '''
             _______
             |     |
             |     O
             |    /|\\
             |    /
            _|_''',
        2: '''
             _______
             |     |
             |     O
             |    /|\\
             |
            _|_''',
        3: '''
             _______
             |     |
             |     O
             |    /|
             |
            _|_''',
        4: '''
             _______
             |     |
             |     O
             |     |
             |
            _|_''',
        5: '''
             _______
             |     |
             |     O
             |
             |
            _|_''',
        6: '''
             _______
             |     |
             |
             |
             |
            _|_''',
        7: '''
             _______
             |
             |
             |
             |
            _|_''',
        8: '''
             
             
             
             
             
            _|_''',
        9: '''
             
             
             
             
             
             
            _|_''',
        10: '''
             
             
             
             
             
             
             
            _|_'''
    }    
    print(switch.get(vite))
    return ""

def impiccato():
    parolaSegreta = pickRandomWord()
    parolaIndovinata = parolaIndovinataReset(parolaSegreta)
    vite = 10
    vinto = False
    while vite > 0 and not vinto:
        lettera = input("Dimmi una lettera: ")
        lettereIndovinate = stringContainsChar(parolaSegreta, lettera)
        if len(lettereIndovinate) > 0:
            for i in lettereIndovinate:
                temp = list(parolaIndovinata)
                temp[i] = parolaSegreta[i]
                parolaIndovinata = "".join(temp)
        else:
            vite -= 1
        print(printaVite(vite), "Vite: " + str(vite))
        print(parolaIndovinata)
        if parolaIndovinata == parolaSegreta:
            vinto = True
        lettereIndovinate = []
    if(vite > 0):
        print("Hai vinto")
    else:
        print("Hai perso")
impiccato()
