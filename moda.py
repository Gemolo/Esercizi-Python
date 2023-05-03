def moda(lista):
    if(len(lista) == 0): 
        raise Exception("Lista vuota")
    ret = lista[0]
    countRet = 1
    for i in range(len(lista)):
        countTemp = 1
        for j in range(len(lista)):
            if(i == j):
                continue
            else:
                if(lista[i] == lista[j]):
                    countTemp += 1
        if(countTemp > countRet):
            ret = lista[i]
            countRet = countTemp
        countTemp = 0
    return ret
print(moda([1, 2, 3, 4, 4, 5]))