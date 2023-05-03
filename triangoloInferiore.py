def generaTriangoloInferiore(n):
    ret = []
    num = 1
    for i in range(n):
        arr = []
        for j in range(i + 1):
            arr.append(num)
            num += 1
        ret.append(arr)
    return ret
    
    
print(generaTriangoloInferiore(7))
