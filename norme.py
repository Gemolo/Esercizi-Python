
def column(matrix, i):
    colonna = [];        
    for row in matrix:
        colonna.append(row[i])
    return colonna

def sommaInAbs(arr):
    somma = 0
    for i in range(len(arr)):
        somma += abs(arr[i])
    return somma

def normaUno(matrix):
    max = -1
    for i in range(len(matrix)):
        colonna = column(matrix, i)
        sommaColonna = sommaInAbs(colonna)
        if max < sommaColonna:
            max = sommaColonna
    return max

def normaInfinito(matrix):
    max  = -1
    for i in range(len(matrix)):
        sommaRiga =  sum(matrix[i])  
        if max < sommaRiga:
            max = sommaRiga
    return max

def trasposta():
    A = [[1, 4, 5, 12],
     [1, 4, 5, 12],
     [1, 4, 5, 12],
     [1, 4, 5, 12]
     ]
    
    B = [[8, 3, 4],
         [1, 5, 9],
         [6, 7, 2],        
    ]
    
    print(normaUno(A))
    print(normaInfinito(A))
    
trasposta()