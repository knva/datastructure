import datetime
#quick sort
def quickSort(L, low, high):
    i = low 
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j-1                                                             
        L[i] = L[j]
        while i < j and L[i] <= key:    
            i = i+1 
        L[j] = L[i]
    L[i] = key 
    quickSort(L, low, i-1)
    quickSort(L, j+1, high)
    return L

            
m_arr = [1,3,5,6,2,4,9,11,49,58,14]

starttime = datetime.datetime.now()

q_arr = quickSort(m_arr,0,10)

endtime = datetime.datetime.now()

print (q_arr)

print ((endtime - starttime).seconds)


