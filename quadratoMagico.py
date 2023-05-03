
def column(matrix, i):
    colonna = [];        
    for row in matrix:
        colonna.append(row[i])
    return colonna

def getDiagonal(matrix):
    diagonal = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(i == j):
                diagonal.append(matrix[i][i])
    return diagonal

def getDiagonalReverse(matrix):
    diagonal = []
    for i in reversed(range(len(matrix))):
        for j in reversed(range(len(matrix[i]))):
            if(i == j):
                diagonal.append(matrix[i][i])
    return diagonal


def checkNumeri(matrix, n):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] > (n*n)):
                return -1
    return 1

def checkSomma(matrix, somma, n):
    
    if(checkNumeri(matrix, n) == -1):
        print("Problemi numeri maggiori di n * n")
   
    for i in range(len(matrix)):
                
         # controlliamo le righe
        if(sum(matrix[i]) != somma):
            print("Errore righe somma diversa")
            return -1
        
        # controlliamo le colonne
        colonna = column(matrix, i)
        if(sum(colonna) != somma):
            print("Errore colonne somma diversa")
            return -1
        
    # controlliamo la diagonale da sx a dx
    if(sum(getDiagonal(matrix)) != somma):
        print("Errore diagonale da sx a dx somma diversa")
        return -1
    
     # controlliamo la diagonale da dx a sx
    if(sum(getDiagonalReverse(matrix)) != somma):
        print("Errore diagonale da dx a sx somma diversa")
        return -1
    
    print("Quadrato magico")
    return 1
        
   
            

def quadratoMagico(n):
    A = [
     [1, 4, 5, 12],
     [1, 4, 5, 12],
     [1, 4, 5, 12],
     [1, 4, 5, 12]
     ]
  
    
    B = [[8, 3, 4],
         [1, 5, 9],
         [6, 7, 2],        
    ]
    
    
    # print(B[0])
    somma = sum(B[0])
    
    checkSomma(B, somma, n)
    
quadratoMagico(10)