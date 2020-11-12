import math
from docs import removeDuplicate, removeDuplicate2

def sortHasil(arrayHasil, arrayDokumen, array_count_kata, termTabel):     #arrayDokumen = filenames
    n = len(arrayHasil)
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arrayHasil[j] < arrayHasil[j+1] : 
                arrayHasil[j], arrayHasil[j+1] = arrayHasil[j+1], arrayHasil[j]
                arrayDokumen[j], arrayDokumen[j+1] = arrayDokumen[j+1], arrayDokumen[j]
                termTabel[j], termTabel[j+1] = termTabel[j+1], termTabel[j]
                array_count_kata[j], array_count_kata[j+1] = array_count_kata[j+1], array_count_kata[j]
    return arrayHasil, arrayDokumen, array_count_kata, termTabel

def dotProduct (ArrayHasil, IdxDocs) :
    sum = 0
    for j in range(len(ArrayHasil[0])):
        sum += ArrayHasil[0][j] * ArrayHasil[IdxDocs][j]
    return sum

def besar(ArrayHasil, IdxDocs):
    sum = 0
    for j in range(len(ArrayHasil[IdxDocs])):
        sum += pow(ArrayHasil[IdxDocs][j],2)
    return math.sqrt(sum)

def sim(ArrayHasil):
    sim = [0 for i in range(len(ArrayHasil))]
    Q = besar(ArrayHasil, 0)
    for i in range(1,len(sim)):
        D = besar(ArrayHasil, i)
        dotQD = dotProduct(ArrayHasil, i)
        sim[i] = dotQD / (Q * D)
    return sim

def countFoundTerm(term, stemmedData, stemmedQuery, tabel):
    if (tabel):
        TERM = removeDuplicate2(stemmedQuery)
        TERM.sort()
    else:
        TERM = removeDuplicate(term)
        TERM.sort()
    arrayHasil = [[0 for i in range(len(TERM))] for j in range(len(stemmedData)+1)]
    for i in range(len(stemmedData)):
        termDocs = stemmedData[i].split() 
        for j in range (len(TERM)):
            for k in range (len(termDocs)):
                if (TERM[j] == termDocs[k]):
                    arrayHasil[i+1][j] += 1
    termQuery = stemmedQuery
    for j in range (len(TERM)):
            for k in range (len(termQuery)):
                if (TERM[j] == termQuery[k]):
                    arrayHasil[0][j] += 1
    return arrayHasil