def sumOfRow(matrix, row):
    somma = 0
    for el in matrix[row]:
        somma += el
    return somma

def sumColumn(matrix, column):
    somma = 0
    for row in matrix:
        somma+= row[column] 
    return somma

def countForTypeOfMedal(typeMedal, matrix):
    match typeMedal:
        case "Oro":
           return sumColumn(matrix, 0)
        case "Argento":
           return sumColumn(matrix, 1)
        case "Bronzo":
           return sumColumn(matrix, 2)
        case _:
            return -1

def medalForNation(nations, matrix):
    f = open("totali.txt", "w")
    stringa = ""
    for i in range(len(nations)):
        stringa += nations[i] + " " + str(sumOfRow(matrix, i)) + "\n"
    f.write(stringa)
    

def generaMatrice():
    nazioni = []
    counts = []
    f = open("file-05.csv", "r")
    for i in f.readlines():
        i = i.strip('\n')
        riga = i.split(",")
        if(riga[0] != 'Nazione'):
            temp = []
            for j in range(len(riga)):
                if j == 0:
                    nazioni.append(riga[j])
                else:
                    temp.append(int(riga[j]))
            counts.append(temp)
    medalForNation(nazioni, counts)
    print(countForTypeOfMedal("Bronzo", counts))
generaMatrice()