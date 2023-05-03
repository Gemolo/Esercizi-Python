
def column(matrix, i):
    colonna = [];        
    for row in matrix:
        colonna.append(row[i])
    return colonna


def trasposta():
    A = [[1, 4, 5, 12],
     [1, 4, 5, 12],
     [1, 4, 5, 12],
     [1, 4, 5, 12]
     ]
    
    B = [[8, 3, 4 ,6],
         [1, 5, 9, 6],
         [6, 7, 2, 6],        
    ]
    
    traspostaMatrix = []
    
    for i in range(len(B[i])):
        traspostaMatrix.append(column(B, i))
    
    print(traspostaMatrix)
    
trasposta()