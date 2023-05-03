def media(urlFile):
    f = open(urlFile, "r")
    somma = 0.
    num = 0
    for i in f.readlines():
        somma += float(i)
        num += 1
    if (num == 0):
        raise Exception("Nessun valore inserito, media non valida")
    else:
        return somma/num

urlFileUtente = input("Dammi il nome del file: ")
print(media(urlFileUtente))
